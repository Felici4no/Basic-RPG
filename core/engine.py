def text_msg(nick,txt):
    if nick != '':
        print(nick.title(),'said:')
    print(f'- {txt}')

def typeErro(func): # Usado em funções como ultima condicional
    print(f'!! Erro !! \n - function {func}  ')
def sOrN(rtype):
    if rtype == 's/n':
        while True:
            r = input('- s/n:\n>> ')
            if r.upper() == 'N' or r.upper() == 'S':
                print(f'_{r}')
                return r
            else:
                print('\n\n\nResposta Invalida')
    else:
        typeErro('freeAndSorN')

#sOrN('s/n')

##Definição de personagem

#Definição de Nickname
def nickname():
    while True:
        nick = input('Nickname: ');
        if nick == '':
            text_msg('Game', 'Nickname is empty')
        elif len(nick) < 4 or len(nick) > 20:
            text_msg('Game', 'Nickname is invalid')
        else:
            text_msg('Game', f'Nickname is valid, \n- Welcome {nick.title()}')
            return nick.title()

def class_Selector():
    while True:
        text_msg('Game', 'Select a sword:')
        text_msg('','[1] Espada 1 ')
        text_msg('','[2] Espada 2 ')
        text_msg('','[3] Espada 3 ')
        r = input('<< ')
        if r == '1':
            text_msg('Game','espada 1')
            return r
        elif r == '2':
            text_msg('Game','espada 2')
            return r
        elif r == '3':
            text_msg('Game','espada 3')
            return r
        else:
            text_msg('Game', 'Invalid input')
