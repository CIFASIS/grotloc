""" 
CSV Reader part of the GroTLoC python tool

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


from grispy import GriSPy
import numpy as np


class MultiGrispy:

    def __init__(self, data_points, data_tuples):
        """ TODO / FIXME """
        self.data_points = data_points
        self.size = self.data_points.shape[0]
        self.data_tuples = data_tuples

    def create_structure(self):
        self.grids = []
        for df_function, df_columns, df_parameters in self.data_tuples:
            df_data = self.data_points[df_columns].to_numpy()
            ds = GriSPy(df_data, metric=df_function)
            self.grids.append((ds, df_data, df_parameters))

    def query_neighbors(self):
        neighbor_tuples = []
        # For each point
        for point_idx in range(self.size):
            results_sets = []
            # Run all grid queries
            for ds, df_data, df_parameters in self.grids:
                query_point = df_data[point_idx]
                _, indexes = ds.shell_neighbors(np.array([query_point]), **df_parameters)
                indexes_plain = set(np.concatenate(indexes).ravel().tolist())
                results_sets.append(indexes_plain)
            result_intersection = set.intersection(*results_sets)
            # filter lower indices
            result_intersection = list(filter(lambda x: x >= point_idx, result_intersection))
            if result_intersection:
                neighbor_tuples.extend([(point_idx, ridx) for ridx in result_intersection])
        return neighbor_tuples