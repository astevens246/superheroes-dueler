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

