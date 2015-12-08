import numpy as np
def statistics(grades):

    mean = np.mean(grades)
    std = np.std(grades)
    high_score = max(grades)
    low_score = min(grades)
    
    return mean
    return std
    return high_score
    return low_score
