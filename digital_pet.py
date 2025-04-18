# digital_pet.py
class Pet:
    def __init__(self, name):
        """Initialize a new pet with default attributes"""
        self.name = name
        self.hunger = 5  # Mid-range starting value
        self.energy = 5   # Mid-range starting value
        self.happiness = 5  # Mid-range starting value
        self.tricks = []  # List to store learned tricks
        
    def eat(self):
        """Reduce hunger and slightly increase happiness"""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} eats happily. Hunger decreases, happiness increases!")
        
    def sleep(self):
        """Restore energy"""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} takes a nap. Energy restored!")
        
    def play(self):
        """Increase happiness at the cost of energy and hunger"""
        if self.energy >= 2:  # Only play if there's enough energy
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} plays excitedly!")
        else:
            print(f"{self.name} is too tired to play right now.")
            
    def get_status(self):
        """Print the current state of the pet"""
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {'★' * self.hunger}{'☆' * (10 - self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'★' * self.energy}{'☆' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'★' * self.happiness}{'☆' * (10 - self.happiness)} ({self.happiness}/10)")
        
        # Status messages based on levels
        if self.hunger >= 8:
            print(f"{self.name} is very hungry!")
        elif self.hunger <= 2:
            print(f"{self.name} is full and satisfied.")
            
        if self.energy <= 2:
            print(f"{self.name} is exhausted and needs sleep.")
            
        if self.happiness >= 8:
            print(f"{self.name} is extremely happy!")
        elif self.happiness <= 2:
            print(f"{self.name} seems sad and bored.")
            
    # Bonus methods
    def train(self, trick):
        """Teach the pet a new trick"""
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)  # Learning makes pets happy
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}.")
            
    def show_tricks(self):
        """Display all learned tricks"""
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

# Create and interact with a pet
my_pet = Pet("Fluffy")
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.train("sit")
my_pet.train("roll over")
my_pet.train("fetch")
my_pet.show_tricks()
my_pet.get_status()