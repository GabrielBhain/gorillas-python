import sys, time, os, curses, textwrap
from curses import wrapper
from msvcrt import kbhit, getch
import Banana

menu = [" Jogar ", " Ranking ", " Como Jogar", " Sair "]

dificuldades = [" Fácil ", " Médio ", " Difícil ", " Voltar "]

# Introdução do jogo
def intro_game():
    os.system('cls')
    intro = "No ano de 2043 um grupo de gorilas inteligentes treinados pela National Aeronautics and Space Administration (NASA) foram enviados a lua Europa do planeta Júpiter, eles ficaram conhecidos mundialmente como os Goriláticos e tinham a finalidade de colonizar a Europa, para descobrir se realmente seria possível que os humanos sobrevivessem nela apenas com os recursos lá presentes. Foi descoberto a existência de algumas plantas que conseguiram se desenvolver naquele solo, algumas delas eram bananeiras que originavam frutos com efeitos nunca antes vistos, alguns deles chegando até a explodir quando em contato com algum objeto (como a roupa espacial dos gorilas, por exemplo). Entretanto, algo inesperado aconteceu... Segundo informações captadas pelos androides enviados para auxiliar os Goriláticos na missão, o grupo teria conseguido ingerir água do planeta pela primeira vez, mas nela estava presente um composto químico que, em contato com os gorilas, afeta o sistema nervoso deles os deixando extremamente agressivos... E agora, o que acontecerá na missão? Será possível retomar a consciência deles a tempo? Você tem a missão de ajudá-los nisso!"
    intro_format = "\n".join(textwrap.wrap(intro, width=100, initial_indent="\t\t\t\t\t", subsequent_indent="\t\t\t\t"))
    tecla_p = 0
    t = 1
    print("\n\n\n\n")
    
    for i_f in intro_format:
        for i in i_f:
            sys.stdout.flush()
            time.sleep(0.05*t)
            print(i, end="")

            if(i == "!"):
                sys.stdout.flush()
                print("\n\n\n\t\t\t\t\t\t---------Pressione a tecla P para pular a introdução---------")
                getch()
                while(tecla_p != 1):
                    if(getch() == b'p'):
                        tecla_p = 1
                        break

            elif(kbhit()):
                sys.stdout.flush()
                t = 0

def como_jogar(stdscr):
    como_jogar = "O jogo consiste na disputa entre dois gorilas, cada jogador vai ter que arremessar uma banana no adversário a fim de derrotá-lo. Cada banana atingida no gorila contará como +50 pontos na pontuação do jogador e acertar obstáculos acrescentará +10 pontos na pontuação. Existem 3 dificuldades divididas em fácil, normal e difícil... Na primeira dificuldade a gravidade da lua Europa é igual a 9.8 (valor não correspondente a realidade) e a quantidade de obstáculos é normal. Na dificuldade 'normal' os gorilas estão em uma enorme cratera onde a gravidade da lua Europa passa a ser igual a 11 (valor não correspondente a realidade) e a quantidade de obstáculos é normal. No 'difícil' as condições são semelhantes a dificuldade anterior, mas com a máxima quantidade de obstáculos."
    format = "\n".join(textwrap.wrap(como_jogar, width=100, initial_indent= "\t\t\t\t\t", subsequent_indent= "\t\t\t\t"))

    stdscr.clear()
    stdscr.addstr(10, 0, format)
    stdscr.addstr(20, 60, "\n\n\t\t\t\t\t\t---------Pressione qualquer tecla para voltar ao menu---------")
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

# Confirmar saída do usuário
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

def ranking(stdscr):
    h, w = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.addstr(h//2 -2, w//2 - 10, "Pontuação do jogador 1: ")
    stdscr.addstr(h//2, w//2 - 10, "Pontuação do jogador 2: ")
    stdscr.refresh()

def jogar(stdscr, opcao_selecionada):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(dificuldades):
        x = w//2 - 10
        y = h//2 - len(dificuldades)//2 + idx
        if idx == opcao_selecionada:
            stdscr.attron(curses.color_pair(1))
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
        tecla = stdscr.getch()
        if tecla == curses.KEY_UP and linha_escolhida > 0:
            linha_escolhida -= 1
        elif tecla == curses.KEY_DOWN and linha_escolhida < len(menu)-1:
            linha_escolhida += 1
        elif tecla == curses.KEY_ENTER or tecla in [10, 13]:
            if linha_escolhida == len(menu)-1:
                menu_sair(stdscr, escolha_sair)
                # O usuário escolheu sair do jogo e será pedido uma confirmação
                while linha_escolhida == len(menu)-1:
                    tecla = stdscr.getch()
                    if tecla == curses.KEY_LEFT and escolha_sair > 0:
                        escolha_sair -= 1
                    elif tecla == curses.KEY_RIGHT and escolha_sair < 1:
                        escolha_sair += 1
                    elif tecla == curses.KEY_ENTER or tecla in [10, 13]:
                        if escolha_sair == 0:
                            break
                        elif escolha_sair == 1:
                            linha_escolhida = 0
                    menu_sair(stdscr, escolha_sair)

            elif linha_escolhida == len(menu)-2:
                # O usuário quer saber como jogar
                como_jogar(stdscr)
                getch()

            elif linha_escolhida == len(menu)-3:
                # O usuário quer consultar o ranking
                ranking(stdscr)
                getch()

            elif linha_escolhida == 0:
                jogar(stdscr, linha_escolhida)

                while(escolha_sair != 0):
                    tecla = stdscr.getch()
                    if tecla == curses.KEY_UP and linha_escolhida > 0:
                        linha_escolhida -= 1
                    elif tecla == curses.KEY_DOWN and linha_escolhida < len(dificuldades)-1:
                        linha_escolhida += 1
                    elif tecla == curses.KEY_ENTER or tecla in [10, 13]:
                        if linha_escolhida == 3:
                            linha_escolhida = 0
                            break
                        elif linha_escolhida == 0:
                            # Dificuldade fácil
                            stdscr.refresh()
                            Banana.jogo()

                        elif linha_escolhida == 1:
                            #Dificuldade normal
                            stdscr.refresh()
                            Banana.jogo("Algum argumento")

                        elif linha_escolhida == 2:
                            #Dificuldade difícil
                            stdscr.refresh()
                            Banana.jogo("Algum argumento")

                    jogar(stdscr, linha_escolhida)

        menu_prin(stdscr, linha_escolhida)
        
intro_game()
wrapper(prin) 