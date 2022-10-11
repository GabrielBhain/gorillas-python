import sys, time, os
from msvcrt import kbhit

texto = "No ano de 2043 um grupo de gorilas inteligentes treinados pela National Aeronautics and Space Administration (NASA) foram enviados a lua Europa do planeta Júpiter, eles ficaram conhecidos mundialmente como os Goriláticos e tinham a finalidade de colonizar a Europa, para descobrir se realmente seria possível que os humanos sobrevivessem nela apenas com os recursos lá presentes. \nFoi descoberto a existência de algumas plantas que conseguiram se desenvolver naquele solo, algumas delas eram bananeiras que originavam frutos com efeitos nunca antes vistos, alguns deles chegando até a explodir quando em contato com algum objeto (como a roupa espacial dos gorilas, por exemplo). \nEntretanto, algo inesperado aconteceu... \nSegundo informações captadas pelos androides enviados para auxiliar os Goriláticos na missão, o grupo teria conseguido ingerir água do planeta pela primeira vez, mas nela estava presente um composto químico que, em contato com os gorilas, afeta o sistema nervoso deles os deixando extremamente agressivos...\nE agora, o que acontecerá na missão? Será possível retomar a consciência deles a tempo? Você tem a missão de ajudá-los nisso!"
os.system('cls')

for i in texto:
    sys.stdout.flush()
    time.sleep(0.05)
    print(i, end="")
    if(kbhit()):
        sys.stdout.flush()
        os.system('cls')
        print(texto)
        break