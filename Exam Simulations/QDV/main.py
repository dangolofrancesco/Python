# Questo programma segnala gli le province con l'indicatore selezionato
from operator import itemgetter

def main() :

    filename = '20201214_QDV2020_001.csv'
    file_indicatore = 'indicatore.txt'

    indicatori(filename)
    print()
    province(filename, file_indicatore)

def indicatori(filename) :

    # Apertura file 1

    try :
        infile = open(filename, 'r')
    except OSError :
        print('Errore, file non trovato')
        return 0

    # Creazione lista indicatori
    indicatori = []

    # Caricamento lista indicatoriv
    intestazione = infile.readline()

    for line in infile:
        parti = line.strip().split(',')
        indicatore = parti[5]

        if indicatore not in indicatori:
            indicatori.append(indicatore)

    i = 1
    for ind in indicatori :
        print(f'{i}. {ind}')
        i += 1

def province(filename, file_ind) :

    # Apertura file indicatore
    try :
        prov = open(filename, 'r')
        ind = open(file_ind, 'r')
    except OSError :
        print('Errore, file non trovato')
        return 0

    intestazione = prov.readline()

    indicatore = []
    for line in ind :
        indicatore.append(line.strip())


    prov_val = {}
    for line in prov :
        parti = line.strip().split(',')
        ind = parti[5]
        valore = float(parti[4])
        prov = parti[0]
        if ind == indicatore[0] :
            prov_val[prov] = valore


    prov_val = sorted(prov_val.items(), key=itemgetter(1), reverse=True)

    print(f"Classifica secondo l'indicatore {indicatore[0]}")
    for i in prov_val:
        print(f'{i[0]:<30} {i[1]}')



main()