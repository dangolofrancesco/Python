# QUESTO PROGRAMMA GESTISCE LE ALTEZZE DELLE PIRAMIDI

def main() :

    filename = 'mappa.txt'

    infile = open(filename, 'r')

    griglia = []

    for line in infile :
        row = []
        parti = line.strip().split()
        for c in parti :
            c = int(c)
            row.append(c)

        griglia.append(row)

    # RICERCA CIME

    cime = []
    for row in range(len(griglia)) :
        for col in range(len(griglia[row])) :
            r = griglia[row][col]
            if row != 0 and row != (len(griglia) - 1) and col != 0 and col != (len(griglia[row]) - 1) :
                if r > griglia[row - 1][col] and r > griglia[row + 1][col] and r > griglia[row][col - 1] and r > griglia[row][col + 1] :
                    cime.append({'cima' : r, 'pos' : [row, col]})
            elif row == 0 and col != 0 and col != (len(griglia[row]) - 1) :
                if r > griglia[row + 1][col] and r > griglia[row][col - 1] and r > griglia[row][col + 1]:
                    cime.append({'cima': r, 'pos': [row, col]})
            elif row == (len(griglia) - 1) and col != 0 and col != (len(griglia[row]) - 1) :
                 if r > griglia[row - 1][col] and r > griglia[row][col - 1] and r > griglia[row][col + 1]:
                     cime.append({'cima': r, 'pos': [row, col]})

    altezza = []
    for cima in cime :
        altezza.append(cima['cima'])
        print(cima['cima'], cima['pos'][0], cima['pos'][1] )

    altezza_media = sum(altezza) / len(altezza)

    print('Altezza media:', altezza_media)
main()