class Item:
    def __init__(self, name, item_type, description, value):
        self.name = name  # Nome do item
        self.item_type = item_type  # Tipo do item (ex: 'Arma', 'Armadura', 'Poção')
        self.description = description  # Descrição do item
        self.value = value  # Valor do item (pode ser o preço ou o valor em ouro)

    def use(self, target):
        """Método para usar o item. Deve ser implementado nas subclasses."""
        raise NotImplementedError("Este item não pode ser usado diretamente.")

    def __str__(self):
        return f"{self.name} ({self.item_type}): {self.description} - Valor: {self.value} moedas de ouro"


# Subclasse para uma Poção
class Potion(Item):
    def __init__(self, name, description, value, healing_amount):
        super().__init__(name, "Poção", description, value)
        self.healing_amount = healing_amount  # Quantidade de vida restaurada pela poção

    def use(self, target):
        """Método para usar a poção em um alvo (por exemplo, o jogador)."""
        target.health += self.healing_amount
        print(f"{target.name} usou {self.name} e recuperou {self.healing_amount} de vida.")
        if target.health > 100:
            target.health = 100  # Garantir que a vida não exceda o máximo


# Subclasse para uma Arma
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        super().__init__(name, "Arma", description, value)
        self.damage = damage  # Dano causado pela arma

    def use(self, target):
        """Método para atacar um alvo com a arma."""
        target.take_damage(self.damage)
        print(f"{target.name} foi atacado com {self.name} e sofreu {self.damage} de dano.")


# Subclasse para uma Armadura
class Armor(Item):
    def __init__(self, name, description, value, defense):
        super().__init__(name, "Armadura", description, value)
        self.defense = defense  # Defesa oferecida pela armadura

    def equip(self, target):
        """Método para equipar a armadura em um alvo."""
        target.defense += self.defense
        print(f"{target.name} equipou {self.name} e ganhou {self.defense} de defesa.")
