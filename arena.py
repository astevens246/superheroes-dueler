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
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("Enter the armor's name: ")
        max_block = int(input("Enter the armor's maximum block: "))
        return Armor(name, max_block)

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

    def build_team_two(self):
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for _ in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        while self.team_one.num_alive() > 0 and self.team_two.num_alive() > 0:
            print("Before attacks:")
            print(f"Team One has {self.team_one.num_alive()} heroes alive.")
            print(f"Team Two has {self.team_two.num_alive()} heroes alive.")

            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)

            print("After attacks:")
            print(f"Team One has {self.team_one.num_alive()} heroes alive.")
            print(f"Team Two has {self.team_two.num_alive()} heroes alive.")

        # Check which team has surviving heroes
        if self.team_one.num_alive() > 0:
            print(f"{self.team_one.name} is the winning team!")
        elif self.team_two.num_alive() > 0:
            print(f"{self.team_two.name} is the winning team!")
        else:
            print("It's a draw! Both teams have no surviving heroes.")




    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # Calculate and display the average K/D for Team One
        self.display_average_kd(self.team_one)

        # Calculate and display the average K/D for Team Two
        self.display_average_kd(self.team_two)

        # Display heroes from Team One that survived
        self.display_surviving_heroes(self.team_one)

        # Display heroes from Team Two that survived
        self.display_surviving_heroes(self.team_two)

    def display_average_kd(self, team):
        team_kills = sum(hero.kills for hero in team.heroes)
        team_deaths = sum(hero.deaths for hero in team.heroes)

        if team_deaths == 0:
            team_deaths = 1

        print(team.name + " average K/D was: " + str(team_kills/team_deaths))

    def display_surviving_heroes(self, team):
        for hero in team.heroes:
            if hero.is_alive():
                print("Survived from " + team.name + ": " + hero.name)

if __name__ == "__main__":
    game_is_running = True
    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
