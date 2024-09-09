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




Main_Player = User(name=nickname(), character_class=class_Selector())