"""
Read a 100 g load cell through an HX711 amplifier on a PicoBricks (Pico W).

Wiring
  Load cell (4-wire)      HX711            HX711 -> PicoBricks
  E+ / red          ---------- E+              VCC  -> 3V3
  E- / black         ---------- E-              GND  -> GND
  A+ / white         ---------- A+              DT   -> DATA_PIN  (below)
  A- / green         ---------- A-              SCK  -> CLOCK_PIN (below)

PicoBricks already uses several GPIOs for its built-in modules (e.g. GP0 for
the IR receiver, GP4/GP5 for the I2C bus to the OLED). Wire the HX711 to two
free pins on the protoboard section and set them here.
"""

from machine import Pin
import utime

DATA_PIN = 2      # HX711 DT  -> pick a free GPIO on your board
CLOCK_PIN = 3     # HX711 SCK -> pick a free GPIO on your board

# ---- calibration ------------------------------------------------------
CALIBRATION_FACTOR = 12679.5 # counts per gram -- replace after calibrating


class HX711:
    def __init__(self, data_pin, clock_pin, gain=128):
        self.data = Pin(data_pin, Pin.IN, Pin.PULL_UP)  # Internal pull-up helps resist EMI
        self.clock = Pin(clock_pin, Pin.OUT)
        self.clock.value(0)
        self.offset = 0
        self.gain_pulses = {128: 1, 64: 3, 32: 2}[gain]
        
    def reset(self):
        """Forces the HX711 hardware chip out of power-down/sleep mode.""" # 
        self.clock.value(1)
        utime.sleep_us(100)  # Pulse HIGH > 60 us forces a complete chip reset
        self.clock.value(0)
        utime.sleep_ms(1)    # Give chip time to reset its internal ADC clock

    def is_ready(self):
        return self.data.value() == 0

    def read_raw(self, timeout_ms=200): 
        start = utime.ticks_ms()
        while not self.is_ready():
            if utime.ticks_diff(utime.ticks_ms(), start) > timeout_ms:
                # --- WAKE UP / HARDWARE RESET CYCLE ---
                self.clock.value(1)
                utime.sleep_us(80)  # >60us pulse forces HX711 power-down reset
                self.clock.value(0)
                utime.sleep_us(100) # Allow chip to reboot into 10Hz sampling mode
                return None
            utime.sleep_us(50)

        value = 0
        for _ in range(24):
            self.clock.value(1)
            value = (value << 1) | self.data.value()
            self.clock.value(0)

        for _ in range(self.gain_pulses):
            self.clock.value(1)
            self.clock.value(0)

        if value & 0x800000:
            value -= 1 << 24
        return value
    
    def read_average(self, times=10):
        valid_samples = []
        attempts = 0
        
        # Try collecting samples up to 30 times total
        while len(valid_samples) < times and attempts < 30:
            val = self.read_raw()
            if val is not None:
                valid_samples.append(val)
            else:
                # If a read timed out, force reset the hardware before the next try
                self.reset()
            attempts += 1
            utime.sleep_ms(2)

        if not valid_samples:
            return None  # Return None if the noise completely blocked all attempts
        return sum(valid_samples) / len(valid_samples)

    def tare(self, times=15):
        avg = self.read_average(times)
        if avg is not None:
            self.offset = avg
            return True
        return False

    def get_grams(self, times=5):
        raw = self.read_average(times)
        if raw is None:
            return None
        return (raw - self.offset) / CALIBRATION_FACTOR


def main():
    hx = HX711(DATA_PIN, CLOCK_PIN)

    print("Taring... keep the load cell empty")
    utime.sleep(1)
    if hx.tare():
        print("Tare complete. Offset =", hx.offset)
    else:
        print("Tare warning: Sensor noise detected during startup!")

    if CALIBRATION_FACTOR == 1.0:
        print("CALIBRATION_FACTOR not set yet -- printing raw counts.")
        print("Place your known reference weight now.")

    while True:
        if CALIBRATION_FACTOR == 1.0:
            raw = hx.read_average(5)
            if raw is not None:
                print("raw counts: {:.0f}".format(raw - hx.offset))
            else:
                print("raw counts: [Skipped - Fan Noise]")
        else:
            grams = hx.get_grams()
            if grams is not None:
                print("{:.2f} g".format(grams))
            else:
                print("[Skipped - Fan Noise]")
        utime.sleep(0.2)


if __name__ == "__main__":
    main()
