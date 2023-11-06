import random
from hero import Hero
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()


    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0   


    def view_all_heroes(self):
        """Print a list of all the team's heroes to the terminal."""
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)
    
    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self, health=100):
        '''Reset all heroes' health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    def attack(self, other_team):
        '''Battle each team against each other.'''
        living_heroes = list(self.heroes)  # Copy of your heroes
        living_opponents = list(other_team.heroes)  # Copy of opponent heroes

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # Step 1: Randomly select a living hero from each team
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            # Step 2: Have the heroes fight each other
            hero.fight(opponent)

            # Step 3: Update the list of living_heroes and living_opponents
            if not hero.is_alive():
                living_heroes.remove(hero)
                self.remove_hero(hero.name)  # Remove defeated hero from the team
                other_team.add_hero(hero)  # Add defeated hero to the opponent's team

            if not opponent.is_alive():
                living_opponents.remove(opponent)
                other_team.remove_hero(opponent.name)  # Remove defeated opponent from their team
                self.add_hero(opponent)  # Add defeated opponent to your team

    
# Create a team
my_team = Team("Avengers")

#Create instances of Heros
hero1 = Hero("Superman")
hero2 = Hero("Batman")

# Add heroes to the team (assuming you have Hero objects)
my_team.add_hero(hero1)
my_team.add_hero(hero2)

# View all heroes in the team
my_team.view_all_heroes()

