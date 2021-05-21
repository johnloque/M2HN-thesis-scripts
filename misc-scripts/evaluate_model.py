import pandas as pd
import os
import re
import numpy as np
import itertools

orig = '' #dossier parent contenant tous les fichiers tsv avec annotation brute
corr = '' #dossier parent contenant tous les fichiers tsv avec annotation corrigée

#fonction affichant sous forme de dataframe les score de précision, rappel et f-mesure pour un lemme et une pos donnés
def evaluate_as_df(directories, lemma, pos):

    table = np.empty((len(os.listdir(directories[1]))+1,2))
    table[:] = np.nan
    main = []
    corr = []
    main_counter = 0

    for i in range(len(os.listdir(directories[0]))):
        sub = []
        df1 = pd.read_table(directories[0] + '/' + os.listdir(directories[0])[i])
        df2 = pd.read_table(directories[1] + '/' + os.listdir(directories[0])[i])
        df1 = df1[(df1['form'].str.match(lemma)) & (df1['POS'] == pos)]
        df2 = df2[(df2['form'].str.match(lemma)) & (df2['POS'] == pos)]

        if df1.index.values.tolist():
            for item in df1.index.values.tolist():
                main_counter += 1
                if item in df2.index.values.tolist():
                    sub.append(item)
            table[i,0] = len(sub)/len(df1.index.values.tolist())
            if df2.index.values.tolist():
                table[i,1] = len(sub)/len(df2.index.values.tolist())
            main.append(sub)
            corr.append(df2.index.values.tolist())
            
        elif df2.index.values.tolist():
            table[i,1] = str(len(sub)/len(df2.index.values.tolist()))
        
    main_unlist = list(itertools.chain.from_iterable(main))    
    corr_unlist = list(itertools.chain.from_iterable(corr))
    
    table[len(os.listdir(directories[0])),0] = len(main_unlist)/main_counter
    table[len(os.listdir(directories[0])),1] = len(main_unlist)/len(corr_unlist)
    
    rownames = os.listdir(directories[0])
    rownames.append('Total')
    
    df = pd.DataFrame(table, index = rownames, columns = ['Précision', 'Rappel'])
    df['F-mesure'] = 2 * df['Précision'] * df['Rappel'] / (df['Précision'] + df['Rappel'])
    
    l = df.index.tolist()
    l = sorted(l)
    df = df.reindex(l)
    
    return df


#exemple
evaluate_as_df([orig, corr], 'possible','NOUN')
evaluate_as_df([orig, corr], 'possible','ADJ')
