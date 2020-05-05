file = open('submitInput', 'r')
cases = file.readline()
resto = file.readlines()

resultado = ''
casenumber = 1
for r in resto:
    resultado += 'Case #'+str(casenumber)+": "
    casenumber += 1
    entrada = int(r.split()[0])

    divisiones = int(entrada // 20)
    resto = entrada % 20
    if 9*divisiones < resto:
        best = 0
    else:
        best = divisiones

    if best == 0:
        resultado += 'IMPOSSIBLE\n'
    else:
        cadena = str(best)
        resultado += cadena+'\n'

print(resultado)
file = open('chall5.out','w')
file.write(resultado)