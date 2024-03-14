##
# Questo programma elenca i redditi annui pro capite delle nazioni

def main() :
    pro = redditi('rawdata_2004.txt')
    print(pro)


    start = input('Vuoi iniziare (Y/N)? ').upper()
    if start == 'N' :
        exit('Arrivederci')
    elif start == 'Y' :
        play = True
        while play:
            right = True
            while right:
                nazione = input('Nome della nazione: ').upper()
                if nazione.isdigit():
                    print('Errore, inserire solo lettere')
                elif nazione not in pro:
                    print('Errore, la nazione inserita non è valida')
                elif nazione in pro:
                    right = False
                    print(nazione, pro[nazione])
            continuo = input('Vuoi continuare (Y/QUIT)? ').upper()
            if continuo == 'Y' :
                play = True
            elif continuo == 'QUIT' :
                play = False
                print('Arrivederci')
            else :
                print('Errore, valore non valido')
    else:
        print('Valore non valido')


def redditi(filename) :
    # Creo dizionario vuoto
    redditi = {}

    # Apro file in lettura
    infile = open(filename, 'r')

    for line in infile :
        line = line.upper()
        fields = line.split()
        redditi[fields[1]] = fields[3]

    return redditi



main()