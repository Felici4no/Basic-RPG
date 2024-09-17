from models import *
from core.engine import *

'''
# Exemplo de uso da classe
player1 = User(name="Aragorn", character_class="Guerreiro")
player1.add_to_inventory("Espada Longa")
player1.gain_experience(120)
player1.take_damage(30)
player1.show_inventory()

#
# Criando instâncias dos itens
healing_potion = Potion("Poção de Cura", "Restaura 50 de vida", 10, 50)
sword = Weapon("Espada Longa", "Uma espada afiada que causa 15 de dano", 100, 15)
shield = Armor("Escudo de Madeira", "Oferece 5 de defesa", 50, 5)

# Criando um jogador para testar os itens
player = User(name="Aragorn", character_class="Guerreiro")

# Usando os itens
healing_potion.use(player)
sword.use(player)
shield.equip(player)
'''
#Inicio do game - nick e classe
name = nickname()
central_aguarda()
character_class = class_Selector()

#Cria o objeto
Main_Player = User(name, character_class)

#Add espada ao inventario
if Main_Player.character_class == "Maritmus":
    sword = Weapon("MaritmusSup", "Uma espada profunda que causa 15 de dano", 100, 15)
    Main_Player.add_to_inventory(sword.name)
elif Main_Player.character_class == "Flanejos":
    sword = Weapon("FlanejosRock", "Uma espada flanejante que causa 15 de dano", 100, 15)
    Main_Player.add_to_inventory(sword.name)
elif Main_Player.character_class == "Levitus":
    sword = Weapon("LevitusSky", "Uma espada flutuante que causa 15 de dano", 100, 15)
    Main_Player.add_to_inventory(sword.name)

central_aguarda()

Main_Player.gain_experience(10)
Main_Player.show_inventory()

central_aguarda()
pulalinha(5)


tutorial = question('Deseja iniciar o tutorial?')
if tutorial == True:
    print('Tutorial iniciado')
elif tutorial == False:
    print('Partindo direto para o game.')

central_aguarda()