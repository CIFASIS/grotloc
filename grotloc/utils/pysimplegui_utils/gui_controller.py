""" 
GUI Controller for GroTLoC (python tool).

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


class GUIController():
    BROADCAST_KEY = 'broadcast'
    widgets = {}

    def add(self, widget: GUIWidget):
        layout = widget.get_layout()
        window = widget.get_window(layout)
        self.widgets[window] = widget

    def loop(self):
        while True:  # Event Loop
            window, event, values = sg.read_all_windows()
            # if all windows were closed
            if window == sg.WIN_CLOSED:
                break
            # if an event was prefixed with broadcast
            if event and event.startswith(self.BROADCAST_KEY):
                for window in self.widgets:
                    widget = self.widgets[window]
                    widget.step(window, event, values)
            else:
                widget = self.widgets[window]
                widget.step(window, event, values)
