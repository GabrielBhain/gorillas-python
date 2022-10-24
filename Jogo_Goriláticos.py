import time, curses, sys
import numpy as np
from curses import wrapper
import random

o1,o2,o3,o4 = 0,0,0,0
coords1 = []
coords2 = []
coords3 = []
coords4 = []
objeto1 = []
objeto2 = []
objeto3 = []
objeto4 = []

altura1 = random.randint(15,35)
altura2 = random.randint(15,35)


posicaoGorilaP1 = [[altura1 - 3,9],[altura1 - 3,10],[altura1 - 3,11], [altura1 - 2,9],[altura1 - 2,10],[altura1 - 2,11],[altura1 - 1,9],[altura1 - 1,10],[altura1 - 1,11]]
posicaoGorilaP2 = [[altura2 - 3,115],[altura2 - 3,116],[altura2 - 3,117],[altura2 - 2,115],[altura2 - 2,116],[altura2 - 2,117],[altura2 - 1,115],[altura2 - 1,116],[altura2 - 1,117]]

gorilacabeca = [['á','“',']'],['[','”','à']]
gorilacorpo = ['/','◙','\\']
gorilapernas = [['(',' ','('],[')',' ',')']]

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

def planeta1(stdscr):
    for i in range(altura1 ,altura1 + 7):
        for g in range (6,15):
            stdscr.addstr(i,g,'█')
    for k in range(altura1 + 1,altura1 + 6):
            stdscr.addstr(k,15,'█')
    for j in range(altura1 + 2, altura1 + 5):
            stdscr.addstr(j,16,'█')
    stdscr.refresh()


def planeta2(stdscr):
    for i in range(altura2,altura2 + 7):
        for g in range (111,120):
            stdscr.addstr(i,g,'█')
    for k in range(altura2 +1,altura2 +6):
            stdscr.addstr(k,110,'█')
    for j in range(altura2 + 2,altura2 + 5):
            stdscr.addstr(j,109,'█')
    stdscr.refresh()

def printObject(stdscr,object,objectCoords):
    for num in range(0,len(object)):
        stdscr.addstr(objectCoords[num][0],objectCoords[num][1],object[num])

def chooseObject(coords,objeto, xf):
    numeroObjeto = random.randint(1,3)
    if numeroObjeto == 1:
        yf = random.randint(12,38)
        objeto = ['Å','/','º','\\','/','ᴳ','ᴿ','ᴸ','\\','|','╔','═','╗','|','|','║','▒','║','|','|','║','▒','║','|','|','║','▒','║','|','|','║','▒','║','|','╔','╚','W','╝','╗']
        coords = [[yf-4,xf],[yf-3,xf-1],[yf-3,xf],[yf-3,xf+1],[yf-2,xf-2],[yf-2,xf-1],[yf-2,xf],[yf-2,xf+1],[yf-2,xf+2],[yf-1,xf-2],[yf-1,xf-1],[yf-1,xf],[yf-1,xf+1],[yf-1,xf+2],[yf,xf-2],[yf,xf-1],[yf,xf],[yf,xf+1],[yf,xf+2],[yf+1,xf-2],[yf+1,xf-1],[yf+1,xf],[yf+1,xf+1],[yf+1,xf+2],[yf+2,xf-2],[yf+2,xf-1],[yf+2,xf],[yf+2,xf+1],[yf+2,xf+2],[yf+3,xf-2],[yf+3,xf-1],[yf+3,xf],[yf+3,xf+1],[yf+3,xf+2],[yf+4,xf-2],[yf+4,xf-1],[yf+4,xf],[yf+4,xf+1],[yf+4,xf+2]]
    elif numeroObjeto == 2:
        yf = random.randint(12,38)
        objeto = ['▄','▄','▄','▐','▄','◙','▄','▌']
        coords = [[yf-1,xf-1],[yf-1,xf],[yf-1,xf+1],[yf,xf-2],[yf,xf-1],[yf,xf],[yf,xf+1],[yf,xf+2]]
    elif numeroObjeto == 3:
        yf = random.randint(12,38)
        objeto = ['▄','▄','▄','▄','▄','█','█','█','█','█','█','█','█','█','█','█','█''█','█','█','▀','▀','▀','▀','▀']
        coords = [[yf-1,xf-2],[yf-1,xf-1],[yf-1,xf],[yf-1,xf+1],[yf-1,xf+2],[yf,xf-3],[yf,xf-2],[yf,xf-1],[yf,xf],[yf,xf+1],[yf,xf+2],[yf,xf+3],[yf+1,xf-3],[yf+1,xf-2],[yf+1,xf-1],[yf+1,xf],[yf+1,xf+1],[yf+1,xf+2],[yf+1,xf+3],[yf+2,xf-2],[yf+2,xf-1],[yf+2,xf],[yf+2,xf+1],[yf+2,xf+2]]
    return coords,objeto

def gencoord():
    global objeto1,objeto2,objeto3,objeto4,coords1,coords2,coords3,coords4
    coords1,objeto1 = chooseObject(coords1,objeto1,35)
    coords2,objeto2 = chooseObject(coords2,objeto2,55)
    coords3,objeto3 = chooseObject(coords3,objeto3,75)
    coords4,objeto4 = chooseObject(coords4,objeto4,95)

def gerarCenario(stdscr):
    global objeto1,objeto2,objeto3,objeto4,coords1,coords2,coords3,coords4,o1,o2,o3,o4
    planeta1(stdscr)
    planeta2(stdscr)
    gorilaP1(stdscr)
    gorilaP2(stdscr)
    if o1 < 3:
        printObject(stdscr,objeto1,coords1)
    if o2 < 3:
        printObject(stdscr,objeto2,coords2)
    if o3 < 3:
        printObject(stdscr,objeto3,coords3)
    if o4 < 3:
        printObject(stdscr,objeto4,coords4)

pontos_p1, pontos_p2 = 0, 0
def parab(stdscr, angulo1, velocidade1, x_player, aumentar_grav):
    global o1, o2, o3, o4, pontos_p1, pontos_p2
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
                #Checar posições x e y:
                #stdscr.addstr(10, 10, f"X: {x}")
                #stdscr.addstr(10, 20, f"Y: {y}")
                stdscr.refresh()
            except curses.error:
                stdscr.refresh()
                pass
            
            if [y, x] in coords1 and o1 < 3:
                o1 += 1
                if o1 == 3:
                    stdscr.clear()
                    gerarCenario(stdscr)
                break
            if [y, x] in coords2 and o2 < 3:
                o2 += 1
                if o2 == 3:
                    stdscr.clear()
                    gerarCenario(stdscr)
                break
            if [y, x] in coords3 and o3 < 3:
                o3 += 1
                if o3 == 3:
                    stdscr.clear()
                    gerarCenario(stdscr)
                break
            if [y, x] in coords4 and o4 < 3:
                o4 += 1
                if o4 == 3:
                    stdscr.clear()
                    gerarCenario(stdscr)
                break
            
            if [y, x] in posicaoGorilaP1:
                stdscr.addstr(h//2 - 5, w//2 - 10, "+50 Pontos para o Player 2", curses.color_pair(2))
                stdscr.refresh()
                time.sleep(3)
                stdscr.clear()
                gerarCenario(stdscr)
                pontos_p2 += 50
                break
            elif [y, x] in posicaoGorilaP2:
                stdscr.addstr(h//2 - 5, w//2 - 10, "+50 Pontos para o Player 1", curses.color_pair(2))
                stdscr.refresh()
                time.sleep(3)
                stdscr.clear()
                gerarCenario(stdscr)
                pontos_p1 += 50
                break
            
            t += 0.05
            time.sleep(0.02)

            if(y > h):
                loop_coord = 1
                break 
            elif(x < 0):
                loop_coord = 1
                break

        elif(x > w):
            loop_coord = 1
            break    
        else:
            break
        
    stdscr.refresh()

def traj(stdscr):
    global pontos_p1, pontos_p2
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    angulo1 = 10
    velocidade1 = 20
    loop_ang = 1
    x_player = 13
    stdscr.clear()
    gerarCenario(stdscr)

    while(loop_ang != 0):
        stdscr.refresh()
        stdscr.addstr(1, 1, f" Player 1: {pontos_p1}   Player 2: {pontos_p2}", curses.color_pair(1))
        stdscr.addstr(5, 3, f" Ângulo: {angulo1} ", curses.color_pair(1))
        
        key = stdscr.getch()

        if key == curses.KEY_UP and angulo1 < 85:
            angulo1 += 1
        elif key == curses.KEY_DOWN and angulo1 > 10:
            angulo1 -= 1
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

        if(pontos_p1 >= 50 or pontos_p2 >= 50):
            loop_ang = 0
            pontos_p1, pontos_p2 = 0, 0
            break

    stdscr.refresh()

def jogo(num):
    try:
        gencoord()
        global o1, o2, o3, o4
        o1, o2, o3, o4 = 0, 0, 0, 0
        if num == 1:
            o3 = 3
            o4 = 4
        elif num == 2:
            o4 = 3
        wrapper(traj)
        
    except curses.error:
        pass