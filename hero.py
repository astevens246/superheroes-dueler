from ability import Ability
from armor import Armor
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0  # Add deaths property with default value 0
        self.kills = 0  # Add kills property with default value 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        if damage > defense:
            self.current_health -= (damage - defense)

    def is_alive(self):
        return self.current_health > 0

    def fight(self, opponent):
        if not self.abilities or not opponent.abilities:
            if not self.abilities and not opponent.abilities:
                print("Both heroes have no abilities. It's a draw!")
            elif not self.abilities:
                print(f"{self.name} has no abilities. {opponent.name} wins!")
                opponent.add_kill(1)
                self.add_death(1)
            else:
                print(f"{opponent.name} has no abilities. {self.name} wins!")
                self.add_kill(1)
                opponent.add_death(1)
            return

        rounds = 0
        while self.is_alive() and opponent.is_alive() and rounds < 100:
            self_damage = self.attack()
            opponent.take_damage(self_damage)
            if not opponent.is_alive():
                print(f"{self.name} won!")
                self.add_kill(1)  # Update kills for the winning hero
                opponent.add_death(1)  # Update deaths for the losing opponent
                return

            opponent_damage = opponent.attack()
            self.take_damage(opponent_damage)
            if not self.is_alive():
                print(f"{opponent.name} won!")
                self.add_death(1)  # Update deaths for the losing hero
                opponent.add_kill(1)  # Update kills for the winning opponent
                return

            rounds += 1

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)

    armor1 = Armor("Shield", 50)
    armor2 = Armor("Magic Robe", 30)

    hero1 = Hero("Wonder Woman")
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero1.add_armor(armor1)

    hero2 = Hero("Dumbledore")
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero2.add_armor(armor2)

    hero1.fight(hero2)
