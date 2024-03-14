# Questo programma simula una partita a indovina chi

def main() :
    file_personaggi = 'personaggi.txt'
    file_domande = 'domande1.txt'

    # Apertura file 1
    try :
        infile = open(file_personaggi, 'r', encoding='UTF-8')
    except OSError :
        print('Errore, file non trovato')
        return 0

    # Carico file personaggi
    proprieta = infile.readline().strip().split(';')

    personaggi = {}
    for line in infile :
        parti = line.strip().split(';')
        personaggio = {}
        for i in range(len(proprieta)):
            personaggio[proprieta[i]] = parti[i]
        personaggi[parti[0]] = personaggio



    partita(personaggi, file_domande)

def partita(personaggi, file_domande) :

    infile = open(file_domande, 'r', encoding='UTF-8')

    personaggi_in_gioco = dict(personaggi)

    #for line in personaggi_in_gioco.items() :
    #    print(line)

    lista = []
    for line in infile :
        parti = line.strip().split('=')
        proprieta = str(parti[0])
        valore = parti[1]
        for p in personaggi_in_gioco.keys() :
            #print(p)
            if personaggi_in_gioco[p][proprieta] == valore :
                lista.append(personaggi_in_gioco[p])

    for i in lista :
        print(i)











main()