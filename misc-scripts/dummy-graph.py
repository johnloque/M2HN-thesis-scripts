import spacy
import csv

reading_file = "toute conscience est anticipation de l'avenir. Considérez la direction de votre esprit à n'importe quel moment : vous trouverez qu'il s'occupe de ce qui est, mais en vue surtout de ce qui va être. L'attention est une attente, et il n'y a pas de conscience sans une certaine attention à la vie. L'avenir est là ; il nous appelle, ou plutôt il nous tire à lui : cette traction ininterrompue, qui nous fait avancer sur la route du temps, est cause aussi que nous agissons continuellement. Toute action est un empiétement sur l'avenir."

wpath = "" #chemin vers le fichier où l'on souhaite enregistrer l'annotation tsv de la citation

nlp = spacy.load("fr_core_news_sm")
nlp.max_length = 2500000
doc = nlp(reading_file, disable = ['ner', 'parser'])

writing_file = open(wpath, 'w')

tsv_writer = csv.writer(writing_file, delimiter='\t')
tsv_writer.writerow(['form', 'lemma', 'POS'])

for token in doc :
    tsv_writer.writerow([token.text, token.lemma_, token.pos_])

writing_file.close()

keylist = ['conscience NOU','avenir NOU', 'action NOU']
poslist = ['NOU','ADJ','VER']

#réalisation du graphe
lx.lexnet(keylist, wpath, poslist, 1, 'red_dev', 'lemma', 'all', 'default')

