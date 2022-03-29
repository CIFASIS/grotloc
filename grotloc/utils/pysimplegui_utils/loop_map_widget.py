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
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import PySimpleGUI as sg
import matplotlib.colors as mcolors


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


class ScatterMap3D(GUIWidget):
    """
    Widget to display a 3d scatter map with 3 components (x,y,z) and unions
    between candidates
    """

    def set_params(self, data_points, loop_candidates, columns, **kwargs):
        """
        Args:
            data_points (DataFrame): data frame with data points
            loop_candidates (List[Tuple[int,int]]): pairs of candidate indexes
        """
        self.data_points = data_points
        self.loop_candidates = loop_candidates
        self.columns = columns

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
        window = sg.Window('Scatter Map 3D', layout, finalize=True)
        return window

    def scatter_figure(self):
        """ Helper function to plot with PyPlot """
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        ax.set_xlabel(self.columns[0])
        xvals = self.data_points[self.columns[0]]

        ax.set_ylabel(self.columns[1])
        yvals = self.data_points[self.columns[1]]

        ax.set_zlabel(self.columns[2])
        zvals = self.data_points[self.columns[2]]

        # given the pairs of candidates as (i1,i2), get the pairs of loops as
        # ((x1,y1,z1),(x2,y2,z2))
        candidate_pairs = list(map(
            lambda i: [
                    (xvals.iloc[i[0]], yvals.iloc[i[0]], zvals.iloc[i[0]]),
                    (xvals.iloc[i[1]], yvals.iloc[i[1]], zvals.iloc[i[1]])
                ], self.loop_candidates
        ))

        color = mcolors.to_rgba('Crimson')
        lc = Line3DCollection(
            candidate_pairs, linewidth=0.5, linestyles='solid', color=color)
        
        ax.scatter3D(xvals, yvals, zvals, alpha=0.5, s=.1)
        ax.add_collection(lc)
        ax.autoscale_view()
        ax.margins(0.1)

        # Turn off tick labels
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.set_zticklabels([])

        return fig, ax

    def step(self, window, event, values):
        """
        This method receives an event and values for the window it's displaying
        and the window object.
        Presumably it operates on the window by inspecting the event and values.
        It can safely assume this is the window for this widget.
        """
        if event == 'Plot':
            fig, _ = self.scatter_figure()
            pysimplegui_pyplot_draw(
                window['figure'].TKCanvas, window['figure_controls'].TKCanvas,
                fig)
        if event == sg.WIN_CLOSED or event == 'broadcast_exit':
                window.close()


class ScatterMap2D(GUIWidget):
    """
    Widget to display a 2d scatter map with 2 components (x,y) and unions
    between candidates
    """

    def set_params(self, data_points, loop_candidates, columns, **kwargs):
        """
        Args:
            data_points (DataFrame): data frame with data points
            loop_candidates (List[Tuple[int,int]]): pairs of candidate indexes
        """
        self.data_points = data_points
        self.loop_candidates = loop_candidates
        self.columns = columns

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
        window = sg.Window('Scatter Map 2D', layout, finalize=True)
        return window

    def scatter_figure(self):
        """ Helper function to plot with PyPlot """
        fig = plt.figure()
        ax = fig.add_subplot()

        ax.set_xlabel(self.columns[0])
        xvals = self.data_points[self.columns[0]]

        ax.set_ylabel(self.columns[1])
        yvals = self.data_points[self.columns[1]]

        # given the pairs of candidates as (i1,i2), get the pairs of loops as
        # ((x1,y1,z1),(x2,y2,z2))
        candidate_pairs = list(map(
            lambda i: [
                    (xvals.iloc[i[0]], yvals.iloc[i[0]]),
                    (xvals.iloc[i[1]], yvals.iloc[i[1]])
                ], self.loop_candidates
        ))

        color = mcolors.to_rgba('Crimson')
        lc = LineCollection(
            candidate_pairs, linewidth=0.5, linestyles='solid', color=color)
        
        ax.scatter(xvals, yvals, alpha=1, s=10)
        ax.add_collection(lc)
        ax.autoscale_view()
        ax.margins(0.1)

        # Turn off tick labels
        ax.set_yticklabels([])
        ax.set_xticklabels([])

        return fig, ax

    def step(self, window, event, values):
        """
        This method receives an event and values for the window it's displaying
        and the window object.
        Presumably it operates on the window by inspecting the event and values.
        It can safely assume this is the window for this widget.
        """
        if event == 'Plot':
            fig, _ = self.scatter_figure()
            pysimplegui_pyplot_draw(
                window['figure'].TKCanvas, window['figure_controls'].TKCanvas,
                fig)
        if event == sg.WIN_CLOSED or event == 'broadcast_exit':
                window.close()