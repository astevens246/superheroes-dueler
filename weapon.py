import random

class Weapon:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        # Calculate the attack power range between half and the full max_damage value
        attack_power = self.max_damage // 2 + random.randint(0, self.max_damage // 2)
        return attack_power
