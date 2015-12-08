import numpy as np
def statistics(grades):

    mean = np.mean(grades)
    std = np.std(grades)
    high_score = max(grades)
    low_score = min(grades)
    
    return mean,std,high_score,low_score
