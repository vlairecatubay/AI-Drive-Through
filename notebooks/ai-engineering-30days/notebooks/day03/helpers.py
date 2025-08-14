def normalizeNumberRange(range):
    minVal = min(range)
    maxVal = max(range)
    normalizeRange = [(x - minVal)/(maxVal - minVal) for x in range]
    return([(x - minVal)/(maxVal - minVal)] for x in range)