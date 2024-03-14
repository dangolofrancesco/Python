##
# Questo programma riporta l'importo totale relativo a ciascun tipo di servizio di un albergo
#

def main() :
    importi = {}
    try :
        file_name = 'nput.txt'

        infile = open(file_name, 'r')
        value = 0
        for line in infile :
            line = line.split(';')
            importi[line[1].lstrip(' ')] = 0

        infile.close()
    except IOError :
        print('Errore. File non trovato')

    try:

        infile = open(file_name, 'r')

        for line in infile :
            line = line.split(';')
            importi[line[1].lstrip(' ')] += int(line[2])

        print(importi)

        infile.close()
        
    except IOError:
        print('Errore. File non trovato')

main()