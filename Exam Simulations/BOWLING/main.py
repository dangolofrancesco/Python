##
# Questo programma registra i risultati di una partita di bowling
#

def main() :
    filename = 'bowling.txt'

    punti = punteggi(filename)
    somma_punti = somma(punti)
    sorted_print(somma_punti, punti)

def punteggi(filename) :
    infile = open(filename, 'r', encoding='utf-8')
    punti_tot = []

    for line in infile :
        punti = []
        parts = line.rstrip().split(';')
        for i in parts :
            punti.append(i)
        punti_tot.append(punti)

    infile.close()

    return punti_tot

def somma(punti) :
    somma_punti = {}
    for player in punti :
        somma = []
        lenght = len(player)
        for i in range(2, lenght) :
            player[i] = int(player[i])
            somma.append(player[i])
        somma = sum(somma)
        chiave = player[0] + ' ' + player[1]

        somma_punti[chiave] = somma

    return somma_punti

def sorted_print(somma_punti, punti) :

    print('I punteggi finali sono: ')
    sorted_dict = sorted(somma_punti.values(), reverse= True)
    for value in sorted_dict :
        print(list(somma_punti.keys())[list(somma_punti.values()).index(value)], value)

    for player in punti :
        i = 0
        j = 0
        for el in player :
            if el == 10 :
                i = i + 1
            elif el == 0 :
                j = j + 1
        print(f'{player[0]} {player[1]} ha abbattuto tutti i birilli {i} volta/e e ha mancato tutti i birilli {j} volta/e')

main()
