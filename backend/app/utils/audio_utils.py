# Placeholder for audio helpers (VAD, resampling, etc.)
def level_meter(samples):
    return sum(abs(x) for x in samples) / max(1, len(samples))
