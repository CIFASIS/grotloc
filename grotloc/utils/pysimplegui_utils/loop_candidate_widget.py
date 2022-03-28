""" 
Image confirmation widgets for GroTLoC (python tool).

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


class LoopCandidateWidget(GUIWidget):
    """
    Widget to display candidate information, verification and control other
    widgets via specific events
    """

    def set_params(self, data_points, loop_candidates, **kwargs):
        """
        Args:
            data_points (DataFrame): data frame with data points
            loop_candidates (List[Tuple[int,int]]): pairs of candidate indexes
        """
        self.data_points = data_points
        self.loop_candidates = loop_candidates
        self.total = len(loop_candidates)
        self.lc_iterator = iter(enumerate(loop_candidates))
        self.current = next(self.lc_iterator)

    def get_layout(self):
        layout = [
            [
                sg.Text('Loop Candidate Pair'), 
                sg.Text(f'{self.current[0]}', key='current_index'),
                sg.Text('of'),
                sg.Text(f'{self.total}')
            ],
            [
                sg.Table(
                    [
                        self.data_points.values.tolist()[self.current[1][0]],
                        self.data_points.values.tolist()[self.current[1][1]]
                    ],
                    headings=self.data_points.columns.values.tolist(),
                    num_rows=2,
                    key='current_table'
                )
            ],
            [
                sg.Button('Next', key='broadcast_next'),
                sg.Button('Exit', key='broadcast_exit')
            ]
        ]
        return layout

    def get_window(self, layout):
        """
        This method should create a new window for the current object.
        """
        window = sg.Window('Loop Candidate Verification', layout, finalize=True)
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
                self.current = next(self.lc_iterator)
                window['current_index'].update(self.current[0])
                window['current_table'].update(
                    [
                        self.data_points.values.tolist()[self.current[1][0]],
                        self.data_points.values.tolist()[self.current[1][1]]
                    ]
                )
            except StopIteration:
                window.close()
        if event == sg.WIN_CLOSED or event == 'broadcast_exit':
                window.close()
