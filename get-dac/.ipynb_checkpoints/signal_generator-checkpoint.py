import numpy as np
import time

def get_sin_wave_amplitude(freq: float, current_time: float) -> float:
    sin_val = np.sin(2 * np.pi * freq * current_time)
    normalized_amplitude = (sin_val + 1) / 2
    return normalized_amplitude

def get_triangle_wave_amplitude(freq: float, current_time: float) -> float:
    period = 1.0 / freq
    phase = (current_time % period) / period
    if phase < 0.5:
        return phase * 2.0
    else:
        return 2.0 - (phase * 2.0)

def wait_for_sampling_period(sampling_frequency: float):
    sampling_period = 1.0 / sampling_frequency
    time.sleep(sampling_period)
