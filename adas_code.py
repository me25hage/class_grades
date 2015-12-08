def read_data(x):
    import numpy as np
    columns = np.loadtxt(x,delimiter=',',skiprows=1,unpack=True,dtype='int')
    grades = columns[1]
    return grades

print read_data('grades1.csv')
