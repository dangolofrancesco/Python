infile = open("mappa.txt", "r")
matrice = []
for r in range(15):
    riga = infile.readline()
    matrice.append(riga.split())

infile.close()

for i in range(15) :
    for j in range(15) :
        print(matrice[i][j], end=' ')
    print()
D = 2

coordinatex_vette = []
coordinatey_vette = []

for r in range(15):
    for c in range(15):
        casella_bassa = False
        for i in range(-D, D+1):
            if casella_bassa:
                break
            if r + i >= 0:
                for j in range(-D, D+1):
                    if c + j >= 0:
                        try:
                            if int(matrice[r][c]) <= int(matrice[r+i][c+j]):
                                if r + i != r or c + j != c:
                                    casella_bassa = True
                                    break
                        except IndexError:
                            casella_bassa = False
        if not casella_bassa:
            coordinatex_vette.append(r)
            coordinatey_vette.append(c)

matrice_vette = []
for r in range(15):
    riga1 = ["-"] * 15
    matrice_vette.append(riga1)

for k in range(len(coordinatex_vette)):
    matrice_vette[coordinatex_vette[k]][coordinatey_vette[k]] = matrice[coordinatex_vette[k]][coordinatey_vette[k]]

for i in range(15):
    for j in range(15):
        print("%4s" % str(matrice_vette[i][j]), end="")
    print()
