import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/home/michel/Documents/bergson/data/copres-pos-lemma.csv')
df = df.set_index('Livre')
df.columns = ['virtuel ADJ, possible ADJ', 'virtuel ADJ, possible NOM', 'virtuel NOM, possible ADJ','virtuel NOM, possible NOM']

#diagramme en barres cumulées
df.plot(kind="bar", stacked=True)

#diagramme circulaire
df2 = df.sum(axis=0)
plt.figure(figsize=(5,5))
df2.to_frame()[0].plot.pie(autopct='%1.0f%%')
