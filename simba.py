class Pet:
    def __init__(self):
        self.name = "Simba"
        self.hunger = 5  
        self.energy = 10  
        self.happiness = 5  
        self.tricks = []  
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has eaten and is feeling better!")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good nap and is feeling energized!")
    
    def play(self):
        if self.energy >= 2: 
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
     
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} had fun playing!")
        else:
            print(f"{self.name} is too tired to play!")
    
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
    
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} has learned to {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}!")
    
    def show_tricks(self):
        if self.tricks:
            print(f"\n{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet!")


def main():
    my_pet = Pet()
    my_pet.get_status()
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.train("sit")
    my_pet.train("roll over")
    my_pet.show_tricks()
    my_pet.get_status()

if __name__ == "__main__":
    main()
