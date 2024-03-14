# Questo programma presenta delle ricette

def main() :
    file_cibi = 'cibi.txt'
    file_ricetta = 'fusilli_alle_olive.txt'

    # Apertura file ricetta

    ricetta = open(file_ricetta, 'r')

    ingredienti = {}


    for line in ricetta :
        parti = line.strip().split(';')
        if len(parti) > 1 :
            cibo = parti[0]
            grammi = float(parti[1])

            ingredienti[cibo] = [grammi]

    ricetta.close()

    # Apertura file cibi

    cibi = open(file_cibi, 'r')

    prezzo = []
    calorie_tot = []
    for line in cibi :
        parti = line.strip().split(';')
        if len(parti) > 1 :
            cibo = parti[0]
            costo = float(parti[1])
            calorie = float(parti[2])

            if cibo in ingredienti.keys() :
                divisore = 1000 / ingredienti[cibo][0]
                costo = round((costo / divisore), 3)
                calorie = round((calorie / divisore), 3)
                prezzo.append(costo)
                calorie_tot.append(calorie)



    prezzo = sum(prezzo)
    calorie_tot = sum(calorie_tot)

    print('Ingredienti:')
    for i in ingredienti.items() :
        print(f'{i[0]} - {i[1][0]}')

    print()
    print(f'Numero di ingredienti: {len(ingredienti.keys())}')
    print(f'Costo ricetta: {prezzo}')
    print(f'Calorie ricetta: {calorie_tot}')

main()

