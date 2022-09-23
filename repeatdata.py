def contiene(array,number,repeat):
    data = dict((i, lista.count(i)) for i in lista)
    return bool(data[number]>=repeat)



lista = [4,5,2,4,5,9,9,4,4]
print(contiene(lista,4,5))
print(contiene(lista,4,4))
print(contiene(lista,4,3))
print(contiene(lista,9,2))
 