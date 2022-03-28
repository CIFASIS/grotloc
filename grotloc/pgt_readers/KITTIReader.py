""" 
KITTI Odometry Format Reader part of the GroTLoC python tool

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

import pandas as pd


class KITTIReader():
    """
    Pose Ground-Truth reader that conforms to the KITTI Odometry format
    http://www.cvlibs.net/datasets/kitti/eval_odometry.php
    """
    
    # KITTI represents odometry in 4x4 homogeneous pose matrices
    # and only writes the 3x3 rotation and 3x1 translation.
    # The missing row would be [0, 0, 0, 1]
    KITTI_COL_NAMES = [
        'r11', 'r12', 'r13', 'tx',
        'r21', 'r22', 'r23', 'ty',
        'r31', 'r32', 'r33', 'tz'
    ]

    def read_pgt(self, input_file):
        poses = pd.read_csv(input_file, sep=' ', names=self.KITTI_COL_NAMES)
        return poses


class KITTITimestampedReader():
    """
    Pose Ground-Truth reader that conforms to the KITTI Odometry format
    http://www.cvlibs.net/datasets/kitti/eval_odometry.php
    with an additional initial timestamp column
    """
    
    # KITTI represents odometry in 4x4 homogeneous pose matrices
    # and only writes the 3x3 rotation and 3x1 translation.
    # The missing row would be [0, 0, 0, 1]
    KITTI_COL_NAMES = [
        'time',
        'r11', 'r12', 'r13', 'tx',
        'r21', 'r22', 'r23', 'ty',
        'r31', 'r32', 'r33', 'tz'
    ]

    def read_pgt(self, input_file):
        poses = pd.read_csv(input_file, sep=' ', names=self.KITTI_COL_NAMES)
        return poses
