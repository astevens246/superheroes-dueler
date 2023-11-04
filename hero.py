# hero.py
import random

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
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

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    opponent_hero = Hero("Opponent", 150) 
    # Fight each hero until a victor emerges
    while my_hero.current_health > 0 and opponent_hero.current_health > 0:
        my_hero.fight(opponent_hero)