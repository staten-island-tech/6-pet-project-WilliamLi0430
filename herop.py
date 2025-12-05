class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item ["title"])
        print(self.inventory)

jonuc = Hero("Jonuc", 100, ["Axe"])
jonuc.buy({"title": "Healing Vial", "heal": 50})
print(jonuc.__dict__)