""" 
Image visualization widgets for GroTLoC (python tool).

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
import os

class ImageVisualization(GUIWidget):
    """
    Widget to display two images at a time from a list of pairs of paths to 
    images
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


class IndexedImagesFromFolder(ImageVisualization):
    """
    Widget to display two images at a time from a path that contains images
    indexed by the pose index.
    """

    def set_params(self, path, loop_candidates, ext='.png', **kwargs):
        """
        Args:
            path (str): top level path to the images
            loop_candidates (iter(Tuple[int,int])): pairs of indexes to display
            ext (str): extension for the images
            **kwargs:
                zero_pad (int): pad index with zeros for file name
        """
        self.zero_pad = kwargs.get('pad-with-zeros', 0)
        path_pairs = (
            (os.path.join(path, f'{i:0{self.zero_pad}}' + ext),
                os.path.join(path, f'{j:0{self.zero_pad}}' + ext)) 
            for i,j in loop_candidates
        )
        return super().set_params(path_pairs, **kwargs)
