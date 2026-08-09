import pandas as pd
import numpy as np

from config import *
from perturbations import *

df = pd.read_csv(DATASET_FILE)

labels = np.zeros(len(df), dtype=int)

for column in COLUMNS_TO_PERTURB:

	signal = df[column]

	if POINT_SPIKE["enabled"]:
		signal, temp = add_point_spikes(
			signal,
			POINT_SPIKE["count"],
			POINT_SPIKE["severity"],
			RANDOM_SEED
		)
		labels = np.maximum(labels, temp)

	if GAUSSIAN_NOISE["enabled"]:
		signal, temp = add_gaussian_noise(
			signal,
			GAUSSIAN_NOISE["start"],
			GAUSSIAN_NOISE["length"],
			GAUSSIAN_NOISE["severity"],
			RANDOM_SEED
		)
		labels = np.maximum(labels, temp)

	if BIAS["enabled"]:
		signal, temp = add_bias(
			signal,
			BIAS["start"],
			BIAS["length"],
			BIAS["offset"]
		)
		labels = np.maximum(labels, temp)

	if DRIFT["enabled"]:
		signal, temp = add_drift(
			signal,
			DRIFT["start"],
			DRIFT["length"],
			DRIFT["slope"]
		)
		labels = np.maximum(labels, temp)

	if FLATLINE["enabled"]:
		signal, temp = add_flatline(
			signal,
			FLATLINE["start"],
			FLATLINE["length"]
		)
		labels = np.maximum(labels, temp)

	if DROPOUT["enabled"]:
		signal, temp = add_dropout(
			signal,
			DROPOUT["start"],
			DROPOUT["length"],
			DROPOUT["value"]
		)
		labels = np.maximum(labels, temp)

	df[column] = signal

df["is_anomaly"] = labels

df.to_csv(OUTPUT_FILE, index=False)

print("Perturbed dataset saved successfully.")
