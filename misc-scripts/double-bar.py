import pandas as pd
from matplotlib import pyplot as plt

path = '' #chemin absolu vers le fichier .csv contenant les occurrences des bigrammes impliquant le possible ou le virtuel pour exprimer l'idée d'immobilité (données issues de TXM)

df = pd.read_table(path)
df['keyword'] = df['word'].str.contains('virtuel')
df = df.groupby('keyword').sum()
df = df.T
new_index = df.index.values.tolist()
new_index = new_index[1:]
new_index.append('F')
df = df.reindex(new_index)
df = df.rename(index={'F' : 'Total'})
df.columns = ['arrêt/immobilité possible', 'arrêt/station virtuel(le)']
df.plot(kind="bar")
