##
# Cifratura monoalfabetica casuale
#

def main() :
    infile = open('input.txt', 'r', encoding='UTF-8')
    outfile = open('output.txt', 'w', encoding='UTF-8')
    alphabet = []
    alfabeto = {}
    lista_chiave = []
    lettere_mancanti = []
    chiave = input('Inserisci la chiave: ')
    chiave = chiave.upper()

    for ch in chiave :
        if ch not in lista_chiave :
            lista_chiave.append(ch)

    for i in range(65, 91) :
        alphabet.append(chr(i))
        if chr(i) not in lista_chiave :
            lettere_mancanti.append(chr(i))

    lettere_mancanti.reverse()
    lista_chiave = lista_chiave + lettere_mancanti

    i = 0
    while i < 26:
        alfabeto[alphabet[i]] = lista_chiave[i]
        i = i + 1

    print(alfabeto)

    for line in infile :
        line = line.upper()
        for ch in line :
            if ch in alphabet :
                outfile.write(alfabeto[ch])
            else :
                outfile.write(ch)

main()
