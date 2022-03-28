""" 
GUI Widget definition for GroTLoC (python tool).

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

from abc import ABC, abstractmethod


class GUIWidget(ABC):
    """
    Abstract Widget class to manage multiple widgets in separate windows with
    PySimpleGui format.
    This class has to be overriden by any/all widgets needed for GroTLoC 
    visualization tools.
    """

    @abstractmethod
    def set_params(self, **kwargs):
        """
        This method allows the parameters for a given widget to be changed but
        does not necessarily force the redraw of a window.
        It should accept partial or total modification of all modifiable params
        and not fail if a parameter is ommited (but can fail if the parameter
        is non existant).
        All parameters should default to an existing value unless this class
        explicitly asks for them (add as function parameters without defaults).
        """
        pass

    @abstractmethod
    def get_layout(self):
        """
        This method should return the layout for the current widget by using the
        parameters stored in this class.
        """
        pass

    @abstractmethod
    def get_window(self):
        """
        This method should create a new window for the current object.
        """
        pass

    @abstractmethod
    def step(self, window, event, values):
        """
        This method receives an event and values for the window it's displaying
        and the window object.
        Presumably it operates on the window by inspecting the event and values.
        It can safely assume this is the window for this widget.
        """
        pass
