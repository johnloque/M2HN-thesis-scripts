import pandas as pd
import os


#partion des livres en paragraphes dans des fichiers csv

def tsv_p_split(file):
    rfolder = '' #dossier contenant les fichiers .tsv corrigés complets (data/full_tsv_corr)
    wfolder = '' #dossier destiné à contenir les fichiers .tsv corrigés par paragraphes (data/full_tsv_corr_split)    

    main_df = pd.read_table(rfolder + file + '.tsv')
    
    counter = 1
    n = 1

    for i in range(1,len(main_df)) :
        if main_df.form[i].endswith('\n'):
            sub_df = main_df.iloc[counter:i]
            sub_df.to_csv(wfolder + file + '/p' + str(n) + '.csv', sep='\t', index= False)
            counter = i
            n += 1


#conversion de ces fichiers en tsv (modification de l'extension)

def csv_to_tsv(folder):
    basepath = '' #dossier destiné à contenir les fichiers .tsv corrigés par paragraphes (data/full_tsv_corr_split)
    for filename in os.listdir(basepath + folder):
        os.rename(basepath + folder + '/' + filename, re.sub('.csv', '.tsv', basepath + folder + '/' + filename))


#application de ces deux fonctions à chacun des textes du corpus

flist = ['1888_EDIC','1896_MM','1900_R','1907_EC','1919_ES','1922_DS','1932_2S','1934_PM']

for f in flist:
    tsv_p_split(f)
    csv_to_tsv(f)
