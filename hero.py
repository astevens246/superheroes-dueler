# hero.py
from ability import Ability
from armor import Armor

import random

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
    def __init__(self, name, starting_health=100):        
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []  # List to store abilities
        self.armors = []  # List to store armor objects
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
          # We use the append method to add ability objects to our list.
        self.armors.append(armor)
    
    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        if damage > defense:
            self.current_health -= (damage - defense)


    def fight(self, opponent):
        # Generate a random number (0 or 1) to determine the winner
        winner = random.randint(0, 1)

        if winner == 1:
            self.current_health -= random.randint(10, 20)  # Random damage between 10 and 20 to the hero
        else:
            opponent.current_health -= random.randint(10, 20)  # Random damage between 10 and 20 to the opponent

        if self.current_health <= 0:
            print(f"{opponent.name} wins!")
        elif opponent.current_health <= 0:
            print(f"{self.name} wins!")
        else:
            print(f"The battle between {self.name} and {opponent.name} continues!")
    def is_alive(self):
        return self.current_health > 0

    def fight(self, opponent):
        if not self.abilities or not opponent.abilities:
            print("Draw")
            return

        while self.is_alive() and opponent.is_alive():
            self_damage = self.attack()
            opponent.take_damage(self_damage)
            if not opponent.is_alive():
                print(f"{self.name} won!")
                return

        opponent_damage = opponent.attack()
        self.take_damage(opponent_damage)
        if not self.is_alive():
            print(f"{opponent.name} won!")
            return
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
    # Fight each hero until a victor emerges
'''while my_hero.current_health > 0 and opponent_hero.current_health > 0:
    my_hero.fight(opponent_hero)'''