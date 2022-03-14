""" 
Angular Distance function part of the GroTLoC python tool

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__authors__ = ["Nicolas Soncini"]
__license__ = "GPLv3"
__version__ = "0.0.1"

# TODO: not final! Implementing as grispy custom distance for demonstration

import numpy as np


def _min_angle_difference(a1, a2):
    """
    Returns the minimum angular distance between two angles in the
    range (-180, 180] as a positive angle in the range [0, 180]
    
    Args:
        a1, a2 (num): two numbers representing the angles to compare

    Returns:
        (float): the signed angular distance (can be negative)
    """
    a1 = a1 + 360 if a1 < 0 else a1  # \in [0,360) now
    a2 = a2 + 360 if a2 < 0 else a2  # \in [0,360) now
    difference = (a2 - a1 + 180) % 360 - 180
    return abs(difference)


def angulardistance1d(c0, centres, dim):
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
        dis = _min_angle_difference(c0, c1)
        
        # store the distance
        distances[idx] = dis

    return distances
