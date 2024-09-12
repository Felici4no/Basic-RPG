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



class User:
    def __init__(self, name, character_class):
        self.name = name  # Nome do jogador
        self.character_class = character_class  # Classe do personagem (guerreiro, mago, etc.)
        self.level = 1  # Nível inicial do jogador
        self.health = 100  # Vida inicial
        self.mana = 50  # Mana inicial
        self.experience = 0  # Experiência inicial
        self.inventory = []  # Inventário inicial (vazio)
        self.defense = 0  # Defesa inicial

    def level_up(self):
        """Método para aumentar o nível do jogador."""
        self.level += 1
        self.health += 20  # Aumenta a vida ao subir de nível
        self.mana += 10  # Aumenta a mana ao subir de nível


        print(f"{verde}{self.name} subiu para o nível {self.level}!{restaura_cor_original}")

    def take_damage(self, damage):
        """Método para o jogador receber dano, considerando a defesa."""
        net_damage = max(damage - self.defense, 0)  # Calcula o dano efetivo
        self.health -= net_damage
        if self.health <= 0:
            self.health = 0
            print(f"{vermelho}{self.name} foi derrotado.{restaura_cor_original}")
        else:
            print(f"{vermelho}{self.name} recebeu {net_damage} de dano e agora tem {self.health} de vida.{restaura_cor_original}")

    def use_mana(self, amount):
        """Método para o jogador usar mana."""
        if amount > self.mana:
            print(f"{vermelho}Mana insuficiente! {self.name} tem apenas {self.mana} de mana.{restaura_cor_original}")
        else:
            self.mana -= amount
            print(f"{amarelo}{self.name} usou {amount} de mana e agora tem {self.mana} de mana restante.{restaura_cor_original}")

    def add_to_inventory(self, item):
        """Método para adicionar itens ao inventário."""
        self.inventory.append(item)
        print(f"{verde}{item} foi adicionado ao inventário de {self.name}.{restaura_cor_original}")

    def show_inventory(self):
        """Método para mostrar os itens no inventário."""
        if self.inventory:
            print(f"Inventário de {self.name}: {', '.join(self.inventory)}")
        else:
            print(f"{vermelho}O inventário de {self.name} está vazio.{restaura_cor_original}")

    def gain_experience(self, amount):
        """Método para ganhar experiência."""
        self.experience += amount
        print(f"{verde}{self.name} ganhou {amount} de experiência.{restaura_cor_original}")
        if self.experience >= 100:
            self.level_up()
            self.experience = 0  # Reseta a experiência após subir de nível

