##
# Cifrario di Playfair
#

def main():
    key = 'playfair'
    key = key.upper()
    lettere = []

    # DEFINIZIONE LETTERE ALFABETO
    alfabeto = []
    for i in range(65, 91) :
        alfabeto.append(chr(i))

    # DEFINZIONE LETTERE MANCANTI

    for ch in key :
        if ch not in lettere :
            lettere.append(ch)

    for ch in alfabeto :
        if ch not in lettere :
            lettere.append(ch)

    if 'I' in key :
        lettere.remove('J')
    elif 'J' in key :
        lettere.remove('I')

    i = 0
    tabella = []


    while i != 5 :
        row = []
        for n in range(0, 5):
            row.append(lettere[n])
        for j in range(5) :
            lettere.pop(0)

        tabella.append(row)
        i = i + 1

    for row in tabella :
        print(row)

main()
