
def main():
    filename = 'noleggio.txt'

    try:
        infile = open(filename, 'r')
    except OSError:
        print('Errore file non trovato')
        return 0

    auto = caricamento(infile)
    selezione = scelta(auto)
def caricamento(infile):
    auto = []
    intestazione = infile.readline().strip().split(',')

    for line in infile:
        parts = line.strip().split(',')
        dizionario = {}
        i = 0
        for el in intestazione:
            dizionario[el] = parts[i]
            i += 1
        auto.append(dizionario)

    for line in auto:
        print(line)
    return auto

def scelta(auto_lista) :
    input1 = input("Scegli categoria e giorni: ").lower()
    lista_input = input1.split()


    disp = []

    for car in auto_lista:
        if car['Categoria'] == lista_input[0] :
            dizionario = {'marca' : car['Marca'], 'modello': car['Modello'], 'colore': car['Colore'], 'giorni' : []}
            for el in lista_input[1::] :
                if car[el] == 'L' :
                    dizionario['giorni'].append(el)
            disp.append(dizionario)

    for auto in disp:
        if len(auto['giorni']) < len(lista_input) - 1:
            disp.remove(auto)

    if len(disp) == 0 :
        print('Auto non disponibile')
    else:
        print('Le macchine disponibili sono:')
        i = 1
        for auto in disp:
            print(f'{i}) {auto["marca"]} {auto["modello"]} colore {auto["colore"]}')
            i += 1

    try:
        input2 = int(input("Quale vuoi prenotare?: "))
    except ValueError:
        print('Errore, inserire un numero')
        return 0

    auto_scelta = disp[input2 - 1]
    print(f'Auto scelta: {auto_scelta["marca"]} {auto_scelta["modello"]} colore {auto_scelta["colore"]}')


    for auto in auto_lista:
        if auto['Marca'] == auto_scelta['marca'] and auto['Modello'] == auto_scelta['modello']:
            for giorni in lista_input[1::] :
                auto[giorni] = 'A'

    print()
    for auto in auto_lista :
        print(auto)

main()

