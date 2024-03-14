##
# Questo programma visualizza l'elenco degli esami superati da uno studente
#

# def main() :
#
#     id = '11234'
#     classes = open('classes.txt', 'r')
#
#     print('Student ID', id)
#
#     for classe in classes :
#         course = classe.rstrip()
#         infile = open(course + '.txt', 'r')
#
#         for line in infile :
#             parts = line.split()
#             if id == parts[0] :
#                 print(course + ' ' + line, end='')
#
#         infile.close()
#
#     classes.close()
#
# main()

def main() :

    id = input('Inserisci la matricola: ')
    studenti = {'Student ID': 0,}
    classes = open('classes.txt', 'r')
    print('Student ID', id)

    for classe in classes :
        course = classe.rstrip()
        studenti[course] = 0
        infile = open(course + '.txt', 'r')
        for line in infile :
            parts = line.split()
            studenti['Student ID'] = parts[0]
            studenti[course] = parts[1].rstrip()
            if studenti['Student ID'] == id :
                print(course + ' ' + studenti[course])


main()
























    # for line in classes :
    #     studente[line.rstrip()] = 0
    #
    # input = '11234'
    #
    # for line in csc1 :
    #     studente['STUDENT ID'] = line.rstrip().split(' ')[0]
    #     studente['CSC1'] = line.rstrip().split(' ')[1]
    #     print(studente)
    #
    # # for line in csc2 :
    # #     studente['CSC1'] = line.rstrip().split(' ')[1]
    # #     print(studente)
    #
    #     if input in studente.values() :
    #         studente1 = studente
    #         for i in studente1 :
    #             print(i, studente[i])

        #print(studente)








    #print(studente)




