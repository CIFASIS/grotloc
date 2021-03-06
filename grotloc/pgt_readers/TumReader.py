""" 
TUM Format Reader part of the GroTLoC python tool

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


class TumReader():
    """
    Pose Ground-Truth reader that conforms to the TUM Ground Truth format
    https://vision.in.tum.de/data/datasets/rgbd-dataset/file_formats
    """
    
    def read_pgt(self, input_file):
        poses = pd.read_csv(input_file, sep=' ')
        return poses
