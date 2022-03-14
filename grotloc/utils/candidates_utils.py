""" 
Loop Closure Candidates Handling Utils for GroTLoC (python tool).

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
import os


def write_candidate_pairs(
        loop_candidates, outdir, name='pairs', prefix='', suffix=''):
    """
    Writes pairs of candidates to a file
    """
    file_name = '_'.join(filter(None, [prefix, name, suffix])) + '.txt'
    file_path = os.path.join(outdir, file_name)
    with open(file_path, 'w') as f:
        for item in loop_candidates:
            f.write(f'{item}\n')
    return file_path