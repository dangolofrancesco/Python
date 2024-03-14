# QUESTO PROGRAMMA CODIFICA E DECODIFICA CON ALFABETO MORSE

def main() :
    morse = 'morse.txt'
    comandi = 'comandi.txt'

    cod_morse = codice_morse(morse)
    alf = alfabeto(morse)

    codifica(comandi, cod_morse, alf)

def codice_morse(morse) :

    # Creare dizionario con alfabeto morse
    # Aperura file morse
    morse = open(morse, 'r')

    cod_morse = {}
    # Carico dizionario con alfabeto morse
    for line in morse:
        parti = line.strip().split()
        lettera = parti[0]
        codice = parti[1]
        cod_morse[lettera] = codice

    morse.close()
    return cod_morse

def alfabeto(morse) :

    morse = open(morse, 'r')

    alfabeto = {}
    # Carico dizionario con alfabeto
    for line in morse :
        parti = line.strip().split()
        lettera = parti[0]
        codice = parti[1]
        alfabeto[codice] = lettera

    morse.close()
    return alfabeto

def codifica(comandi, cod_morse, alf) :

    infile = open(comandi, 'r')


    for line in infile :
        parti = line.strip().split()
        if parti[0] == 'c' :
            testo = open(parti[1], 'r')
            frase = []
            for line in testo :
                frase.append(line.strip('!\n'))   # Biosgna escludere tutti i caratteri non compresi nell'alfabeto morse
            lettere = []
            for parole in frase :
                for ch in parole :
                    lettere.append(ch.upper())

            tradotto = []
            for ch in lettere :
                if ch != ' ':
                    tradotto.append(cod_morse[ch])
            print('Codifica del file testo.txt:')
            for i in tradotto :
                print(i, end=' ')

            print()
            print()

        elif parti[0] == 'd' :
            testo = open(parti[1], 'r')
            frase = []
            for line in testo:
                simboli = line.strip().split()

                for ch in simboli :
                    frase.append(alf[ch])

            print('Decodifica del file codice.txt:')
            for i in frase :
                print(i, end=' ')

            print()

main()
