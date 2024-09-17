from time import sleep

#Cores
# Cores de texto
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'

# Estilos
restaura_cor_original = '\033[0;0m'  # Restaura a cor original
negrito = '\033[1m'                  # Negrito
reverso = '\033[2m'                  # Reverso (inverte cor de texto e fundo)

# Cores de fundo
fundo_preto = '\033[40m'
fundo_vermelho = '\033[41m'
fundo_verde = '\033[42m'
fundo_amarelo = '\033[43m'
fundo_azul = '\033[44m'
fundo_magenta = '\033[45m'
fundo_ciano = '\033[46m'
fundo_branco = '\033[47m'

#Felici4no
print(f"{negrito}By {vermelho}F{verde}e{amarelo}l{azul}i{magenta}c{preto}i{vermelho}4{ciano}n{verde}o  {restaura_cor_original}")

def mudar_cor(texto, cor=branco, estilo=restaura_cor_original, fundo=restaura_cor_original):

    print(f"{estilo}{cor}{fundo}{texto}{restaura_cor_original}")

# Exemplo de uso
##

entrA = '<< '
saI = '>> '
def text_msg(nick, txt):
    if nick != '':
        print(negrito)
        print(f"{nick.title()}:")
        print(restaura_cor_original)
    print(f"- {txt}")
# Erro
def typeErro(func):  # Usado em funções como última condicional
    print(f"!! Erro !! \n - function {func}")

def sOrN():
    # Simplificada para apenas 's/n' sem verificação de 'rtype'
    while True:
        r = input('- s/n:\n>> ').upper()
        if r == 'N' or r == 'S':
            print(f'_{r}')
            return r
        else:
            print('\nResposta Inválida. Por favor, digite "S" ou "N".')

# Definição de Nickname
def nickname():
    while True:
        nick = input('Nickname: ')
        if nick == '':
            text_msg('Game', 'Nickname is empty')
        elif len(nick) < 4 or len(nick) > 20:
            text_msg('Game', f'Nickname is {vermelho}invalid{restaura_cor_original}. Deve ter entre 4 e 20 caracteres.')
        else:
            text_msg('Game', f'Nickname is {verde}valid{restaura_cor_original}. Bem-vindo(a),{ciano}{nick.title()}{restaura_cor_original}!')
            return nick.title()

# Seleção de Espada
def class_Selector():
    while True:
        print(negrito)
        print('Selecione uma espada:')
        print(ciano)
        print('- [1] MaritmusSup\n- [2] FlanejosRock\n- [3] LevitusSky')
        print(restaura_cor_original)

        r = input(entrA)
        if r in ['1', '2', '3']:
            if r == '1':
                text_msg('Game', f'Espada MaritmusSup escolhida')
                return 'Maritmus'
            elif r == '2':
                text_msg('Game', f'Espada FlanejosRock escolhida')
                return 'Flanejos'
            elif r == '3':
                text_msg('Game', f'Espada LevitusSky escolhida')

                return 'Levitus'

        else:
            text_msg('Game', 'Entrada inválida, tente novamente.\n')

def timePradonizador(padrao):
    while True:
        if padrao == 1:
            sleep(0.3)
            return padrao
        elif padrao == 2:
            sleep(0.5)
            return padrao
        elif padrao == 3:
            sleep(1)
            return padrao
        else:
            sleep(padrao)
            return padrao

def divisor_de_tela(divisor,linhas,colunas):
    if colunas == 'c':
        for i in range(linhas):
            print(divisor * i)
            timePradonizador(0.1)
    else:
        for i in range(linhas):
            print(divisor * colunas)
            timePradonizador(0.1)

    print('\n')

def pulalinha(x):
    for i in range(x):
        print('\n')

def aguarda():
    r = input(entrA +'(press enter)')

def central_aguarda():
    pulalinha(2)
    aguarda()
    print('//')
    pulalinha(3)

def question(Questao):
    while True:
        print(negrito,'\n -',Questao,restaura_cor_original)
        r = input('y / n ?\n')
        if r == 'y' or r == 'Y':
            return True
        elif r == 'n' or r == 'N':
            return False
        else:
            pulalinha(3)
            print('Respostas Inválida')

def startutorial():
    print(negrito,'O jogo é um modo história',negrito,restaura_cor_original)