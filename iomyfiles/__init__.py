# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:51:58 2019

@author: tinivella
"""

import scipy.io as sio
import numpy as np
import pandas as pd
import time
import sys
import os
#from .importmyfiles import WaveformsMatFilePC41, ExcelRequirements105
from .helpers_plot import plot_kpi_comparison

print(f'Invoking __init__.py for {__name__}')

class ExcelRequirements105():
    """[summary]
    
    Arguments:
        object {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """

    # TODO: change static methods to used this dict to be have better code
    # self.operating_points = {
    #         sheet_name: 'OperatingPoints',
    #         use_columns: ['OPN', 'Vi (V)', 'Vo (V)', 'Po (W)'],
    #         name_translation_excel2py: {  'OPN': 'OPN',
    #                                     'Vi (V)': 'Vin',
    #                                     'Vo (V)': 'Vout_ref',
    #                                     'Po (W)': 'Pout_ref'}
    #     }
    # self.circuit_cfg = {
    #         sheet_name: 'CircuitConfigs.',
    #         name_translation_excel2py: {'fs (Hz)': 'fs',
    #                                     'Cdclink (F)': 'Cdclink',
    #                                     'Cdm (F)': 'Cdm'}
    #     }

    def __init__(self, requirements_filename=None, dict_op_excel2plecs=None, dict_cfg_excel2plecs=None):
        if requirements_filename is None:
            self.req_filename = r"requirements.xlsx"
            print(f"{req_filename} has been loaded")
        else:
            self.req_filename = requirements_filename

        # load op/cfg to varin
        op_df = self.load_operating_point(
            xls_filename=self.req_filename, dict_op_excel2plecs=dict_op_excel2plecs)
        cfg_df = self.load_circuit_cfg(
            xls_filename=self.req_filename, dict_cfg_excel2plecs=dict_cfg_excel2plecs)
        # load wfm input, read CFN and OPN
        sims_df = self.load_simuation_list(xls_filename=self.req_filename)

        # fill dataframe with all boost_NIBB_coupled_plot_waveform.mat
        sims_df = pd.merge(cfg_df, sims_df, on='CFN')
        sims_df = pd.merge(op_df, sims_df, on='OPN')

        self.operating_points = op_df
        self.circuit_configuration = cfg_df
        self.simulation_list = sims_df

    @staticmethod
    def load_operating_point(xls_filename: str, dict_op_excel2plecs: dict):
        if dict_op_excel2plecs is None:
            dict_op_excel2plecs = {
                'OPN': 'OPN', 'Vi (V)': 'Vin', 'Vo (V)': 'Vout_ref', 'Po (W)': 'Pout_ref'}
        usecols = list(dict_op_excel2plecs.keys())
        df_op = pd.read_excel(
            io=xls_filename, sheet_name='OperatingPoints', skiprows=0, usecols=usecols)
        df_op = df_op.rename(index=str, columns=dict_op_excel2plecs)
        df_op = df_op.set_index('OPN')
        return df_op

    @staticmethod
    def load_circuit_cfg(xls_filename: str, dict_cfg_excel2plecs: dict):
        if dict_cfg_excel2plecs is None:
            dict_cfg_excel2plecs = {
                'fs (Hz)': 'fs', 'Cdclink (F)': 'Cdclink', 'Cdm (F)': 'Cdm'}
        usecols = list(dict_cfg_excel2plecs.keys())
        df_cfg = pd.read_excel(
            io=xls_filename, sheet_name='CircuitConfigs.', skiprows=0)
        df_cfg = df_cfg.rename(index=str, columns=dict_cfg_excel2plecs)
        df_cfg = df_cfg.set_index('CFN')
        return df_cfg

    @staticmethod
    def load_simuation_list(xls_filename):
        usecols = ['OPN', 'CFN']
        # wfm=wfm.set_index(['CFN', 'OPN'], drop=False)
        return pd.read_excel(io=xls_filename, sheet_name='Simulations', header=1, usecols=usecols)


class WaveformsMatFilePC41(object):
    def __init__(self, mat_filename: str):
        self.simulations_list = self.load_mat_file(mat_filename)

    @staticmethod
    def load_mat_file(mat_filename: str):
        # result = mat4py.loadmat(filename = "./TPFC_waveforms.mat") this fails!!!
        # TODO: check if there is a better way to implement with dataframes

        simulations_list = []
        mat_recarray = sio.loadmat(file_name=mat_filename)
        var_names = mat_recarray['waveforms'].dtype.names
        _, simulations_number = mat_recarray['waveforms'].shape
        for sim_index in range(simulations_number):
            simulation = {}
            for var_name in var_names:
                simulation[var_name] = mat_recarray['waveforms'][var_name][0][sim_index]
            simulations_list.append(simulation)
        return simulations_list, mat_recarray
        # mat = sio.loadmat(file_name = mat_filename)  # load mat-file
        # mdata = mat['waveforms']  # variable in mat file
        # mdtype = mdata.dtype  # dtypes of structures are "unsized objects"
        # ndata = {n: mdata[n][0, 0] for n in mdtype.names}
        # columns = [n for n, v in ndata.items()]
        # return ndata, columns

    @staticmethod
    def save_mat_file(mat_filename, mat_recarray: np.recarray = None, list_of_dict: list = None):
        # simulations_list is a list of dicts
        # TODO: from list of dict to matfile
        if mat_recarray is not None:
            sio.savemat(file_name=mat_filename, mdict=mat_recarray)
            return 0
        elif list_of_dict is not None:
            names = list(list_of_dict[0].keys())
            formats = ['O']*len(names)
            dtype = dict(names=names, formats=formats)

            matfile_template = {'__globals__': [],
                                '__header__': 'MATLAB 5.0 MAT-file, written by iomyfile',
                                '__version__': '1.0',
                                'waveforms': np.ndarray(shape=(1, len(list_of_dict)), dtype=dtype)}

            # for row in range(len(list_of_dict)):
            #     row_array = np.array(list(list_of_dict[row].items()))
            #     waveforms[row] = row_array
            for row in range(len(list_of_dict)):
                # struct = np.rec.array(tuple(list_of_dict[row]), dtype=dtype)
                for k, v in list_of_dict[row].items():
                    matfile_template['waveforms'][0][row][k] = v
            sio.savemat(file_name= mat_filename, mdict = matfile_template)
            return 0
