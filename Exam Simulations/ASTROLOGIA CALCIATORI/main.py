##
# Programma per verificare se l'astrologia abbia degli effetti sulle prestazioni dei giocatori di Calcio
#

from csv import reader

def main() :
    filename1 = 'sportivi.csv'
    filename2 = 'zodiaco.csv'

    calciatori = sportivi(filename1)
    segni = zodiaco(filename2)

    print(calciatori)
    print(segni)

    segni_calc = correlazione(calciatori, segni)

    print(segni_calc)

    somma(filename1, filename2, segni_calc)

def sportivi(filename) :
    infile = open(filename)
    calciatori = {}
    csv_reader = reader(infile)


    for row in csv_reader :
        data = row[3].split('/')
        data = data[1] + data[0]

        calciatori[row[0]] = data

    infile.close()

    return calciatori

def zodiaco(filename) :
    infile = open(filename)
    segni = {}
    csv_reader = reader(infile)

    for row in csv_reader :
        date = []
        data1 = row[1].split('/')
        data1 = data1[1] + data1[0]

        data2 = row[2].split('/')
        data2 = data2[1] + data2[0]

        date.append(data1)
        date.append(data2)

        segni[row[0]] = date

    infile.close()

    return segni

def correlazione(calciatori, segni) :
    segni_calc = {}

    for (key,value) in segni.items() :
        segno = key
        value1 = int(value[0])
        value2 = int(value[1])
        for (key, value) in calciatori.items() :
            calciatore = key
            if int(value) in range(value1, value2) :
                segni_calc[calciatore] = segno


    return segni_calc

def somma(filename1, filename2, segni_calc) :
    gol = {}
    infile = open(filename1)
    csv_reader = reader(infile)

    for row in csv_reader :
        reti = int(row[1])

        gol[row[0]] = reti

    infile.close()

    segni = []
    infile = open(filename2)
    infile = reader(infile)

    for row in infile :
        segni.append(row[0])


main()