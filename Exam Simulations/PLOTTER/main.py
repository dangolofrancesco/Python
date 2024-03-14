
# Questo programma simula il plotter

def main() :
    filename = 'plotter.txt'

    # CREAZIONE TABELLA
    ROW = 5
    COL = 5
    tabella = []
    for i in range(ROW) :
        row = []
        for j in range(COL) :
            row.append('.')
        tabella.append(row)

    numerazione = {'5' : 0, '4' : 1, '3' : 2, '2' : 3, '1' : 4, '0' : 5}

    infile = open(filename, 'r')

    for line in infile :
        parti = line.strip().split()
        print()
        segno = parti[0]
        x = numerazione[parti[1]]
        y = int(parti[2])
        #l = int(parti[3])
        # if segno == 'P' :
        #     print(x, y)
        #     tabella[x][y] = '*'

    x = 3
    y = 2

    tabella[2][4] = 'p'

    #STAMPA TABELLA
    for row in range(5):
        for col in range(5):
            print("%3s" % tabella[row][col], end=' ')
        print()







main()

