file = open('submitInput', 'r')
cases = int(file.readline())
resto = file.readlines()

end = False
ind = 0
resultado = ''
casenumber = 1
victorias = {}
derrotas = {}
for i in range(cases):
    resultado += 'Case #'+str(casenumber)+': '
    casenumber += 1
    n_matches = int(resto[ind])
    ind += 1
    matches = resto[ind:ind+n_matches]
    ind += n_matches
    for m in matches:
        op1, op2, win = m.split()
        if win == '1':
            if op1 not in victorias.keys():
                victorias[op1] = 1
            else:
                victorias[op1] = victorias[op1] + 1

            if op2 not in derrotas.keys():
                derrotas[op2] = 1
            else:
                derrotas[op2] = derrotas[op2] + 1
        else:
            if op2 not in victorias.keys():
                victorias[op2] = 1
            else:
                victorias[op2] = victorias[op2] + 1

            if op1 not in derrotas.keys():
                derrotas[op1] = 1
            else:
                derrotas[op1] = derrotas[op1] + 1

    strongest_op = ''
    strongest_proportion = 0
    for k,v in victorias.items():
        if k in derrotas:
            if v/derrotas[k] > strongest_proportion:
                strongest_op = k
                strongest_proportion = v/derrotas[k]
        else:
            strongest_proportion = v
            strongest_op = k

    resultado += strongest_op+'\n'
    victorias = {}
    derrotas = {}

print(resultado)
file = open('chall2.out','w')
file.write(resultado)
