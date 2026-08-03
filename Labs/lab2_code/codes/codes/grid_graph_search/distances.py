import numpy as np

def manhattan( n0, n1 ):
    return np.sum(np.abs( n0 - n1 ))

def euclidean( n0, n1 ):
    n0 = np.array( n0 )
    n1 = np.array( n1 )
    return np.sqrt( (( n0 - n1 ) ** 2).sum()  )

distances = {}
distances['manhattan'] = manhattan
distances['euclidean'] = euclidean