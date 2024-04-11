import networkx as nx
import pandas as pd
import numpy as np
from src import generate_edge_types
from src import add_aggregate_networks

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

edge_types = generate_edge_types.generate_edge_types()
edge_types = edge_types + ['T_T', 'U_U', 'T_U', 'U_T', 'TM_*', 'TF_*', 'UM_*', 'UF_*', 'T_*', 'U_*']

dataset_list = ['Skripal', 'Navalny', 'Ukraine']

for dataset in dataset_list:
    if dataset != 'Skripal':
        # rename total_te to *_*
        dict1 = {"total_te":"*_*"}
        edge_types = [dict1.get(n,n) for n in edge_types]

    # Data
    if dataset == 'Skripal':
        te_df_path = 'Data/raw/Skripal/Skripal_actor_te_edges_df.csv'
    elif dataset == 'Ukraine':
        te_df_path = 'Data/raw/Ukraine/Ukraine_actor_te_edges_df.csv'
    elif dataset == 'Navalny':
        te_df_path = 'Data/raw/Navalny/Navalny_actor_te_edges_df.csv'

    # Networks
    graph_dict = {}
    edge_types2 = ['actors'] + edge_types

    out_infl_weights_df = pd.DataFrame(columns = edge_types2)

    # Pre-process
    graph_df = pd.read_csv(te_df_path)
    actors = pd.unique(graph_df[['Source', 'Target']].values.ravel('K'))
    out_infl_weights_df['actors'] = actors

    # Check number of unique users
    num_us = len(pd.unique(graph_df[['Source', 'Target']].values.ravel('K')))
    print(f'number of unique users: {num_us}')

    graph_df = add_aggregate_networks.add_aggr_nets(graph_df)

    for edge_type in edge_types:
        graph_dict[edge_type] = {}
            
        g = nx.from_pandas_edgelist(graph_df, source='Source', target='Target', edge_attr=[edge_type], create_using=nx.DiGraph())

        graph_dict[edge_type] = g

        # identify which influence types nodes appear in, save summed weights
        for node in actors:

            ## out weight df filling
            if g.has_node(node):
                out_edges = g.out_edges(node, data=True)
                summed_weight = 0
                for edge_data in out_edges:
                    #convert 'dict_items' dtype to float
                    for k, v in edge_data[2].items():
                        w = float(v)
                    summed_weight += w
                row_index = out_infl_weights_df.index[out_infl_weights_df['actors']==node].to_list()
                out_infl_weights_df.loc[row_index, [edge_type]]=summed_weight

    out_infl_weights_df.to_csv(f'Data/preprocessed/{dataset}/{dataset}_out_infl_weights_df.csv')

