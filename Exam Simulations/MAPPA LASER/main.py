def main() :

    infile = open('mappa.txt', 'r')

    mappa = []
    tabella = []

    for line in infile :
        parti = line.strip().split()
        row = []
        for i in parti :
            row.append(int(i))
        mappa.append(row)

    for x in range(len(mappa)) :
        row = []
        for y in range(len(mappa)) :
            row.append('-')
        tabella.append(row)

    raggio = len(mappa)
    valore = 2

    if valore > 0:

        for volte in range(0, valore):
            mappa.insert(0, [0 for i in range(raggio)])
            mappa.append([0 for i in range(raggio)])

    for volte in range(0, valore) :
        for riga in mappa:
            riga.insert(0,0)
            riga.append(0)

    calcolo(mappa, tabella)

def calcolo(mappa, tabella) :

    D = 3
    matrice = []
    for x in range(D - 1, len(mappa) - D + 1) :
        for y in range(D - 1, len(mappa) - D + 1) :
            punto = mappa[x][y]
            for raggiox in range(- D + 1, D) :
                for raggioy in range(- D + 1, D):
                    punto1 = mappa[x + raggiox][y + raggioy]
                    matrice.append(mappa[x + raggiox][y + raggioy])
            if mappa[x][y] == max(matrice) and matrice.count(mappa[x][y]) == 1 :
                tabella[x - D + 1][y - D + 1] = punto
                matrice.clear()
            else:
                matrice.clear()

    for i in tabella:
        for j in i:
            print(f'{j:<3}', end=' ')
        print()

main()