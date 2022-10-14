import sys, time, os, curses, textwrap
import numpy as np
from curses import wrapper
from msvcrt import kbhit, getch

def parab(stdscr, angulo1, velocidade1):
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
    loop_coord = 0

    while(loop_coord == 0):
        if(x < w):
            #vy = (velocidade1 * np.sin(theta)) + g*t
            x = 4 + int(((velocidade1*t) * np.cos(theta))) 
            y = int(h - ((velocidade1*t) * np.sin(theta))-((0.5*g)*(t**2)))
            
            try:
                stdscr.clear()
                stdscr.addstr(y, x, "O", curses.color_pair(3))
                stdscr.refresh()
            except curses.error:
                stdscr.clear()
                stdscr.refresh()
                pass

            if(t > t_subida):
                if(g == 9.8):
                    g = -9.8
                    
            elif(x > w):
                loop_coord = 1
            
            #Checar posições x e y:
            #stdscr.addstr(10, 10, f"X: {x}")
            #stdscr.addstr(10, 20, f"Y: {y}")
            t += 0.1
            time.sleep(0.5)
            
        elif(y > h):
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
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED)
    angulo1 = 10
    velocidade1 = 20
    loop_ang = 1

    stdscr.clear()

    while(loop_ang != 0):
        stdscr.addstr(10, 0, f"Ângulo: {angulo1}", curses.color_pair(2))
        key = stdscr.getch()

        if key == curses.KEY_UP and angulo1 < 85:
            angulo1 += 1
        elif key == curses.KEY_DOWN and angulo1 > 10:
            angulo1 -= 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            loop_ang = 0
            loop_vel = 0

            while(loop_vel == 0):
                stdscr.addstr(12, 0, f"Velocidade: {velocidade1}", curses.color_pair(2))
                key = stdscr.getch()
                
                if key == curses.KEY_UP and velocidade1 < 50:
                    velocidade1 += 1
                elif key == curses.KEY_DOWN and velocidade1 > 20:
                    velocidade1 -= 1
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    parab(stdscr, angulo1, velocidade1)
                    break

    stdscr.refresh()

wrapper(traj)