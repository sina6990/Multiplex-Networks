import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

######################################################
### creating plots for the same sources (4 Layers) ###
######################################################

def plot_user_heatmap_outdegree_4layers(inf, df, name, dic, results_dir, map_color):
    '''
    inf:            source influence type
    df:             dataframe, ex// TM_out_aggr_wdf, or
                    "Trustworthy-Mainstream out edge aggregated weight dataframe"
    results_dir:    string of results dir
    return_plot:    boolean indicating whether to return the plot or not (default: False)
    '''
    aggr_type = str(inf + '_*')
    df = df.drop(['actors'], axis=1)
    print(df.head())
    print(df.columns)

    # Data
    heatmap = np.empty((5, len(df[aggr_type])))
    for i, (column_name, column_data) in enumerate(df.items()):
        heatmap[i] = column_data

    # renaming the first label in y-axis
    df = df.rename(columns={f'{inf}_TM':f'{inf} → TM', f'{inf}_UM':f'{inf} → UM',f'{inf}_TF':f'{inf} → TF',
                            f'{inf}_UF':f'{inf} → UF', aggr_type:f'{inf} → * *'})
    cbar_column = f'{inf}_(TM,UM,TF,UF)'

    # Plotting
    fig = plt.figure(figsize=(30,25))
    ax = fig.add_subplot(111)
    im = ax.imshow(heatmap, interpolation='nearest', vmin= 0, vmax=20, cmap=f'{map_color}')
    ax.set_yticks(range(5))
    labels = df.columns
    ax.set_yticklabels(labels, rotation = 0, fontsize = 58)
    ax.set_xticklabels(ax.get_xticklabels(), fontsize = 60)
    ax.set_xlabel('Sorted actors according to the strength of influence', fontsize = 55)
    ax.set_title(f'{dic[name]} {inf} source actors influence', fontsize = 60)
    cbar = fig.colorbar(ax=ax, mappable=im, orientation = 'horizontal')
    cbar.ax.tick_params(labelsize=60)
    cbar.set_label('Transfer Entropy', fontsize = 60)
    ax.set_aspect('auto')
    plt.savefig(f'{results_dir}/{name}_{inf}_out_activity.png')
    return fig


#############################################################
### creating plots for heatmaps of pairwise co-occurrence ###
#############################################################

def plot_layer_heatmap_4layers(df, name, dic, results_dir):
    new_indecies = ['TM → *', 'TF → *', 'UM → *', 'UF → *']
    df.set_index([new_indecies], inplace=True)
    new_columns = {'TM_*':'TM → *', 'TF_*':'TF → *', 'UM_*':'UM → *', 'UF_*':'UF → *'}
    df.rename(columns = new_columns, inplace=True)
    ax = sns.heatmap(df, linewidth=0.5, vmin=0, vmax=1, annot=True, fmt='.2f', annot_kws={'size': 14})
    ax.set_title(f'Pairwise Link Presense between Influence Types in {dic[name]} Dataset', fontsize = 8)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0, fontsize = 14)
    ax.set_yticklabels(ax.get_yticklabels(), rotation=90, fontsize = 14)
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=14)
    plt.savefig(f'{results_dir}/{name}_layer_correlation_heatmap_4layers.png')