import re
import pandas as pd
import os

#le vrai bon (il faut avoir un paragraphe par ligne)

book = input('Identifiant du texte : ')

reading_file = open('/home/michel/Documents/bergson/tei2/'+ book + '.xml', 'r')
writing_file = open('/home/michel/Documents/bergson/tei2/' + book + '_w.xml', 'w')

path = '/home/michel/Documents/bergson/txtsplit/full_tsv_corr/split/' + book

#contenu à écrire (document complet)
new_content = ''

i = 1

for line in reading_file :
    #contenu à écrire (paragraphe)
    new_line = ''
    
    try :
        df = pd.read_table(path + '/p' + str(i) + '.tsv')
    except Exception :
        pass
    
    #si c'est un paragraphe
    
    if re.search(r'<p n=\"' + str(i) + '\">', line) :
        #début de paragraphe : ouverture de la balise p
        new_line += '<p n="' + str(i) + '">\n'
        
        #récupérer le contenu de la balise
        text = re.search(r'">(.*)</p>', line)
        repline = text.group(1)
        
        j = 0
        
        #tant que le paragraphe n'est pas fini
        while len(repline) > 0 and j < len(df):
            #si on rencontre une nouvelle page
            if re.match(r'<pb.*?/>', repline) :
                pb = re.search(r'(<pb.*?/>)', repline)
                #on copie la balise pb
                new_line += pb.group(1) + '\n'
                #et on la supprime du contenu restant du paragraphe à traiter
                repline = re.sub(pb.group(1), '', repline, count=1)
            #si on rencontre un token
            else :
                #un signe de ponctuation
                if re.match(r'[",\'\?!\(\):;\.\s-]', df.iloc[j, 0]) :
                    #on copie le signe dans une balise pc
                    new_line += '<pc>' + df.iloc[j,0] + '</pc>\n'
                    try :
                        #et on le supprime du contenu restant du paragraphe à traiter
                        repline = re.sub(df.iloc[j, 0], '', repline, count = 1)
                    except Exception :
                        pass
                #ou un mot
                else :
                    #on copie le mot et ses attributs dans une balise w
                    new_line += '<w lemma="' + str(df.iloc[j, 1]) + '" pos="' + str(df.iloc[j,2]) + '">' + str(df.iloc[j,0]) + '</w>\n'
                    try :
                        #et on le supprime du contenu restant du paragraphe à traiter
                        repline = re.sub(df.iloc[j, 0], '', repline, count = 1)
                    except Exception :
                        pass
                j += 1
                #suppression des espaces qui polluent
                repline = re.sub(r'\s*', '', repline, count = 1)
        
        #fin de paragraphe : fermeture de la balise p
        new_line += '</p>\n'
        i += 1
        
    #si c'est une ligne normale  
    else :
        #on la recopie telle quelle
        new_line += line
    
    #on ajoute la ligne au contenu du document à écrire
    new_content += new_line

writing_file.write(new_content)
writing_file.close()
reading_file.close()
