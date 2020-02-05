# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:59:23 2019

@author: tinivella
"""

import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.offline import plot
from plotly.subplots import make_subplots
from plotly.colors import sequential

import macpath


# import sys
# sys.path.append('../')

from importmyfiles import plot_kpi_comparison, WaveformsMatFilePC41, ExcelRequirements105

def test_plot_kpi_comparison():

    import plotly.express as px

    sims_excel_list = [r"../data/requirements_foo_dcm.xlsx"]
    sims_df = pd.DataFrame()
    sims_df = pd.read_excel(io=sims_excel_list[0], sheet_name='Simulations', header=1)
    sims_df.dropna(axis=1, how='all')
    Po_max=65e3
    sims_60kW_df = sims_df[sims_df['Po (W)'] <= Po_max]
    columns_to_plot = ['iin_rpl', 'io_rpl',
                       'DMin_energy', 'DMin_h1',
                       'DMout_energy', 'DMout_h1',
                       'CMin_energy', 'CMin_h1',
                       'Pcond_inv', 'Psw_inv',
                       'flux_mot',]
    config_list = sims_60kW_df['Configuration Name'].unique()
    worst_case_df = pd.DataFrame()
    for config_name in config_list:
        df = sims_60kW_df[sims_60kW_df['Configuration Name'] == config_name]
        df_max = df.max(axis=0)
        worst_case_df= worst_case_df.append(df_max, ignore_index=True)

    fig_worstcase = plot_kpi_comparison(simulations_df = worst_case_df,
                        plot_cols = columns_to_plot,
                        fig_title = "Topology KPIs for worstcase",
                        fig_filename = "KPI_worstcase")

    fig_all_sims = plot_kpi_comparison(simulations_df = sims_60kW_df,
                        plot_cols = columns_to_plot,
                        fig_title="Topology KPIs for different OPN",
                        fig_filename = "KPI_OPN")

def test_WaveformsMatFilePC41():
    pc41_wfm = WaveformsMatFilePC41(mat_filename = r"../data//TPFC_waveforms.mat")
    simulations_list, mat_recarray = WaveformsMatFilePC41.load_mat_file(mat_filename = r"../data//TPFC_waveforms.mat")
    # WaveformsMatFilePC41.save_mat_file(mat_filename= r"../data//TPFC_waveforms_exp.mat", mat_recarray = mat_recarray)
    WaveformsMatFilePC41.save_mat_file(mat_filename = r"../data//TPFC_waveforms_list.mat", list_of_dict = simulations_list)

def test_ExcelRequirements105():
    req_105 = ExcelRequirements105(requirements_filename= r"../data//requirements_foo_dcm.xlsx")

if __name__ == '__main__':

    test_plot_kpi_comparison()
    test_WaveformsMatFilePC41()
    test_ExcelRequirements105()
