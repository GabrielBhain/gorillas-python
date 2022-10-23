import time, curses, sys
import numpy as np
from curses import wrapper
import random

def cordsGen(stdscr):
    global foguete, coordsFoguete, posicaoGorilaP1, posicaoGorilaP2, gorilacabeca, gorilacorpo, gorilapernas, objetos
    xf = random.randint(26,105)
    yf = random.randint(12,28)
    foguete = ['Å','/','º','\\','/','ᴳ','ᴿ','ᴸ','\\','|','╔','═','╗','|','|','║','▒','║','|','|','║','▒','║','|','|','║','▒','║','|','|','║','▒','║','|','╔','╚','W','╝','╗']
    coordsFoguete = [[yf-4,xf],[yf-3,xf-1],[yf-3,xf],[yf-3,xf+1],[yf-2,xf-2],[yf-2,xf-1],[yf-2,xf],[yf-2,xf+1],[yf-2,xf+2],[yf-1,xf-2],[yf-1,xf-1],[yf-1,xf],[yf-1,xf+1],[yf-1,xf+2],[yf,xf-2],[yf,xf-1],[yf,xf],[yf,xf+1],[yf,xf+2],[yf+1,xf-2],[yf+1,xf-1],[yf+1,xf],[yf+1,xf+1],[yf+1,xf+2],[yf+2,xf-2],[yf+2,xf-1],[yf+2,xf],[yf+2,xf+1],[yf+2,xf+2],[yf+3,xf-2],[yf+3,xf-1],[yf+3,xf],[yf+3,xf+1],[yf+3,xf+2],[yf+4,xf-2],[yf+4,xf-1],[yf+4,xf],[yf+4,xf+1],[yf+4,xf+2]]

    posicaoGorilaP1 = [[altura1 - 3,9],[altura1 - 3,10],[altura1 - 3,11], [altura1 - 2,9],[altura1 - 2,10],[altura1 - 2,11],[altura1 - 1,9],[altura1 - 1,10],[altura1 - 1,11]]
    posicaoGorilaP2 = [[altura2 - 3,115],[altura2 - 3,116],[altura2 - 3,117],[altura2 - 2,115],[altura2 - 2,116],[altura2 - 2,117],[altura2 - 1,115],[altura2 - 1,116],[altura2 - 1,117]]

    gorilacabeca = [['á','“',']'],['[','”','à']]
    gorilacorpo = ['/','◙','\\']
    gorilapernas = [['(',' ','('],[')',' ',')']]
    objetos = []

def gerarObjetos(quantity):
    gerados = 0
    while (quantity > gerados):
        gerarObjeto()
        quantity += 1

def chooseObject():
    number = random.randint(1,5)
    if number == 1:
        coords = coordsFoguete
        objeto = foguete
    
    return coords, objeto


def gerarObjeto(stdscr):
    coords, objeto = list
    tentativas = 0
    valido = False
    while tentativas < 20 or valido == False:
        chooseObject()
        xf = random.randint(31,95)
        yf = random.randint(12,38)
        colisao = bool
        checkColision(coords,objeto)
        if colisao == True:
            tentativas =+ 1
        elif colisao == False:
            valido = True
            if valido == True:
                printObject(stdscr,objeto,coords)


def gorilaP1(stdscr):
    numero = 0
    for y,x in posicaoGorilaP1[0], posicaoGorilaP1[1], posicaoGorilaP1[2]:
        stdscr.addstr(y, x, gorilacabeca[1][numero])
        numero += 1
    numero = 0
    for y,x in posicaoGorilaP1[3], posicaoGorilaP1[4], posicaoGorilaP1[5]:
        stdscr.addstr(y, x, gorilacorpo[numero])
        numero += 1
    numero = 0
    for y,x in posicaoGorilaP1[6], posicaoGorilaP1[7], posicaoGorilaP1[8]:
        stdscr.addstr(y, x, gorilapernas[1][numero])
        numero += 1
    stdscr.refresh()

def gorilaP2(stdscr):
    numero = 0
    for y,x in posicaoGorilaP2[0], posicaoGorilaP2[1], posicaoGorilaP2[2]:
        stdscr.addstr(y, x, gorilacabeca[0][numero])
        numero += 1
    numero = 0
    for y,x in posicaoGorilaP2[3], posicaoGorilaP2[4], posicaoGorilaP2[5]:
        stdscr.addstr(y, x, gorilacorpo[numero])
        numero += 1
    numero = 0
    for y,x in posicaoGorilaP2[6], posicaoGorilaP2[7], posicaoGorilaP2[8]:
        stdscr.addstr(y, x, gorilapernas[0][numero])
        numero += 1
    stdscr.refresh()

def printObject(stdscr,object,objectCoords):
    object = []
    for num in range(0,len(object)):
        stdscr.addstr(objectCoords[num][0],objectCoords[num][1],object[num])
        object.append([objectCoords[num][0],objectCoords[num][1]])
    objetos.append(object)
    
def checkColision(objectCoord,objects):
	colisao = True
	while colisao == True:
		for numero in range(0,len(objectCoord)):
			for numero2 in range (0,len(objects)):
				if objectCoord[numero] == objects[numero2]:
					colisao = False
			else:
				colisao = True
	return colisao


def planeta1(stdscr):
    planeta=[]
    for i in range(altura1 ,altura1 + 7):
        for g in range (6,15):
            planeta.append([i,g])
            stdscr.addstr(i,g,'█')
    for k in range(altura1 + 1,altura1 + 6):
            planeta.append([k,15])
            stdscr.addstr(k,15,'█')
    for j in range(altura1 + 2, altura1 + 5):
            planeta.append([j,16])
            stdscr.addstr(j,16,'█')
    objetos.append(planeta)
    stdscr.refresh()


def planeta2(stdscr):
    planeta = []
    for i in range(altura2,altura2 + 7):
        for g in range (111,120):
            planeta.append([i,g])
            stdscr.addstr(i,g,'█')
    for k in range(altura2 +1,altura2 +6):
            planeta.append([k,110])
            stdscr.addstr(k,110,'█')
    for j in range(altura2 + 2,altura2 + 5):
            planeta.append([j,109])
            stdscr.addstr(j,109,'█')
    objetos.append(planeta)
    stdscr.refresh()


def gerarCenario(stdscr):
    planeta1(stdscr)
    planeta2(stdscr)
    gorilaP1(stdscr)
    gorilaP2(stdscr)
    printObject(stdscr,foguete,coordsFoguete)
    

def parab(stdscr, angulo1, velocidade1, x_player, aumentar_grav):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    g = 9.8*aumentar_grav 
    theta = angulo1*(np.pi / 180)
    #t_subida = (velocidade1 * np.sin(theta)) /g
    #t_total = t_subida * 2
    #alt_max = ((velocidade1**2) * (np.sin(theta))**2) /2*g
    #alcance = ((velocidade1 **2) * np.sin(2*theta)) /g
    x = 0
    t = 0
    x_mao_macaco = 13
    loop_coord = 0

    if(x_player %2 == 0):
        y_mao_macaco = h - altura2 +3
        x_player = -124
        inverter = -1
    else:
        y_mao_macaco = h - altura1 +3
        x_player = 0
        inverter = 1

    while(loop_coord == 0):
        if(x < w):
            vy = (velocidade1 * np.sin(theta)) - g*t
            x = int(x_mao_macaco + ((velocidade1*t) * np.cos(theta)) + x_player)*inverter
            y = -y_mao_macaco + int(h - ((vy*t))-((0.5*g)*(t**2)))

            try:
                stdscr.clear()
                gerarCenario(stdscr)
                stdscr.addstr(y, x, "💣", curses.color_pair(3))
                stdscr.refresh()
            except curses.error:
                stdscr.refresh()
                pass
            
            if [y, x] in posicaoGorilaP1:
                stdscr.clear()
                stdscr.addstr(h//2 - 5, w//2 - 5, "Player 2 WIN", curses.color_pair(2))
                break
            elif [y, x] in posicaoGorilaP2:
                stdscr.clear()
                stdscr.addstr(h//2 - 5, w//2 - 5, "Player 1 WIN", curses.color_pair(2))
                break
            
            t += 0.05
            time.sleep(0.1)

            if(y > h):
                x = w
            elif(x < 0):
                loop_coord = 1
                break

        elif(x > w):
            loop_coord = 1
            break    
        else:
            stdscr.clear()
            break
        
    stdscr.refresh()

def traj(stdscr):
    global altura1, altura2
    altura1 = random.randint(15,35)
    altura2 = random.randint(15,35)
    cordsGen(stdscr)
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    angulo1 = 10
    velocidade1 = 20
    loop_ang = 1
    x_player = 13
    stdscr.clear()
    '''if(dificuldade == 1 or 2):
        aumentar_grav = 1.12'''

    while(loop_ang != 0):
        stdscr.addstr(5, 3, f" Ângulo: {angulo1} ", curses.color_pair(1))
        gerarCenario(stdscr)
        key = stdscr.getch()

        if key == curses.KEY_UP and angulo1 < 85:
            angulo1 += 1
        elif key == curses.KEY_DOWN and angulo1 > 10:
            angulo1 -= 1
        elif key == curses.KEY_LEFT:
            sys.exit()
        elif key == curses.KEY_ENTER or key in [10, 13]:
            loop_vel = 1
        
            while(loop_vel == 1):
                stdscr.addstr(7, 3, f" Velocidade: {velocidade1} ", curses.color_pair(1))
                key = stdscr.getch()
                if key == curses.KEY_UP and velocidade1 < 80:
                    velocidade1 += 1
                elif key == curses.KEY_DOWN and velocidade1 > 20:
                    velocidade1 -= 1
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    parab(stdscr, angulo1, velocidade1, x_player, 1)
                    angulo1 = 10
                    velocidade1 = 20
                    x_player += 1
                    loop_vel = 0
                    break

    stdscr.refresh()

def jogo():
    wrapper(traj)