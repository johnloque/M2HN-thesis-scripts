import pandas as pd
import os
import re
from matplotlib import pyplot as plt

folder = '' #chemin vers le dossier contenant un csv pour chaque locution figée
fullocc = '' #chemin vers le csv contenant les occurrences du lemme possible
colnames = []
i = 0

#construction du dataframe df contenant le compte des occurrences des locutions figées

for filename in os.listdir(folder):
    colnames.append(re.sub('part-', '', re.sub('.csv', '', filename)))
    if i == 0:
        df = pd.read_table(folder + '/' + filename).sum().to_frame()
        df.columns = colnames
    else :
        df[colnames[i]] = pd.read_table(folder + '/' + filename).sum()
    i += 1

df = df.drop(df.index[0])
index = df.index.values.tolist()
new_index = index[1:]
new_index.append(index[0])
df = df.reindex(new_index)
df = df.rename(index={'F' : 'Total'})
col_list = list(df)
col_list = col_list[0:len(df.columns)]
df['Total'] = df[col_list].sum(axis = 1)

#construction du dataframe df2 contenant le compte des occurrences du lemme possible

df2 = pd.read_table(fullocc).sum().to_frame()
df2 = df2.drop(df2.index[0])
index = df2.index.values.tolist()
new_index = index[1:]
new_index.append(index[0])
df2 = df2.reindex(new_index)
df2 = df2.rename(index={'F' : 'Total'})

#construction du dataframe df3 contenant le pourcentage représenté par les locutions figées

df3 = df
for i in range(len(df3)):
    for j in range(len(df3.columns)):
        df3.iloc[i,j] = df3.iloc[i,j]*100/df2.iloc[i,0]

#réalisation du barplot

df3[df3.columns[0:5]].plot(kind="bar", stacked=True)
plt.legend(loc="upper center", bbox_to_anchor=(1.3, 0.95), ncol=1)
