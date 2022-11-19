class Hero:
    def __init__(self,name , abiliti = 1):
        self.name = name
        self.abiliti = abiliti



class Super_hero(Hero):
    name = 'Султан2'
    def __str__(self):
        self.name = str
    def phrase(self):
        print(f'{self.name} it is super_hero ')




