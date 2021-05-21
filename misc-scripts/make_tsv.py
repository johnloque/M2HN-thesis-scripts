import os
import re
import spacy
import csv

#fonction d'écriture au format .tsv de l'annotation d'un texte

def make_tsv(rpath, wpath):
    reading_file = open(rpath).read()

    nlp = spacy.load("fr_core_news_sm")
    nlp.max_length = 2500000
    doc = nlp(reading_file, disable = ['ner', 'parser'])

    writing_file = open(wpath, 'w')

    tsv_writer = csv.writer(writing_file, delimiter='\t')
    tsv_writer.writerow(['form', 'lemma', 'POS'])

    for token in doc :
        tsv_writer.writerow([token.text, token.lemma_, token.pos_])

    writing_file.close()
    reading_file.close()


rdir = '' #dossier parent contenant les textes au format txt
wdir = '' #dossier parent voué à contenir tous les textes au format tsv


#écriture des fichiers annotés
for filename in os.listdir(rdir):
    basename = re.sub('.txt', '', filename)
    make_tsv(rdir + '/' + filename, wdir + '/' + basename + '.tsv')


