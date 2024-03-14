##
# Questo programma simula il gioco DINOSAURI

from random import shuffle

def main() :
    filename = 'mazzo.txt'
    infile = open(filename, 'r', encoding='utf-8')

    user1 = []
    user2 = []
    mazzo = []

    for line in infile:
        mazzo.append(line.rstrip())

    FULL = len(mazzo) // 2

    shuffle(mazzo)


    i = 0
    j = 1
    while len(user1) != FULL:
        user1.append(mazzo[i])
        i = i + 2
        user2.append(mazzo[j])
        j = j + 2

    infile.close()

    gioco(user1, user2, FULL)

def gioco(user1, user2, LIMITE) :
    valori = {'Rosso': 5, 'Verde': 3, 'Giallo': 1}
    punti = {'Punti 1': 0, 'Punti 2': 0}

    print('Punteggio giocatore 1:', punti['Punti 1'])
    print('Punteggio giocatore 2:', punti['Punti 2'])

    print()

    carte_comuni = []
    i = 1
    while i <= LIMITE :
        print('Mano n.', i)

        carta1 = user1[0]
        print('Carta giocatore 1:', carta1)
        user1.remove(carta1)
        carta2 = user2[0]
        print('Carta giocatore 2:', carta2)
        user2.remove(carta2)
        carte_comuni.append(carta1)
        carte_comuni.append(carta2)

        giocatore1 = []
        giocatore2 = []

        if valori[carta1] > valori[carta2] :
            print('Risultato: Vince la mano il giocatore 1')
            for carte in carte_comuni :
                giocatore1.append(valori[carte])
            somma = sum(giocatore1)
            punti['Punti 1'] = somma
        elif valori[carta1] < valori[carta2] :
            print('Risultato: Vince la mano il giocatore 2')
            for carte in carte_comuni:
                giocatore2.append(valori[carte])
            somma = sum(giocatore2)
            punti['Punti 2'] = somma
        elif valori[carta1] == valori[carta2] :
            print('Risultato: Pareggio ')

        print('Punteggio giocatore 1:', punti['Punti 1'])
        print('Punteggio giocatore 2:', punti['Punti 2'])

        i = i + 1

    print()

    if punti['Punti 1'] > punti['Punti 2'] :
        print(f"Vince il giocatore 1 con {punti['Punti 1']} punti")
    else :
        print(f"Vince il giocatore 2 con {punti['Punti 2']} punti")

main()