import pandas as pd
import os

path = '' #dossier parent contenant un dossier par texte (chacun contenant lui-même un fichier .tsv par paragraphe) : /full_tsv_corr/split

pos_adj_count = 0
pos_noun_count = 0

for file in sorted(os.listdir(path))[0:8]:
    pref = path + '/' + file
    for i in range(1,len(os.listdir(pref))+1):
        df = pd.read_table(pref + '/p' + str(i) + '.tsv')
        for j in range(len(df)):
            if (df.iloc[j,1] == 'virtuel') & (df.iloc[j,2] == "ADJ"):
                for k in range(len(df)):
                    if (df.iloc[k, 1] == "possible"):
                        for l in range(len(df)):
                            if (df.iloc[l,1]=="possible") & (df.iloc[l,2] == "ADJ"):
                                pos_adj_count += 1
                            elif (df.iloc[l,1]=="possible") & (df.iloc[l,2] == "NOUN"):
                                pos_noun_count += 1
                        break
                break

pos_adj_count/(pos_adj_count+pos_noun_count)
