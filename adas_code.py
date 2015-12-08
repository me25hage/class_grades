def read_data(x):
    import numpy as np
    columns = np.loadtxt(x,delimiter=',',unpack=True,dtype='int')
    grades = columns[1]
    return grades

