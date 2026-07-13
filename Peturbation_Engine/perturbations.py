
import numpy as np

def _initialize(signal):
 
    perturbed = signal.copy()
    labels = np.zeros(len(signal), dtype=int)
    return perturbed, labels

def add_point_spikes(signal, count, severity, seed=None):

    if seed is not None:
        np.random.seed(seed)

    perturbed, labels = _initialize(signal)

    mean = signal.mean()
    std = signal.std()

    count = min(count, len(signal))

    indices = np.random.choice(len(signal), count, replace=False)

    for idx in indices:

        direction = np.random.choice([-1, 1])

        perturbed.iloc[idx] = mean + direction * severity * std

        labels[idx] = 1

    return perturbed, labels

def add_gaussian_noise(signal, start, length, severity, seed=None):

    if seed is not None:
        np.random.seed(seed)

    perturbed, labels = _initialize(signal)

    end = min(start + length, len(signal))

    std = signal.std()

    noise = np.random.normal(
        loc=0,
        scale=severity * std,
        size=end - start
    )

    perturbed.iloc[start:end] += noise

    labels[start:end] = 1

    return perturbed, labels

def add_bias(signal, start, length, offset):

    perturbed, labels = _initialize(signal)

    end = min(start + length, len(signal))

    perturbed.iloc[start:end] += offset

    labels[start:end] = 1

    return perturbed, labels


def add_drift(signal, start, length, slope):

    perturbed, labels = _initialize(signal)

    end = min(start + length, len(signal))

    drift = np.arange(end - start) * slope

    perturbed.iloc[start:end] += drift

    labels[start:end] = 1

    return perturbed, labels

def add_flatline(signal, start, length):

    perturbed, labels = _initialize(signal)

    end = min(start + length, len(signal))

    constant = signal.iloc[start]

    perturbed.iloc[start:end] = constant

    labels[start:end] = 1

    return perturbed, labels

def add_dropout(signal, start, length, value=0):

    perturbed, labels = _initialize(signal)

    end = min(start + length, len(signal))

    perturbed.iloc[start:end] = value

    labels[start:end] = 1

    return perturbed, labels
