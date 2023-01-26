import Gomba
def harmadik():
    lista = []
    def beolvas():
        fajl = open("gep.txt", "r", encoding="utf8")
        fajl.readline()
        sorok = fajl.readlines()
        fajl.close()
        index = 0
        while index < len(sorok):
            lista.append = sorok[index]
            index += 1
    beolvas()
