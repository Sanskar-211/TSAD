DATASET_FILE = "sample_data.csv"

COLUMNS_TO_PERTURB = ["sensor_1", "sensor_2", "sensor_3"]

OUTPUT_FILE = "perturbed_dataset.csv"

RANDOM_SEED = 42

POINT_SPIKE = {
	"enabled": True,
	"count": 20,
	"severity": 4
}

GAUSSIAN_NOISE = {
	"enabled": True,
	"start": 400,
	"length": 150,
	"severity": 1.5
}

BIAS = {
	"enabled": True,
	"start": 700,
	"length": 120,
	"offset": 3
}

DRIFT = {
	"enabled": True,
	"start": 1000,
	"length": 200,
	"slope": 0.03
}

FLATLINE = {
	"enabled": True,
	"start": 1400,
	"length": 100
}

DROPOUT = {
	"enabled": True,
	"start": 1700,
	"length": 60,
	"value": 0
}
