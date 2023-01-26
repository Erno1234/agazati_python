def masodik():
    index = 0
    lista = []
    while index < 5:
        kor = int(input("Adjon meg öt egész számot(0-120):"))
        lista.append(kor)
        index += 1

    print("I/A,B,C:")
    index = 0
    print("\t", end="")
    while index < len(lista)-1:
        print(lista[index], end=":")
        index += 1
    print(lista[index])

    def elso_idos(lista):
        idos = 0
        index = 0
        while index < len(lista) and lista[index] < 70:
            if lista[index] > 70:
                idos += lista[index]
            index += 1

        return idos
    def konzolra_ir(idos):
        print("I/D,E:")
        print("\t Első idős ember korának helye:{}".format(idos))

    idos = elso_idos(lista)
    konzolra_ir(idos)
