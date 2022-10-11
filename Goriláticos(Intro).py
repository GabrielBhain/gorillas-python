import sys, time, os, curses, textwrap
from curses import wrapper
from msvcrt import kbhit, getch

menu = [" Jogar ", " Ranking ", " Como Jogar", " Sair "]
# Introdução do jogo
def intro_game():
    os.system('cls')
    intro = "No ano de 2043 um grupo de gorilas inteligentes treinados pela National Aeronautics and Space Administration (NASA) foram enviados a lua Europa do planeta Júpiter, eles ficaram conhecidos mundialmente como os Goriláticos e tinham a finalidade de colonizar a Europa, para descobrir se realmente seria possível que os humanos sobrevivessem nela apenas com os recursos lá presentes. \n Foi descoberto a existência de algumas plantas que conseguiram se desenvolver naquele solo, algumas delas eram bananeiras que originavam frutos com efeitos nunca antes vistos, alguns deles chegando até a explodir quando em contato com algum objeto (como a roupa espacial dos gorilas, por exemplo).Entretanto, algo inesperado aconteceu... \n Segundo informações captadas pelos androides enviados para auxiliar os Goriláticos na missão, o grupo teria conseguido ingerir água do planeta pela primeira vez, mas nela estava presente um composto químico que, em contato com os gorilas, afeta o sistema nervoso deles os deixando extremamente agressivos...\n E agora, o que acontecerá na missão? Será possível retomar a consciência deles a tempo? Você tem a missão de ajudá-los nisso!"
    intro_format = "\n".join(textwrap.wrap(intro, width=100, initial_indent="\t\t\t\t"))
    tecla_p = 0
    t = 1
    print("\n\n")
    
    for i_f in intro_format:
        for i in i_f:
            sys.stdout.flush()
            time.sleep(0.1*t)
            print(i, end="")

            if(i == "\n"):
                sys.stdout.flush()
                print(end="\t\t\t")
                
            elif(i == "!"):
                sys.stdout.flush()
                print("\n\n\t\t\t\t\t---------Pressione a tecla P para pular a introdução---------")
                getch()
                while(tecla_p != 1):
                    if(getch() == b'p'):
                        tecla_p = 1    
                        break

            elif(kbhit()):
                sys.stdout.flush()
                t = 0

def static(stdscr, texto):
    stdscr.clear()
    texto = "Bem-vindo ao Goriláticos"
    h, w = stdscr.getmaxyx()
    x = w//2 - len(texto)//2
    y = h//2
    stdscr.addstr(y, x, texto)
    stdscr.refresh()

# Caixa de seleção do menu
def menu_prin(stdscr, opcao_selecionada):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - 10
        y = h//2 - len(menu)//2 + idx
        if idx == opcao_selecionada:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

# Confirmar saida do usuário
def menu_sair(stdscr, opcao_selecionada):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    despedida = "Você tem certeza que deseja sair do jogo?\n"
    confirm = [" Sim ", " Não "]
    x = w//2 - len(despedida)//2
    y = h//2
    stdscr.addstr(y, x, despedida)
    for idx, row in enumerate(confirm):
        x = w//2 - len(row) + idx*5
        y = h//2 + len(confirm)
        if idx == opcao_selecionada:
            stdscr.attron(curses.color_pair(1),)
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()
    
# Função Principal
def prin(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    linha_escolhida = 0
    escolha_sair = 1

    menu_prin(stdscr, linha_escolhida)

    while(escolha_sair != 0):
        key = stdscr.getch()
        if key == curses.KEY_UP and linha_escolhida > 0:
            linha_escolhida -= 1
        elif key == curses.KEY_DOWN and linha_escolhida < len(menu)-1:
            linha_escolhida += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if linha_escolhida == len(menu)-1:
                menu_sair(stdscr, escolha_sair)
                while linha_escolhida == len(menu)-1:
                    key = stdscr.getch()
                    if key == curses.KEY_LEFT and escolha_sair > 0:
                        escolha_sair -= 1
                    elif key == curses.KEY_RIGHT and escolha_sair < 1:
                        escolha_sair += 1
                    elif key == curses.KEY_ENTER or key in [10, 13]:
                        if escolha_sair == 0:
                            break
                        elif escolha_sair == 1:
                            linha_escolhida = 0
                    menu_sair(stdscr, escolha_sair)

        menu_prin(stdscr, linha_escolhida)
        
intro_game()
wrapper(prin) 