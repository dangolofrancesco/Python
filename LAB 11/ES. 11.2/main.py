##
# Operazioni sugli insiemi
#

def main() :
    user1 = input('Enter a name: ').upper()
    user2 = input('Enter a name: ').upper()

    set1 = set()
    set2 = set()

    for ch in user1 :
        set1.add(ch)
    set1.discard(' ')

    for ch in user2 :
        set2.add(ch)
    set2.discard(' ')

    in_both(set1, set2)

    differenza(set1, set2)

    alfabeto = set()
    for i in range(65, 91) :
        alfabeto.add(chr(i))

    lettere(user1, user2, alfabeto)


def in_both(set1, set2) :
    output = set1.intersection(set2)
    print(output)

def differenza(set1, set2) :
    output = set1.difference(set2)
    print(output)

def lettere(user1, user2, alfabeto) :
    lista1 = []
    for ch in user1:
        lista1.append(ch)

    set1 = set()
    for i in lista1 :
        if i.isalpha() :
            set1.add(i)

    lista2 = []
    for ch in user2:
        lista2.append(ch)

    set2 = set()
    for i in lista2:
        if i.isalpha():
            set2.add(i)

    unione = set1.union(set2)

    ch_mancanti = alfabeto.difference(unione)

    print(ch_mancanti)

main()