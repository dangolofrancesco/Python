
from operator import itemgetter
def main() :

    file_obsolete = 'obsoleto.txt'
    file_testo = 'testo.txt'

    try:
        f_obsoleto = open('obsoleto.txt', 'r', encoding='UTF-8')
    except OSError :
        print('Errore, file non trovato')
        return 0

    obsolete = {}

    for line in f_obsoleto :
        parti = line.strip().split()
        obsolete[parti[0]] = parti[1]

    f_obsoleto.close()

    lettura_testo(file_testo, obsolete)

def lettura_testo(filename, obsolete):
    """
    Questa funzione legge il file testo ed elabora il numero di parole, sostituisce le parole obsolete con
    quelle moderne e conta il numero di parole obsolete
    :param filename: nome del testo
    :param obsolete: dizionario parole obsolete
    :return:
    """

    try:
        infile = open(filename, 'r', encoding='UTF-8')
        outfile = open('nuovotesto.txt', 'w', encoding='UTF-8')
    except OSError:
        print('Errore, file non trovato')
        return 0

    ricorrenze = {}
    righe = []
    n = 0
    for line in infile:
        parole = line.strip().split()
        frase = ''
        for p in parole :
            n += 1
            if p in obsolete.keys() :
                if p not in ricorrenze:
                    ricorrenze[p] = 1
                else:
                    ricorrenze[p] += 1
                p = obsolete[p]
                frase += p + ' '
            else:
                frase += p + ' '
        righe.append(frase)




    for line in righe:
        outfile.write(f'{line} \n')

    ricorrenze = sorted(ricorrenze.items(), key=itemgetter(1), reverse=True)


    print('Il numero di parole presenti nel testo è:', n)
    print('Le parole obsolete sono così riportate nel testo originale:')
    for i in ricorrenze:
        print(i[0] + ':', i[1])

main()