""" 
Config Reader Utils for GroTLoC (python tool).

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
from collections import defaultdict

def dot_split_sections(cfg, default=None):
    """ Splits a configparser dict into dot-separated sections"""
    cfg_section_dict = cfg._sections
    new_dict = defaultdict(lambda: default)
    for full_section in cfg_section_dict.keys():
        split_section = full_section.split('.')
        cur_dict = new_dict
        for subsection in split_section:
            if subsection not in cur_dict:
                cur_dict[subsection] = defaultdict(lambda:default)
            cur_dict = cur_dict[subsection]
        cur_dict.update(
            defaultdict(lambda: default, cfg_section_dict[full_section])
        )
    return new_dict
