# Questo programma segnala gli acquisti effettuati da rivenditori non ufficiali

def main() :

    FILENAME_1 = 'prodotti.txt'
    FILENAME_2 = 'acquisti.txt'

    try:
        # Aperura primo file 'prodotti.txt'
        infile = open(FILENAME_1, 'r', encoding='UTF-8')
        infile2 = open(FILENAME_2, 'r', encoding='UTF-8')
    except OSError :
        print('Errore, file non trovatI')
        return 0


    prodotti = {}

    for line in infile :
        parts = line.strip().split()
        prodotto = parts[0]
        ufficiali = parts[1]

        prodotti[prodotto] = {'codice' : prodotto, 'ufficiale' : [ufficiali], 'effettivi' : []}

    infile.close()

    for line in infile2 :
        parts = line.strip().split()
        prodotto = parts[0]
        rivenditori = parts[1]

        prodotti[prodotto]['effettivi'].append(rivenditori)

    infile2.close()

    revisione(prodotti)

def revisione(prodotti) :

    print('Elenco transazioni sospette')
    print()
    for prodotto in prodotti :
        codice = prodotti[prodotto]['codice']
        ufficiale = prodotti[prodotto]['ufficiale']
        effetivi = prodotti[prodotto]['effettivi']

        if len(effetivi) > 0 and effetivi != ufficiale :
            print('Codice prodotto:', codice)
            print('Rivenditore ufficiale:', end=' ')
            for i in ufficiale :
                print(i, end=' ')
                print()
            print('Lista rivenditori:', end=' ')
            for i in effetivi :
                print(i, end=' ')
            print()
            print()

main()

