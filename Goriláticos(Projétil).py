import time, curses, textwrap
import numpy as np
from curses import wrapper

def parab(stdscr, angulo1, velocidade1, x_player):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    g = 9.8 
    theta = angulo1*(np.pi / 180)
    t_subida = (velocidade1 * np.sin(theta)) /g
    t_total = t_subida * 2
    alt_max = ((velocidade1**2) * (np.sin(theta))**2) /2*g
    alcance = ((velocidade1 **2) * np.sin(2*theta)) /g
    x = 0
    t = 0
    x_mao_macaco = 4
    y_mao_macaco = 0
    loop_coord = 0

    if(x_player %2 == 0):
        x_player = -w
        inverter = -1
    else:
        x_player = 0
        inverter = 1

    while(loop_coord == 0):
        if(x < w):
            vy = (velocidade1 * np.sin(theta)) - g*t
            x = int(x_mao_macaco + ((velocidade1*t) * np.cos(theta)) + x_player)*inverter
            y = y_mao_macaco + int(h - ((vy*t))-((0.5*g)*(t**2)))

            try:
                stdscr.clear()
                stdscr.addstr(y, x, "💣", curses.color_pair(3))
                #Checar posições x e y:
                #stdscr.addstr(10, 10, f"X: {x}")
                #stdscr.addstr(10, 20, f"Y: {y}")
                stdscr.refresh()
            except curses.error:
                stdscr.refresh()
                pass

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
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    angulo1 = 10
    velocidade1 = 20
    loop_ang = 1
    x_player = 1
    stdscr.clear()
      
    while(loop_ang != 0):
        stdscr.addstr(5, 3, f"Ângulo: {angulo1}", curses.color_pair(1))
        key = stdscr.getch()

        if key == curses.KEY_UP and angulo1 < 85:
            angulo1 += 1
        elif key == curses.KEY_DOWN and angulo1 > 10:
            angulo1 -= 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            loop_vel = 1
        
            while(loop_vel == 1):
                stdscr.addstr(7, 3, f"Velocidade: {velocidade1}", curses.color_pair(1))
                key = stdscr.getch()
                if key == curses.KEY_UP and velocidade1 < 80:
                    velocidade1 += 1
                elif key == curses.KEY_DOWN and velocidade1 > 20:
                    velocidade1 -= 1
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    parab(stdscr, angulo1, velocidade1, x_player)
                    angulo1 = 10
                    velocidade1 = 20
                    x_player += 1
                    loop_vel = 0
                    #loop_ang = 0
                    break

    stdscr.refresh()

wrapper(traj)