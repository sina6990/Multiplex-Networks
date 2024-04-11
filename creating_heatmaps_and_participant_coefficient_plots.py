import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src import generate_edge_types
from src import plot_heatmap
from src import plot_participant_coef
from src import participation_coef as part_coef

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

edge_types = ['TM_*', 'TF_*', 'UM_*', 'UF_*', 'T_*', 'U_*']

accumulated_UM_4layer_df = pd.DataFrame()
accumulated_TM_4layer_df = pd.DataFrame()
accumulated_UF_4layer_df = pd.DataFrame()
accumulated_TF_4layer_df = pd.DataFrame()
accumulated_T_2layer_df = pd.DataFrame()
accumulated_U_2layer_df = pd.DataFrame()

for dataset in generate_edge_types.dataset_list:
    results_dir_4TUMF = f'plots/{dataset}'

    ############
    ### Data ###
    ############
    out_infl_wdf = pd.read_csv(f'Data/preprocessed/{dataset}/{dataset}_out_infl_weights_df.csv')

    ###################################################
    ######## Heatmaps for each influence type #########
    ###################################################

    ######## UM #########
    ### 4 Layers (TUMF) ###
    UM_out_aggr_wdf = out_infl_wdf[['actors', 'UM_*', 'UM_TM', 'UM_TF', 'UM_UM', 'UM_UF']]
    UM_out_aggr_wdf = UM_out_aggr_wdf.loc[UM_out_aggr_wdf['UM_*'] !=0]
    UM_out_aggr_wdf = UM_out_aggr_wdf.sort_values(by=['UM_*'], ascending=False).dropna()
    plot_heatmap.plot_user_heatmap_outdegree_4layers('UM', UM_out_aggr_wdf, dataset, generate_edge_types.dict_list, results_dir_4TUMF, 'BrBG')
    
    ######## TM #########
    ### 4 Layers (TUMF) ###
    TM_out_aggr_wdf = out_infl_wdf[['actors', 'TM_*', 'TM_TM', 'TM_TF', 'TM_UM', 'TM_UF']]
    TM_out_aggr_wdf = TM_out_aggr_wdf.loc[TM_out_aggr_wdf['TM_*'] !=0]
    TM_out_aggr_wdf = TM_out_aggr_wdf.sort_values(by=['TM_*'], ascending=False).dropna()
    plot_heatmap.plot_user_heatmap_outdegree_4layers('TM', TM_out_aggr_wdf, dataset, generate_edge_types.dict_list, results_dir_4TUMF, 'RdBu')

    ######## UF #########
    ### 4 Layers (TUMF) ###
    UF_out_aggr_wdf = out_infl_wdf[['actors', 'UF_*', 'UF_TM', 'UF_TF', 'UF_UM', 'UF_UF']]
    UF_out_aggr_wdf = UF_out_aggr_wdf.loc[UF_out_aggr_wdf['UF_*'] !=0]
    UF_out_aggr_wdf = UF_out_aggr_wdf.sort_values(by=['UF_*'], ascending=False).dropna()
    plot_heatmap.plot_user_heatmap_outdegree_4layers('UF', UF_out_aggr_wdf, dataset, generate_edge_types.dict_list, results_dir_4TUMF, 'PuOr')

    ######## TF #########
    ### 4 Layers (TUMF) ###
    TF_out_aggr_wdf = out_infl_wdf[['actors', 'TF_*', 'TF_TM', 'TF_TF', 'TF_UM', 'TF_UF']]
    TF_out_aggr_wdf = TF_out_aggr_wdf.loc[TF_out_aggr_wdf['TF_*'] !=0]
    TF_out_aggr_wdf = TF_out_aggr_wdf.sort_values(by=['TF_*'], ascending=False).dropna()
    plot_heatmap.plot_user_heatmap_outdegree_4layers('TF', TF_out_aggr_wdf, dataset, generate_edge_types.dict_list, results_dir_4TUMF, 'PiYG')

    #################################
    ### participation coefficient ###
    #################################

    ## Creating Plots for Participant Coefficient of Sources ##
    part_coef.part_coef_out_4layers(UM_out_aggr_wdf,'UM', 4)
    part_coef.part_coef_out_4layers(TM_out_aggr_wdf,'TM', 4)
    part_coef.part_coef_out_4layers(UF_out_aggr_wdf,'UF', 4)
    part_coef.part_coef_out_4layers(TF_out_aggr_wdf,'TF', 4)
    plt.clf()
    plot_participant_coef.part_coef_plot_out_4layers('UM', UM_out_aggr_wdf, dataset, generate_edge_types.dict_list, results_dir_4TUMF,'#964B00','#005249')
    plt.clf()
    plot_participant_coef.part_coef_plot_out_4layers('TM', TM_out_aggr_wdf, dataset, generate_edge_types.dict_list, results_dir_4TUMF,'#0000FF','#FF0000')
    plt.clf()
    plot_participant_coef.part_coef_plot_out_4layers('UF', UF_out_aggr_wdf, dataset, generate_edge_types.dict_list, results_dir_4TUMF,'#800080','#DBA830')
    plt.clf()
    plot_participant_coef.part_coef_plot_out_4layers('TF', TF_out_aggr_wdf, dataset, generate_edge_types.dict_list, results_dir_4TUMF,'#DB39d9','#00FF00')
    plt.clf()
