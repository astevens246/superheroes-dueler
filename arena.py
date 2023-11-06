from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

    def create_ability(self):
        name = input("What is the ability name? ")
        max_damage = int(input("What is the max damage of the ability? "))
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("Enter the weapon's name: ")
        max_damage = int(input("Enter the weapon's maximum damage: "))
        new_weapon = Weapon(name, max_damage)
        return new_weapon

    def create_armor(self):
        name = input("Enter the armor's name: ")
        max_block = int(input("Enter the armor's maximum block: "))
        new_armor = Armor(name, max_block)
        return new_armor

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                new_ability = self.create_ability()
                hero.add_ability(new_ability)
            elif add_item == "2":
                new_weapon = self.create_weapon()
                hero.add_weapon(new_weapon)
            elif add_item == "3":
                new_armor = self.create_armor()
                hero.add_armor(new_armor)
        return hero

    def build_team_one(self):
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for _ in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

  # Now implement build_team_two
  #HINT: If you get stuck, look at how build_team_one is implemented
    def build_team_two(self):
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for _ in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

def show_stats(self):
    '''Prints team statistics to terminal.'''
    # TODO: This method should print out battle statistics
    # including each team's average kill/death ratio.
    # Required Stats:
    #     Show surviving heroes.
    #     Declare winning team
    #     Show both teams' average kill/death ratio.
    # Loop through the heroes in Team One to calculate their statistics
    team_kills = 0
    team_deaths = 0
    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    
    # Handle the case where there are no deaths to avoid division by zero
    if team_deaths == 0:
        team_deaths = 1

    # Calculate and print Team One's average K/D ratio
    print(self.team_one.name + " statistics:")
    print(f"Surviving heroes from {self.team_one.name}:")
    for hero in self.team_one.heroes:
        if hero.is_alive():
            print(hero.name)
    print(f"Average K/D ratio for {self.team_one.name}: {team_kills/team_deaths}\n")

    # Loop through the heroes in Team Two to calculate their statistics
    team_kills = 0
    team_deaths = 0
    for hero in self.team_two.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths

    # Handle the case where there are no deaths to avoid division by zero
    if team_deaths == 0:
        team_deaths = 1

    # Calculate and print Team Two's average K/D ratio
    print(self.team_two.name + " statistics:")
    print(f"Surviving heroes from {self.team_two.name}:")
    for hero in self.team_two.heroes:
        if hero.is_alive():
            print(hero.name)
    print(f"Average K/D ratio for {self.team_two.name}: {team_kills/team_deaths}\n")

    # Declare the winning team based on the number of surviving heroes
    if self.team_one.num_alive() > self.team_two.num_alive():
        print(f"{self.team_one.name} is the winning team!")
    elif self.team_two.num_alive() > self.team_one.num_alive():
        print(f"{self.team_two.name} is the winning team!")
    else:
        print("It's a draw! Both teams have an equal number of surviving heroes.")

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()