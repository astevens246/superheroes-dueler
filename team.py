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
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / max(1, hero.deaths)  # Avoid division by zero
            print(f"{hero.name} Kill/Deaths: {kd}")

    def revive_heroes(self, health=100):
        '''Reset all heroes' health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        living_heroes = list(self.heroes)
        living_opponents = list(other_team.heroes)

        max_rounds = 100  # Add max_rounds variable

        rounds = 0  # Initialize rounds counter

        while len(living_heroes) > 0 and len(living_opponents) > 0 and rounds < max_rounds:
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

            rounds += 1  # Increment rounds counter

    def num_alive(self):
        """Return the number of heroes alive on the team."""
        alive_heroes = [hero for hero in self.heroes if hero.is_alive()]
        return len(alive_heroes)

# Create teams
team1 = Team("Avengers")
team2 = Team("Justice League")

# Create instances of Heroes
hero1 = Hero("Superman")
hero2 = Hero("Batman")
hero3 = Hero("Wonder Woman")
hero4 = Hero("The Flash")

# Add heroes to the teams (assuming you have Hero objects)
team1.add_hero(hero1)
team1.add_hero(hero2)

team2.add_hero(hero3)
team2.add_hero(hero4)

# View all heroes in each team
print("Team 1:")
team1.view_all_heroes()

print("\nTeam 2:")
team2.view_all_heroes()

# Attack one team against another
team1.attack(team2)

# View stats for each team
print("\nTeam 1 Stats:")
team1.stats()

print("\nTeam 2 Stats:")
team2.stats()
