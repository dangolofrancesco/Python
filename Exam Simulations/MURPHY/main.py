# Lettura di massime

def main() :
    #Apro file delle massime
    infile = open('leggi_di_Murphy.txt', 'r', encoding='UTF-8')
    massime = []

    titolo = infile.readline().rstrip()
    while titolo != '' :
        enunciato = ''
        line = infile.readline().rstrip()
        while line != '' :
            enunciato += line + ' '
            line = infile.readline().rstrip()

        massima = {'titolo' : titolo, 'enunciato' : enunciato}
        massime.append(massima)

        titolo = infile.readline().rstrip()

    infile.close()

    for massima in massime :
        print(massima)


main()