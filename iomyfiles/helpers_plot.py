# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:59:23 2019

@author: tinivella
"""
# Import used modules
import os
import sys
import time
import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.offline import plot
from plotly.subplots import make_subplots
# import scipy.io  as sio

from plotly.colors import sequential

def plot_kpi_comparison(simulations_df, plot_cols, fig_title, fig_filename):
    config_list = simulations_df['Configuration Name'].unique()
    colors = sequential.RdBu #choose a color list
    showLegend = True
    fig = make_subplots(rows=len(plot_cols), cols=1)
    for count, param in enumerate(plot_cols,start=1):
        for idx_config, config_name in enumerate(config_list): 
            df = simulations_df[simulations_df['Configuration Name'] == config_name]
            
            hover_data = df[['Vi (V)','Vo (V)','Po (W)']].to_numpy()
            
            fig.add_trace(
                            go.Bar(x=df['OPN'], 
                                   y=df[param],
                                   customdata=[hover_data[i] for i in range(len(df['OPN']))],
                                   hovertemplate='Vi = %{customdata[0]} V<br>'+
                                                 'Vo = %{customdata[1]} V<br>'+
                                                 'Po = %{customdata[2]} W',
                                   name=config_name,
                                   marker_color=colors[idx_config],
                                   showlegend=showLegend),
                            row=count, col=1)
            fig.update_xaxes(title_text="OPN", row=count, col=1)
            fig.update_yaxes(title_text=param, row=count, col=1)
            
        showLegend = False
    # Update title and height
    fig.update_layout(title_text=fig_title, height=1500)
#    plot(fig)
    file_address = fig_filename +'.html'
    fig.write_html(file_address, auto_open=True)
    
    return fig