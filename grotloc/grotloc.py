#!/usr/bin/env python
""" 
Ground Truth for Loop Closure (GroTLoC) python tool.

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

import argparse
import ast
import configparser
import importlib
import logging
import sys

from grispy import GriSPy
from grotloc.data_structures.MultiGrispy import MultiGrispy

from grotloc.utils.cfgreader_utils import dot_split_sections

# Setup Logging
logging.basicConfig()
logger = logging.getLogger('GroTLoC')
logger.setLevel(logging.DEBUG)


def parse_arguments(argv):
    """ Handles argument parsing """
    parser = argparse.ArgumentParser(
        prog='GroTLoC', 
        description='Ground Truth for Loop Closure (GroTLoC) python tool')

    # Config File
    parser.add_argument(
        '--cfg', help='Configuration file path', required=True)

    # Pose Graph File
    parser.add_argument(
        '--input', help='Input Pose Graph file path', required=True)

    # Output File
    parser.add_argument(
        '--output', help='Output file to write to', required=True)

    # Visualization
    parser.add_argument(
        '--display', action='store_true', help='Show final review tools')

    args = parser.parse_args()
    
    cfg = configparser.ConfigParser()
    cfg.read(args.cfg)
    cfg = dot_split_sections(cfg)
    
    return args, cfg


def load_poses(input_file, cfg):
    """ Loads the PGT given the loading format """
    try:
        pgt_module = importlib.import_module(cfg['input-include'])
        pgt_class = getattr(pgt_module, cfg['input-reader'])
    except Exception:
        logger.critical(
            'Could not import PGT reader %s from module %s', 
            cfg['input-reader'], cfg['input-include'], exc_info=True)
    logger.info(
        'Using PGT reader "%s" from module "%s"', pgt_class.__name__,
        pgt_module.__name__)

    pgt_reader = pgt_class()
    pgt = pgt_reader.read_pgt(input_file)

    logger.info('Read PGT with headers: %s', pgt.columns)
    return pgt


def load_distance_functions(data_points, cfg):
    logger.info('Loading Distance Functions named: %s', list(cfg.keys()))
    df_list = []
    for df_name in cfg:
        df_cfg = cfg[df_name]
        logger.debug('Loading Distance Function %s', df_name)
        try:
            df_module = importlib.import_module(df_cfg['function-include'])
            df_function = getattr(df_module, df_cfg['function-name'])
            df_columns = df_cfg['function-columns'].split(',')
            # TODO: check that columns are actually in the data_points
            df_parameters = ast.literal_eval(df_cfg['function-parameters'])
            # TODO: verify parameters
            df_tuple = (df_function, df_columns, df_parameters)
            logger.debug('Queuing function: %s', df_tuple)
            df_list.append(df_tuple)
        except Exception:
            logger.critical(
                'Could not import Distance Function %s from module %s', 
                df_cfg['function-name'], df_cfg['function-include'], exc_info=True)
            raise
    return df_list


def build_data_structure(data_points, distance_fns, cfg):
    # Right now only one data structure type is supported
    if not cfg['type'] == 'multi-grispy':
        logger.critical('Data structure type %s not supported', cfg['type'])
        exit(1)

    data_structure = MultiGrispy(data_points, distance_fns)
    data_structure.create_structure()

    return data_structure


def query_loop_candidates(data_structure):
    neighbor_indices = data_structure.query_neighbors()
    logger.debug('Found %s candidates', len(neighbor_indices))
    return neighbor_indices


def display_candidates(loop_candidates):
    logger.warning('Display not yet implemented!')
    exit(1)


def grotloc(argv):
    """
    This function serves as the main entry point of the GroTLoC tool.
    """
    args, cfg = parse_arguments(argv)

    data_points = load_poses(args.input, cfg['pose_ground_truth'])

    distance_fns = load_distance_functions(data_points, cfg['distance_functions'])
    if not distance_fns:
        logger.critical('No distance functions were read, failing execution')
        exit(1)

    data_structure = build_data_structure(data_points, distance_fns, cfg['data_structure'])
    logger.info('Data structure created succesfully')

    loop_candidates = query_loop_candidates(data_structure)

    with open(args.output, 'w') as f:
        for item in loop_candidates:
            f.write(f'{item}\n')

    if args.display:
        logger.info('Starting visual confirmation dialogue...')
        display_candidates(loop_candidates)

        # TODO: write confirmed candidates

if __name__ == '__main__':
    grotloc(sys.argv)
