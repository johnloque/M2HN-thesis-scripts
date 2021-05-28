import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import lexnet as lx

path = '' #dossier parent contenant un fichier .tsv par texte : /full_tsv_corr


graph_dic = {} #un graphe par texte
for file in sorted(os.listdir(path))[0:8]: #exécution chronophage
    graph_dic[file] = lx.lexnet(['possible ADJ', 'virtuel ADJ'], path+'/'+file, ['NOU','VER','ADJ'], 3, 'red_dev', 'lemma','not all', 'tsne')


intersection = {} #un tuple par texte
for file in sorted(os.listdir(path))[0:8]:
    intersection[file] = lx.intersection(['possible ADJ','virtuel ADJ'], graph_dic[file], 1)


#diagramme en barres
array = np.zeros((8,2))
inter_df = pd.DataFrame(array, index=graph_dic.keys(), columns = ['ratio','weighted_ratio'])
for file in intersection.keys():
    inter_df.loc[file, 'ratio'] = intersection[file][1]
    inter_df.loc[file, 'weighted_ratio'] = intersection[file][2]
plt.figure(figsize=(5,5))
inter_df.plot.bar()
plt.legend(loc="upper left", bbox_to_anchor=(1.05, 0.9), ncol=1)
