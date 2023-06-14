def media(lista):
    sum_lista = sum(lista)
    long = len(lista)
    print(sum_lista/long)

def mediana(lista):
    list2 = sorted(lista)
    long = len(lista)
    if(long % 2 == 0):
        redondo = (list2[int(long/2)] + list2[int(long/2)-1])/2
        print(redondo)
    else:
        redondo = list2[int((long-1)/2)]
        print(redondo)