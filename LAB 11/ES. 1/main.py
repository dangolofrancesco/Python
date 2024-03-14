##
# Questo prgramma conta le occorrenze di ciascuna parola in un file di testo
#

def main():
    # Chiamo e apro il file
    file_name = 'input.txt'
    infile = open(file_name, 'r')

    # Definisco dizionario per il conteggio
    parole = {}

    # Inserisco parole al dizionario con le rispettive occorrenze
    for line in infile :
        words = line.split()
        for word in words :
            word = word.rstrip('.,!\'')
            cleaned = clean(word)
            if cleaned != '' and cleaned not in parole:
                parole[cleaned] = 1
            elif cleaned in parole:
                parole[cleaned] = parole[cleaned] + 1
    print(parole)

    infile.close()

    m = max(parole.values())
    print(m)
    most_common = []

    while m > 0 :
        for word in parole :
            if parole[word] == m :
                print(parole)
                #most_common.append(parola)
        m = m - 1



    print(most_common)


def clean(string):
    """
    Ripulisce una stringa rendendo tutti i caratteri minuscoli
    ed eliminando quelli che non sono lettere.
    :param string: stringa da ripulire
    :return: stringa ripulita
    """

    result = ''
    for char in string :
        if char.isalpha :
            result = result + char.lower()
    return result


main()