#ajout des balises pb

rfile = '' #chemin vers le fichier à enrichir
wfile = '' #chemin vers le fichier enrichi

reading_file = open(rfile, 'r')
i = 155 #première page à numéroter
offset = 10 #décalage entre le numéro de la page et l'identifiant de l'image sur Gallica
facs_pref = 'http://gallica.bnf.fr/ark:/12148/bpt6k205311/f' #préfixe de l'url de l'oeuvre sur Gallica
facs_suff = '.highres'
new_content = ""
        
for line in reading_file:
    match = re.search(r'<pb/>', line)
    if match :
        repline = re.sub(r'<pb/>', '<pb n="' + str(i) + '" facs="' + facs_pref + str(i+offset) + facs_suff + '"/>', line)
        i += 1
    else :
        repline = line
    new_content += repline

writing_file = open(wfile, 'w')
writing_file.write(new_content)
writing_file.close()
