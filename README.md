# TSAD

# Perturbation Engine

## Introduction

The Perturbation Engine is a Python-based software component developed to inject synthetic anomalies into clean time-series datasets. Its main purpose is to generate realistic faulty sensor data that can be used for testing and evaluating Time-Series Anomaly Detection (TSAD) models.

The engine follows a modular design, where the configuration, perturbation logic, and execution are separated into different files. This makes the software easy to understand, modify, and reuse with different datasets.

## Perturbation Models

The engine currently supports six commonly occurring sensor faults:

* **Point Spike** – Introduces sudden spikes in the signal.
* **Gaussian Noise** – Adds random noise to a selected region of the signal.
* **Bias (Offset)** – Adds a constant value to simulate calibration errors.
* **Drift** – Gradually increases or decreases sensor values over time.
* **Flatline** – Keeps the sensor output constant to simulate a stuck sensor.
* **Dropout** – Replaces sensor values with zero to simulate temporary sensor failure.

Each perturbation is based on a simple mathematical model and can be configured according to the user's requirements.

## Project Structure

The perturbation engine consists of three Python files:

* **config.py** – Stores all user-defined parameters such as the input dataset, output file, sensor column, and perturbation settings.
* **perturbations.py** – Contains the implementation of all six perturbation functions.
* **run_engine.py** – Loads the dataset, applies the perturbations, and generates the final perturbed dataset.

## How to Use the Perturbation Engine

1. Place the input CSV file in the project folder.
2. Open `config.py`.
3. Update the following:

   * Input dataset name (`DATASET_FILE`)
   * Sensor column to perturb (`COLUMN_TO_PERTURB`)
   * Output file name (`OUTPUT_FILE`)
   * Perturbation parameters such as severity, start index, and length.
4. Save the configuration file.
5. Run `run_engine.py`.
6. The engine will generate a new CSV file containing the perturbed sensor data along with an `is_anomaly` column indicating the injected anomalies.

