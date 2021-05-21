import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import lexnet as lx

folder = '' #répertoire parent contenant l'ensemble des fichiers .tsv corrigés

plt.figure(figsize=(30,10))



plt.subplot(1,2,1)

mat = np.zeros((10, len(os.listdir(folder))-1))

for i in range(10):
    for j in range(len(os.listdir(folder))-1):
        try :
            mat[i,j] = lx.full_stat_link(['virtuel ADJ','actuel ADJ'], folder + os.listdir(folder)[j], ['NOU', 'VER','ADJ'], i+1, 'lemma')[2]
        except Exception :
            pass
        
df2 = pd.DataFrame(data = mat, index = [k for k in range(1,11)], columns = os.listdir(folder)[0:len(os.listdir(folder))-1])
df2 = df2.sort_index(axis = 1)
sns.heatmap(df2, cmap = 'RdYlBu_r').set_title('Significativité des coocurrences des adjectifs "virtuel" et "actuel"')



plt.subplot(1,2, 2)

mat = np.zeros((10, len(os.listdir(folder))-1))

for i in range(10):
    for j in range(len(os.listdir(folder))-1):
        try :
            mat[i,j] = lx.full_stat_link(['virtuel ADJ','réel ADJ'], folder + os.listdir(folder)[j], ['NOU', 'VER','ADJ'], i+1, 'lemma')[2]
        except Exception :
            pass
        
df2 = pd.DataFrame(data = mat, index = [k for k in range(1,11)], columns = os.listdir(folder)[0:len(os.listdir(folder))-1])
#df2 = df2.clip(lower = 0)
df2 = df2.sort_index(axis = 1)
sns.heatmap(df2, cmap = 'RdYlBu_r').set_title('Significativité des coocurrences des adjectifs "virtuel" et "réel"')
