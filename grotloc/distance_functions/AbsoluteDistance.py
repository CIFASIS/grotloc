# temporary for demonstration

import numpy as np

def absolutedistance(c0, centres, dim):
    """
    c0: the center to which we seek the distance. 
    centres: the C centers to which we want to calculate the distance from a c0. 
    dim: the dimension of each center and c0.

    Finally the function must return a np.ndarray with C elements where the 
    element j-nth corresponds to the distance between c0 and centres_j.
    """
    # creates a empty array with the required
    # number of distances
    distances = np.empty(len(centres))

    for idx, c1 in enumerate(centres):
        dis = abs(c0[0] - c1[0])

        # store the distance
        distances[idx] = dis

    return distances