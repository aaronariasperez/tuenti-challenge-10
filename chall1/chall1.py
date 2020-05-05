file = open('submitInput','r')
cases = file.readline()
resto = file.readlines()

resultado = ""
casenumber = 1
for r in resto:
    resultado += 'Case #'+str(casenumber)+': '
    first, second = r.split()
    if first == 'R':
        if second == 'R':
            resultado += '-'
        elif second == 'S':
            resultado += 'R'
        else:
            resultado += 'P'
    elif first == 'P':
        if second == 'R':
            resultado += 'P'
        elif second == 'S':
            resultado += 'S'
        else:
            resultado += '-'
    else:
        if second == 'R':
            resultado += 'R'
        elif second == 'S':
            resultado += '-'
        else:
            resultado += 'S'
    resultado += '\n'
    casenumber += 1
print(resultado)
file = open('chall1.out','w')
file.write(resultado)