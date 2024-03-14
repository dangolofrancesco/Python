# Questo programma ordina i dati di una casa discografica

from operator import itemgetter

def main() :
   #Apro il file principale
    infile = open('artisti.txt', 'r', encoding='UTF-8')

    canzoni = []

    for line in infile :
        line = line.rstrip().split(';')
        codice = line[0]
        artista = open(line[1], 'r', encoding='UTF-8')
        for song in artista :
            song = song.strip().split(';')
            canzoni.append({'canzone' : song[1], 'data' : int(song[0]), 'codice' : codice})
        artista.close()

    canzoni.sort(key=itemgetter('data'))

    infile.close()

    stampa(canzoni)

def stampa(canzoni) :
    data = []

    for i in canzoni :
        if i['data'] not in data:
            print(i['data'], ':')
            data.append(i['data'])
        print(f'{i["canzone"]:<30} {i["codice"]}')

main()