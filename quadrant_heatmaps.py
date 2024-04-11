import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from src import plot_heatmap

dataset_list = ['Skripal', 'Navalny', 'Ukraine']
dict_list = {'Skripal': 'Skripal', 'Navalny': 'Navalny', 'Ukraine': 'Ukraine'}
for dataset in dataset_list:
    df_path_4 = f'Data/preprocessed/{dataset}/{dataset}_quadrant_preprocessing_sources_4layers.csv'
    df_heatmap_source = pd.read_csv(df_path_4, index_col=0)
    plot_heatmap.plot_layer_heatmap_4layers(df_heatmap_source, dataset, dict_list, f'plots/{dataset}')
    plt.clf()