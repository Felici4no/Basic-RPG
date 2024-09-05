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
        print(f"{self.name} subiu para o nível {self.level}!")

    def take_damage(self, damage):
        """Método para o jogador receber dano, considerando a defesa."""
        net_damage = max(damage - self.defense, 0)  # Calcula o dano efetivo
        self.health -= net_damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} foi derrotado.")
        else:
            print(f"{self.name} recebeu {net_damage} de dano e agora tem {self.health} de vida.")

    def use_mana(self, amount):
        """Método para o jogador usar mana."""
        if amount > self.mana:
            print(f"Mana insuficiente! {self.name} tem apenas {self.mana} de mana.")
        else:
            self.mana -= amount
            print(f"{self.name} usou {amount} de mana e agora tem {self.mana} de mana restante.")

    def add_to_inventory(self, item):
        """Método para adicionar itens ao inventário."""
        self.inventory.append(item)
        print(f"{item} foi adicionado ao inventário de {self.name}.")

    def show_inventory(self):
        """Método para mostrar os itens no inventário."""
        if self.inventory:
            print(f"Inventário de {self.name}: {', '.join(self.inventory)}")
        else:
            print(f"O inventário de {self.name} está vazio.")

    def gain_experience(self, amount):
        """Método para ganhar experiência."""
        self.experience += amount
        print(f"{self.name} ganhou {amount} de experiência.")
        if self.experience >= 100:
            self.level_up()
            self.experience = 0  # Reseta a experiência após subir de nível
