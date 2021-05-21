import lexnet as lx
import networkx

file = '' #chemin vers le fichier tsv du paragraphe à visualiser

keylist = ['possible ADJ', 'possible NOU', 'virtuel ADJ', 'virtuel NOU']
poslist = ['NOU','ADJ','VER']

#réalisation du graphe
G = lx.lexnet(keylist, file, poslist, 3, 'red_dev', 'lemma', 'all', 'tsne')

#calcul de centralité
networkx.algorithms.centrality.degree_centrality(G)
