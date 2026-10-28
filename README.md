Open-Circuit Wind Tunnel: Design, Development, and Aerodynamic Testing

Overview

This project documents the design, construction, and experimental evaluation of a low-speed, open-circuit wind tunnel developed to investigate the aerodynamic performance of a wing model.

The system uses an axial fan to generate airflow through a test section, where force measurements are collected for a three-dimensional-printed NACA 2412 airfoil at different angles of attack. The project combines mechanical design, airflow visualization, electronic force measurement, data processing, and comparison with theoretical aerodynamic predictions.

The primary objective was to develop a functional, low-cost experimental setup for investigating aerodynamic forces and evaluating how the angle of attack affects the wing’s downforce-to-drag ratio.

Key Features

* Open-circuit wind tunnel: A compact tunnel designed to produce airflow through a defined test section.
* Airflow visualization: Tuft testing to observe qualitative flow-direction behavior.
* Electronic force measurement: A load-cell-based system for measuring aerodynamic forces.
* Signal processing: A retry-and-filter routine that collects valid readings, rejects failed or noisy reads, and calculates the sample mean.
* Aerodynamic testing: Force measurements collected at multiple angles of attack.
* Experimental comparison: Evaluation of measured aerodynamic performance against theoretical predictions and wind-tunnel correction methods.

Experimental Setup

The prototype was developed around the following configuration:

Parameter	Specification:
Tunnel type	Open-circuit wind tunnel
Fan	80 W axial fan
Test-section dimensions	140 × 140 mm
Nominal test-section airspeed	Approximately 10 m/s
Test model	3D-printed NACA 2412 airfoil
Wing chord	100 mm
Wing span	115 mm
Test configuration	Inverted wing for downforce measurements
Angle-of-attack range	0°–24°

These values describe the experimental configuration; actual airflow and force measurements may vary with operating conditions.

Repository Contents

The repository contains the project code and supporting files used to develop and operate the wind-tunnel measurement system.

* Source code: Control and data-acquisition code for the experimental setup.
* Data processing: Logic for collecting, filtering, and averaging force readings.
* Research documentation: Supporting information on the design, methodology, results, and limitations of the experiment.

Update this section with the actual filenames and folders in the repository so visitors can identify each file easily.

Data Acquisition and Filtering

Individual readings in the turbulent airflow showed too much variability for reliable force profiling. To address this, the measurement software uses a retry-and-filter loop that attempts up to 30 reads to collect a valid set of samples.

The routine:

1. Attempts to collect valid sensor readings.
2. Skips failed reads and noisy timeouts.
3. Calculates the sample mean from the collected valid readings.
4. Prints [Skipped - Fan Noise] when a reading is skipped.

This approach improves the consistency of the collected readings, although it does not eliminate all measurement uncertainty or establish the absolute accuracy of the force measurements.

Experimental Results

The wing was tested at multiple angles of attack to investigate the relationship between angle of attack and aerodynamic force.

The measured downforce-to-drag ratio reached a maximum of 3.24 at an angle of attack of 12° under the tested conditions.

The experimental optimum differed from the theoretical wind-tunnel prediction of 14°. This difference highlights the importance of test-section airflow, tunnel-wall effects, force-measurement uncertainty, and experimental setup when interpreting aerodynamic results.

The measured optimum applies to the wing and tunnel configuration tested in this project; it should not be assumed to represent the optimum for the same airfoil in unrestricted airflow.

Limitations

The results should be interpreted in the context of the experimental setup and measurement method.

* Tuft testing provides qualitative airflow information but does not directly measure velocity uniformity or turbulence intensity.
* Sensor calibration and reading variability affect the reliability of force measurements.
* Mounting hardware may influence measured aerodynamic forces.
* The test-section airflow and wall effects may cause the results to differ from open-air theoretical predictions.
* The estimated airflow power is not a direct measurement of the fan’s overall efficiency.

These limitations provide a basis for improving the experimental setup and measurement procedure.

Future Improvements

Potential extensions of this project include:

* Conducting a quantitative velocity survey across the test section.
* Improving force-sensor calibration and measurement repeatability.
* Investigating the influence of mounting hardware on measured forces.
* Measuring the fan’s electrical input and airflow conditions more directly.
* Adding a floor plate to investigate ground-boundary effects.
* Using trip strips to examine the effect of boundary-layer transition.
* Testing additional airfoil geometries and operating conditions.

References

The research draws on established wind-tunnel testing methods and aerodynamic correction techniques, including:

* Barlow, J. B., Rae, W. H., Jr., & Pope, A. (1999). Low-speed wind tunnel testing (3rd ed.). John Wiley & Sons.
* Knight, M., & Harris, T. A. (1931). Experimental determination of jet boundary corrections for airfoil tests in four open wind tunnel jets of different shapes (NACA Technical Report No. 361). National Advisory Committee for Aeronautics.

Author and Contributions

This project was developed as an experimental engineering research project involving wind-tunnel construction, instrumentation, data acquisition, aerodynamic testing, and analysis.

The repository is intended to document the implementation and support further experimentation and development.
