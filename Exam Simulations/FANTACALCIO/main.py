# QUESTO PROGRAMMA SIMULA IL FANTACALCIO

from operator import itemgetter

def main() :
    # Creo dizionari per ogni ruolo
    portieri = []
    difensori = []
    centrocampisti = []
    attaccanti = []

    # Apro il file
    try:
        filename = 'fantacalcio.txt'
        infile = open(filename, 'r', encoding='utf-8')

        # Itero sul file per ordinare i giocatori
        for line in infile :
            field = line.strip().split(', ')
            if field[2] == 'portiere' :
                portieri.append({'nome': field[0], 'valore': int(field[3])})
            elif field[2] == 'difensore' :
                difensori.append({'nome': field[0], 'valore': int(field[3])})
            elif field[2] == 'centrocampista' :
                centrocampisti.append({'nome': field[0], 'valore': int(field[3])})
            elif field[2] == 'attaccante' :
                attaccanti.append({'nome': field[0], 'valore': int(field[3])})

        infile.close()

    except IOError :
        print('Errore apertura file')

    #ordino dizionari
    portieri.sort(key= itemgetter('valore'), reverse=True)
    difensori.sort(key=itemgetter('valore'), reverse=True)
    centrocampisti.sort(key=itemgetter('valore'), reverse=True)
    attaccanti.sort(key=itemgetter('valore'), reverse=True)

    print(portieri)

    crea_squadra(portieri, difensori, centrocampisti, attaccanti)

def crea_squadra(portieri, difensori, centrocampisti, attaccanti) :
    squadra = []

    soldi_portieri = 20
    i = 1
    n_por = 3
    while i <= n_por :
        for por in portieri :
            if por['valore'] <= soldi_portieri and (soldi_portieri - por['valore']) == (n_por - i) :
                squadra.append({'Portieri' : [por['nome'], por['valore']]})
                soldi_portieri = soldi_portieri - por['valore']
                portieri.remove(por)
        i = i + 1

    soldi_difensori = 40 + soldi_portieri
    i = 1
    n_dif = 8

    while i <= n_dif :
        for dif in difensori :
            if dif['valore'] <= soldi_difensori and (soldi_difensori - dif['valore']) == (n_dif - i) :
                squadra.append({'Difensori': [dif['nome'], dif['valore']]})
                soldi_difensori = soldi_difensori - dif['valore']
                difensori.remove(dif)

        i = i + 1

    for plr in squadra :
        print(plr)

main()
