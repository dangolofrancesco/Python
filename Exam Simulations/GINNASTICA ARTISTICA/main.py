# Questo programma esegue la classifica di una gara di ginnastica artistica

from operator import itemgetter

def main() :
    FILENAME = 'punteggi.txt'

    # Creo lista degli atleti
    atleti = []
    try :
        # Apro il file
        infile = open(FILENAME, 'r', encoding='UTF_8')

        # Ordino il file in dizionari
        for line in infile :
            line = line.strip().split()
            punteggi = []
            for i in range(4, 9) :
                punti = float(line[i])
                punti = round(punti, 2)
                punteggi.append(punti)

            punteggi.remove(max(punteggi))
            punteggi.remove(min(punteggi))
            punteggi = sum(punteggi)

            atleta = {'nome' : line[0] + ' ' + line[1], 'sesso' : line[2], 'nazione' : line[3], 'punteggi' : punteggi}
            atleti.append(atleta)

        infile.close()

    except IOError :
        print('File errato')
    # Ordino dizionario atleti
    atleti.sort(key=itemgetter('punteggi'), reverse=True)

    vincitrice(atleti)
    nazioni(atleti)

def vincitrice(atleti) :
    # Cerco l'atleta donna con punteggio più alto


    donne = []
    for atleta in atleti :
        if atleta['sesso'] == 'F' :
            donne.append(atleta)

    vincitrice = donne[0]

    print('Vincitrice femminile: ')
    print(vincitrice['nome'], '- Punteggio totale:', vincitrice['punteggi'])

def nazioni(atleti) :
    nazioni = {}

    for atleta in atleti :
        if atleta['nazione'] not in nazioni :
            nazioni[atleta['nazione']] = atleta['punteggi']
        else :
            nazioni[atleta['nazione']] += atleta['punteggi']

    nazioni = sorted(nazioni.items(), key=itemgetter(1), reverse=True)


    print()
    i = 1
    for (naz, punti) in nazioni [:3] :
        print(f'{i}°) Classificato: {naz} - Punteggio totale: {punti}')
        i += 1

main()