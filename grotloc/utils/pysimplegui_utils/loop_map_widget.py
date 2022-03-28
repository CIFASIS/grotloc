""" 
Map visualization widgets for GroTLoC (python tool).

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

from grotloc.utils.pysimplegui_utils.gui_widget import GUIWidget
import PySimpleGUI as sg

class ScatterMap3D(GUIWidget):
    """
    Widget to display a 3d scatter map with 3 components (x,y,z) and unions
    between candidates

    TODO: REPLACE ALL
    """

    def set_params(self, path_pairs, **kwargs):
        """
        Args:
            path_pairs (Tuple[str,str]): pairs of paths to candidate images
        """
        self.path_pairs = iter(path_pairs)
        self.current_paths = next(self.path_pairs)

    def get_layout(self):
        layout = [
            [sg.Image(self.current_paths[0], key='im1_path')],
            [sg.Image(self.current_paths[1], key='im2_path')]
        ]
        return layout

    def get_window(self, layout):
        """
        This method should create a new window for the current object.
        """
        window = sg.Window('Image Visualization', layout, finalize=True)
        return window

    def step(self, window, event, values):
        """
        This method receives an event and values for the window it's displaying
        and the window object.
        Presumably it operates on the window by inspecting the event and values.
        It can safely assume this is the window for this widget.
        """
        if event == 'broadcast_next':
            try:
                self.current_paths = next(self.path_pairs)
                window['im1_path'].update(self.current_paths[0])
                window['im2_path'].update(self.current_paths[1])
            except StopIteration:
                window.close()
        if event == sg.WIN_CLOSED or event == 'broadcast_exit':
                window.close()