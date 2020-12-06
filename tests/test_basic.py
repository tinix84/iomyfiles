# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:59:23 2019

@author: tinivella
"""

<<<<<<< HEAD
from pathlib import Path
=======
>>>>>>> 19c2a4f48d42fb6fce457871005a17470af3d0f8
import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.offline import plot
from plotly.subplots import make_subplots
from plotly.colors import sequential

<<<<<<< HEAD
import sys, os
import unittest

abs_dirname = os.path.dirname(os.path.abspath(__file__))

try:
    from .context import iomyfiles
    from iomyfiles.helpers_plot import plot_kpi_comparison
    from iomyfiles import WaveformsMatFilePC41, ExcelRequirements105
except:
    print(sys.exc_info())
=======
import macpath


# import sys
# sys.path.append('../')

from importmyfiles import plot_kpi_comparison, WaveformsMatFilePC41, ExcelRequirements105
>>>>>>> 19c2a4f48d42fb6fce457871005a17470af3d0f8

def test_plot_kpi_comparison():

    import plotly.express as px

<<<<<<< HEAD
    sims_excel_list=[abs_dirname+r"/data/requirements_foo_dcm.xlsx"]
    # sims_df = pd.DataFrame()
=======
    sims_excel_list = [r"../data/requirements_foo_dcm.xlsx"]
    sims_df = pd.DataFrame()
>>>>>>> 19c2a4f48d42fb6fce457871005a17470af3d0f8
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
<<<<<<< HEAD
    read_mat_filename = abs_dirname + r"/data/TPFC_waveforms.mat"
    write_mat_filename = abs_dirname + r"/data/TPFC_waveforms_list.mat"

    #test read1
    pc41_wfm = WaveformsMatFilePC41(mat_filename=read_mat_filename)
    # test read2
    simulations_list, mat_recarray = WaveformsMatFilePC41.load_mat_file(
        mat_filename=read_mat_filename)
    #test write
    WaveformsMatFilePC41.save_mat_file(
        mat_filename=write_mat_filename, list_of_dict=simulations_list)

def test_ExcelRequirements105():
    req_105 = ExcelRequirements105(requirements_filename=(abs_dirname +  r"/data/requirements_foo_dcm.xlsx"))


class MyTest(unittest.TestCase):
    def test1(self):
        test_plot_kpi_comparison()

    def test2(self):
        test_WaveformsMatFilePC41()

    def test3(self):
        test_ExcelRequirements105()

if __name__ == '__main__':
    lib_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..'))
    sys.path.append(lib_path)

    # commenting out the following shows the `modules` directory in the path
    # print(sys.path)

    # from .context import formats
    from iomyfiles.helpers_plot import plot_kpi_comparison
    from iomyfiles import WaveformsMatFilePC41, ExcelRequirements105

=======
    pc41_wfm = WaveformsMatFilePC41(mat_filename = r"../data//TPFC_waveforms.mat")
    simulations_list, mat_recarray = WaveformsMatFilePC41.load_mat_file(mat_filename = r"../data//TPFC_waveforms.mat")
    # WaveformsMatFilePC41.save_mat_file(mat_filename= r"../data//TPFC_waveforms_exp.mat", mat_recarray = mat_recarray)
    WaveformsMatFilePC41.save_mat_file(mat_filename = r"../data//TPFC_waveforms_list.mat", list_of_dict = simulations_list)

def test_ExcelRequirements105():
    req_105 = ExcelRequirements105(requirements_filename= r"../data//requirements_foo_dcm.xlsx")

if __name__ == '__main__':
>>>>>>> 19c2a4f48d42fb6fce457871005a17470af3d0f8

    test_plot_kpi_comparison()
    test_WaveformsMatFilePC41()
    test_ExcelRequirements105()
