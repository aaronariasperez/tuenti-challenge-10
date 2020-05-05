import re

file = open('submitInput', 'r')
cases = file.readline()
resto = file.readlines()

alfabeto1 = "abcdefghijklmnopqrstuvwxyz"
alfabeto2 = "axje.uidchtnmbrl'poygk,qf;"

casenumber = 1
resultado = ''
for r in resto:
    resultado += 'Case #'+str(casenumber)+': '
    casenumber += 1

    linea = r

    linea = re.findall('[^ñ]*', linea, flags=0)
    linea = linea[0]

    traducido = ''
    for c in linea:
        if c == ' ':
            traducido += ' '
        elif c == 'v':
            traducido += '.'
        elif c == 'w':
            traducido += ','
        elif c == '-':
            traducido += '\''
        elif c == 'z':
            traducido += '/'
        elif c == 's':
            traducido += ';'
        elif c == '':
            dummy = 0
        elif c == '\n':
            dummy = 0
        elif c in 'axje.uidchtnmbrl\'poygk,qf;v ':
            ind = alfabeto2.index(c)
            trad = alfabeto1[ind]
            traducido += trad
        else:
            traducido += c
    resultado += traducido+'\n'

print(resultado)

file = open('chall7.out','w')
file.write(resultado)