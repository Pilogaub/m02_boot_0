from functools import reduce

def ProductoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor
    return resultado

lista = [1, 3, -1, 15, 9]

sumatorio = reduce(lambda x, y: x + y, lista)
# creo una copia de la lista
l = lista[:]
#añado el neutro para la suma en la posición cero (el neutro de una suma siempre es 0)
l.insert(0, 0)
sumatorioDobles = reduce(lambda x, y: x + y*2, l)

print(sumatorio)
print(sumatorioDobles)
