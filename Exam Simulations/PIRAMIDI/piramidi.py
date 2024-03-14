def main() :
    try:
        infile = open('mappa.txt', 'r')
    except OSError :
        print('Errore, file non trovato')
        return 0

    tabella = mappa(infile)
    infile.close()
    visual = ricerca(tabella)

    altezza_media = []
    for element in visual:
        print(element['valore'], element['coordinate'][0], element['coordinate'][1])
        altezza_media.append(element['valore'])
    print('Altezza media:', sum(altezza_media) / len(altezza_media))

def mappa(file) :
    raggio = 1
    mappa = []
    for line in file:
        row = []
        line = line.strip().split()
        for element in line :
            row.append(int(element))
        mappa.append(row)

    for volte in range(raggio):
        mappa.insert(0, [0 for i in range(len(mappa[0]))])
        mappa.append([0 for i in range(len(mappa[0]))])
        for line in mappa :
            line.insert(0, 0)
            line.append(0)

    return mappa

def ricerca(mappa) :
    raggio = 1
    visual = []
    matrice = []
    for x in range(raggio, len(mappa) - raggio) :
        for y in range(raggio, len(mappa) - raggio):
            for raggiox in range(-raggio, raggio + 1):
                for raggioy in range(-raggio, raggio + 1):
                    matrice.append(mappa[x + raggiox][y + raggioy])
            if mappa[x][y] == max(matrice) and matrice.count(mappa[x][y]) == 1:
                visual.append({'valore': mappa[x][y], 'coordinate': [x - raggio, y - raggio]})
            matrice.clear()
    return visual

main()