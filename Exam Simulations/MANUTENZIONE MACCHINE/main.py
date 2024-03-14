
from operator import itemgetter

def main() :

    f_parametri = open('parametri.txt', 'r')

    data_parametro = 0
    parametro_l = []
    parametro_d = 0

    for line in f_parametri :
        parti = line.strip().split(',')
        lettera = parti[1]
        data = parti[0].split('/')
        data = int(data[2] + data[1] + data[0])
        parametro_l.append(lettera)
        parametro_d = data
        data_parametro = parti[0]

    f_man = open('manutenzione.txt', 'r')

    operazioni = []

    for line in f_man :
        parti = line.strip().split(',')
        operazione = parti[0]
        costo = int(parti[2])
        data = parti[1].split('/')
        data = int(data[2] + '0' + data[1] + data[0])


        if parametro_l[0] == 'a' and data < parametro_d :
            operazioni.append({'operazione' : operazione, 'data' : parti[1], 'costo' : costo})
        elif parametro_l[0] == 'p' and data > parametro_d :
            operazioni.append({'operazione' : operazione, 'data' : parti[1], 'costo' : costo})


    if parametro_l[0] == 'a' :
        print(f'Le operazioni effettuate prima del {data_parametro} sono:')
        print()
        for i in operazioni :
            print(f"{i['operazione']} in data {i['data']} costo {i['costo']} euro")
    elif parametro_l[0] == 'p' :
        print(f'Le operazioni effettuate dopo del {data_parametro} sono:')
        print()
        for i in operazioni :
            print(f"{i['operazione']} in data {i['data']} costo {i['costo']} euro")

    costosa = sorted(operazioni, key=itemgetter('costo'), reverse=True)

    print()
    print(f'La manutenzione più costosa è stata {operazioni[0]["operazione"]} del {operazioni[0]["data"]} costata {operazioni[0]["costo"]} euro')

main()
