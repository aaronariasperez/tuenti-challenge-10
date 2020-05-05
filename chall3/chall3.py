import re

file = open('galdos.txt', 'r')
texto = str(file.readlines())

words = re.findall('[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]{3,}',texto,flags=0)

contador = {}
for w in words:
    low = w.lower()
    if low in contador:
        contador[low] = contador[low] + 1
    else:
        contador[low] = 1

sorted_words = list(zip(contador.values(), contador.keys()))
sorted_words.sort(key=lambda x: x[1])
sorted_words.sort(key=lambda x: x[0], reverse=True)

file = open('submitInput', 'r')
cases = file.readline()
resto = file.readlines()


def buscar_palabra(lista, palabra):
    i = 0
    for l in lista:
        if l[1] == palabra:
            return i, l[0]
        i += 1

resultado = ''
casenumber = 1
for r in resto:
    resultado += 'Case #'+str(casenumber)+': '
    casenumber += 1
    input = r.split()[0]
    if input.isdigit():
        indice = int(input)
        palabra = sorted_words[indice-1][1]
        apariciones = sorted_words[indice-1][0]
        resultado += palabra+" "+str(apariciones)+"\n"
    else:
        ranking, apariciones = buscar_palabra(sorted_words,input)
        resultado += str(apariciones)+" #"+str(ranking+1)+"\n"

print(resultado)

file = open('chall3.out', 'w')
file.write(resultado)
