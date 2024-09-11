from time import sleep

entrA = '<< '
saI = '>> '
def text_msg(nick, txt):
    if nick != '':
        print(f"{nick.title()}:")
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
            text_msg('Game', 'Nickname is invalid. Deve ter entre 4 e 20 caracteres.')
        else:
            text_msg('Game', f'Nickname is valid. Bem-vindo(a), {nick.title()}!')
            return nick.title()

# Seleção de Espada
def class_Selector():
    while True:
        text_msg('Game', 'Selecione uma espada:')
        text_msg('', '[1] MaritmusSup')
        text_msg('', '[2] FlanejosRock')
        text_msg('', '[3] LevitusSky')
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