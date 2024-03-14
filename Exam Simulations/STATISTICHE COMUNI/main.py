# Questo programma effetua delle statistiche sui comuni delle regioni italiane

from operator import itemgetter

def main() :
    file_reg = 'regioni.txt'
    file_com = 'elenco-comuni-italiani.csv'

    # Apro file regioni
    try:
        infile = open(file_reg, 'r')
    except OSError:
        print('Errore, file non trovato')
        return 0

    # Lista regioni da considerare
    regioni = []

    # Carico lista con i dati del file regioni
    for line in infile :
        regione = line.strip()
        regioni.append(regione)

    infile.close()

    # Apro file comuni
    try :
        infile = open(file_com, 'r')
    except :
        print('Errore, file non trovato')
        return 0

    # Creazione dizionario per caricamento comuni
    comuni = {}

    # Carico comuni
    for line in  infile :
        parti = line.strip().split(';')
        regione = parti[10]
        comune = parti[6]
        if regione in regioni and regione not in comuni :
            comuni[regione] = [comune]
        elif regione in regioni and regione in comuni :
            comuni[regione].append(comune)

    infile.close()

    calcolo(comuni)

def calcolo(comuni) :

    comuni = dict(comuni)

    comuni_reg = {}
    stampa = {}
    for i in comuni.keys() :
        num = len(comuni[i])
        stampa[i] = {'regione' : i, 'num comuni' : num}


        comuni_lung = {}
        for c in comuni[i] :
            comuni_lung[c] = len(c)


        comuni_lung = sorted(comuni_lung.items(), key=itemgetter(1))
        comuni_reg[i] = {'minimo' : comuni_lung[0][0], 'massimo' : comuni_lung[len(comuni_lung) - 1][0] }

        print(f'*** REGIONE {i} ***')
        print(f'Nella regione {i} ci sono {stampa[i]["num comuni"]} comuni')
        print(f'Il nome più breve è {comuni_reg[i]["minimo"]} e quello più lungo è {comuni_reg[i]["massimo"]}')
        print()
        
main()