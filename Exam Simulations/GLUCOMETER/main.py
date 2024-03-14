# Questo programma segnala il suoperamento dei 200 mg/dL del livello di glicemia di una lista di pazienti

from operator import itemgetter

def main():
    FILENAME = 'glucometers.txt'

    # Apertura il file
    try:
        infile = open(FILENAME, 'r', encoding='UTF-8')
    except OSError:
        print('File non trovato')
        return 0

    SOGLIA = 200
    # Ordinamento dati del file in dizionario

    pazienti = {}
    for line in infile :
        parti = line.strip().split()
        codice = parti[0]
        orario = parti[1]
        livello = int(parti[2])

        if livello >= SOGLIA :
            if codice not in pazienti :
                pazienti[codice] = {'codice' : codice, 'n_sup' : 1, 'valore' : [orario + ' ' + str(livello)]}
            else :
                pazienti[codice]['n_sup'] += 1
                pazienti[codice]['valore'].append(orario + ' ' + str(livello))

    lista = sorted(pazienti.values(), key=itemgetter('n_sup'), reverse=True)

    for paziente in lista :
        for value in paziente['valore'] :
            print(paziente['codice'], value)
        print()

main()
