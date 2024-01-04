class Ninja:
    def __init__(self, first_name, last_name, Pet, treats=10, pet_food=20):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet
        self.treats = treats
        self.pet_food = pet_food
        
        # return self
        
    def walk(self):
        Pet.play(self)
        return
        
    def feed(self):
        Pet.eat(self)
        self.pet_food -= self.pet_food
        return 
    
    def bathe(self):
        Pet.noise(self)
        
        
    
    
    
    
class Pet:

    def __init__(self, name, type, tricks, health = 80, energy = 75):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        
        # return self
        
# This function shoud add or subtract energy from your pet

    def change_health(health):
        # print('lets change the health')
        health += health 
        # print('health changed')
        
    def change_energy(energy):
        # print('lets change the energy')
        energy += energy 
        # print('energy changed')
        

    def sleep(self):
        print(f'{self.pet.name} energy went up by 25')
        Pet.change_energy(25)
    
    def eat(self):
        print(f'Feeding {self.pet.name} some tasty Mayweather, her energy went up by 5 points and health by 10 points')
        Pet.change_energy(5)
        Pet.change_health(10)
        
    def play(self):
        print(f'{self.pet.name} loves excercise, health went up by 5 points')
        Pet.change_health(5)
        
        
    def noise(self):
        print('RRRRRAAAAAAAAAAAWWWWWWWWWWRRRRRRR!!!!!!')



# precious = {'precious', 'tiger', 'attack'}
pet_precious = Pet('precious', 'tiger', 'attack')
# mike = {'Mike','Tyson', pet_precious,'steak','mayweather'}
ninja_mike = Ninja('Mike','Tyson', pet_precious)


# print(Ninja.pet.sleep())
# print(Ninja.walk('pet'))
ninja_mike.feed()
ninja_mike.walk()
ninja_mike.bathe()
# print(Ninja.bathe('pet'))
