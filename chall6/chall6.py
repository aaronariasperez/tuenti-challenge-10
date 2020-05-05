import socket
import time
import random

HOST = '52.49.91.111'  # The server's hostname or IP address
PORT = 2003        # The port used by the server

class Casilla:
    def __init__(self, pos, trozo_mapa):
        self.position = pos
        self.neighs = []

        if trozo_mapa[0][1] == '.' or trozo_mapa[0][1] == 'P':
            self.neighs.append((pos[0]+2,pos[1]-1,0))
        if trozo_mapa[0][3] == '.' or trozo_mapa[0][3] == 'P':
            self.neighs.append((pos[0]+2,pos[1]+1,1))
        if trozo_mapa[1][4] == '.' or trozo_mapa[1][4] == 'P':
            self.neighs.append((pos[0]+1,pos[1]+2,2))
        if trozo_mapa[3][4] == '.' or trozo_mapa[3][4] == 'P':
            self.neighs.append((pos[0]-1,pos[1]+2,3))
        if trozo_mapa[4][3] == '.' or trozo_mapa[4][3] == 'P':
            self.neighs.append((pos[0]-2,pos[1]+1,4))
        if trozo_mapa[4][1] == '.' or trozo_mapa[4][1] == 'P':
            self.neighs.append((pos[0]-2,pos[1]-1,5))
        if trozo_mapa[3][0] == '.' or trozo_mapa[3][0] == 'P':
            self.neighs.append((pos[0]-1,pos[1]-2,6))
        if trozo_mapa[1][0] == '.' or trozo_mapa[1][0] == 'P':
            self.neighs.append((pos[0]+1,pos[1]-2,7))

    def rehacer_vecinos(self, trozo_mapa, pos):
        if trozo_mapa[0][1] == '.' or trozo_mapa[0][1] == 'P':
            self.neighs.append((pos[0]+2,pos[1]-1,0))
        if trozo_mapa[0][3] == '.' or trozo_mapa[0][3] == 'P':
            self.neighs.append((pos[0]+2,pos[1]+1,1))
        if trozo_mapa[1][4] == '.' or trozo_mapa[1][4] == 'P':
            self.neighs.append((pos[0]+1,pos[1]+2,2))
        if trozo_mapa[3][4] == '.' or trozo_mapa[3][4] == 'P':
            self.neighs.append((pos[0]-1,pos[1]+2,3))
        if trozo_mapa[4][3] == '.' or trozo_mapa[4][3] == 'P':
            self.neighs.append((pos[0]-2,pos[1]+1,4))
        if trozo_mapa[4][1] == '.' or trozo_mapa[4][1] == 'P':
            self.neighs.append((pos[0]-2,pos[1]-1,5))
        if trozo_mapa[3][0] == '.' or trozo_mapa[3][0] == 'P':
            self.neighs.append((pos[0]-1,pos[1]-2,6))
        if trozo_mapa[1][0] == '.' or trozo_mapa[1][0] == 'P':
            self.neighs.append((pos[0]+1,pos[1]-2,7))

def parsear(recibido):
    mapa = [['' for x in range(5)] for y in range(5)]
    #print("***********")
    #print(recibido)
    #print("***********")
    for i in range(5):
        #print(mapa)

        for j in range(5):
            mapa[i][j] = recibido[j]
        recibido = recibido[7:]
    #print(mapa)
    return mapa

def beauty_print(m):
    for i in range(5):
        for j in range(5):
            print(m[i][j], end='')
        print()

def existe(pos, lista):
    index = 0
    for i,c in enumerate(lista):
        if pos == c.position:
            index = i
    return index

def reverse(mov, pos):
    res = (0,0,0)
    if mov[2] == 0:
        res = (pos[0]-2, pos[1]+1, 4)
    elif mov[2] == 1:
        res = (pos[0]-2, pos[1]-1, 5)
    elif mov[2] == 2:
        res = (pos[0]-1, pos[1]-2, 6)
    elif mov[2] == 3:
        res = (pos[0]+1, pos[1]-2, 7)
    elif mov[2] == 4:
        res = (pos[0]+2, pos[1]-1, 0)
    elif mov[2] == 5:
        res = (pos[0]+2, pos[1]+1, 1)
    elif mov[2] == 6:
        res = (pos[0]+1, pos[1]+2, 2)
    elif mov[2] == 7:
        res = (pos[0]-1, pos[1]+2, 3)
    return res

def random_mov(lista):
    ind = random.randint(0,len(lista)-1)
    return lista[ind]


casillas = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #end = False
    #while not end:

    #s.send(b'2u1r')
    data = s.recv(1024)
    recibido = repr(data).split()[0][2:]
    beauty_print(parsear(recibido))
    #print(recibido)
    recibido = recibido[:len(recibido)-3]
    trozo_mapa = parsear(recibido)

    cas_initial = Casilla((0,0),trozo_mapa)
    casillas.append(cas_initial)
    #print(cas_initial.neighs)
    casilla_actual = cas_initial
    ultimo_mov = ''
    casillas_bloqueadas = 0
    ultimos_mov = []

    end = False
    while not end:
        #print("-------------")
        print("vecinos de la casilla "+str(casilla_actual.position))
        #print(casilla_actual.neighs)
        if not casilla_actual.neighs:
            casilla_actual.rehacer_vecinos(trozo_mapa, casilla_actual.position)
            mov = random_mov(casilla_actual.neighs)
            ##mov = reverse(ultimos_mov[len(ultimo_mov) - 1 - casillas_bloqueadas], casilla_actual.position)
            ##casillas_bloqueadas += 1

            #if casillas_bloqueadas == 0:
            #    casillas_bloqueadas += 1
            #    mov = reverse(ultimo_mov, casilla_actual.position)
            #elif casillas_bloqueadas == 1:
            #    casillas_bloqueadas += 1
            #    mov = reverse(penultimo_mov, casilla_actual.position)
            #else:
            #    print("************************")
        else:
            #casillas_bloqueadas = 0
            #mov = casilla_actual.neighs.pop()
            mov = random_mov(casilla_actual.neighs)
            casilla_actual.neighs.remove(mov)
            #ultimos_mov.append(mov)
        #print(mov)
        #penultimo_mov = ultimo_mov
        #ultimo_mov = mov
        #ultimos_mov.append(mov)

        if mov[2] == 0:
            s.send(b'2u1l')
        elif mov[2] == 1:
            s.send(b'2u1r')
        elif mov[2] == 2:
            s.send(b'1u2r')
        elif mov[2] == 3:
            s.send(b'1d2r')
        elif mov[2] == 4:
            s.send(b'2d1r')
        elif mov[2] == 5:
            s.send(b'2d1l')
        elif mov[2] == 6:
            s.send(b'1d2l')
        elif mov[2] == 7:
            s.send(b'1u2l')

        data = s.recv(1024)
        recibido = repr(data).split()[0][2:]
        #print('mov: '+str(mov[2]))
        beauty_print(parsear(recibido))

        trozo_mapa = parsear(recibido)

        cas = Casilla((mov[0], mov[1]), trozo_mapa)
        ind = existe(cas.position, casillas)
        if ind == 0:
            casillas.append(cas)
            casilla_actual = cas
        else:
            casilla_actual = casillas[ind]

        # print(cas_initial.neighs)
        #casilla_actual = cas

        #time.sleep()
        if casilla_actual.position == ():
            end= True
