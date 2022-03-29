""" 
Incidence matrix widget for GroTLoC (python tool).

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
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import PySimpleGUI as sg
import numpy as np


def pysimplegui_pyplot_draw(fig_canvas, tool_canvas, fig):
    """
    Helper function to draw a PyPlot figure with it's toolbar in PySimpleGui

    Args:
        fig_canvas (?): pysimplegui canvas to draw the figure
        tool_canvas (?): pysimplegui canvas to draw the figure
        fig (?): pyplot figure to draw in the canvas
    """
    if fig_canvas.children:
        for child in fig_canvas.winfo_children():
            child.destroy()
    if tool_canvas.children:
        for child in tool_canvas.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=fig_canvas)
    figure_canvas_agg.draw()
    toolbar = NavigationToolbar2Tk(figure_canvas_agg, tool_canvas)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)


class IncidenceMatrix(GUIWidget):
    """
    Widget to display a 2d incidence matrix for loop candidates indices
    """

    def set_params(self, data_points, loop_candidates, **kwargs):
        """
        Args:
            data_points (DataFrame): data frame with data points
            loop_candidates (List[Tuple[int,int]]): pairs of candidate indexes
        """
        self.loop_candidates = loop_candidates
        # build incidence matrix
        size = data_points.shape[0]
        self.imat = np.empty((size, size))
        for a,b in self.loop_candidates:
            self.imat[a,b] = 1
            self.imat[b,a] = 1

    def get_layout(self):
        layout = [
            [sg.Canvas(key='figure', size=(400 * 2, 400))],
            [sg.Canvas(key='figure_controls')],
            [sg.Button('Plot')]
        ]
        return layout

    def get_window(self, layout):
        """
        This method should create a new window for the current object.
        """
        window = sg.Window('Incidence Matrix', layout, finalize=True)
        return window

    def matrix_figure(self):
        """ Helper function to plot with PyPlot """
        fig, ax = plt.subplots()
        ax.matshow(self.imat, cmap=plt.cm.Blues)
        return fig, ax

    def step(self, window, event, values):
        """
        This method receives an event and values for the window it's displaying
        and the window object.
        Presumably it operates on the window by inspecting the event and values.
        It can safely assume this is the window for this widget.
        """
        if event == 'Plot':
            fig, _ = self.matrix_figure()
            pysimplegui_pyplot_draw(
                window['figure'].TKCanvas, window['figure_controls'].TKCanvas,
                fig)
        if event == sg.WIN_CLOSED or event == 'broadcast_exit':
                window.close()
