from pet import Pet


class PetGame:
    """Handles the game interface and flow"""
    def __init__(self):
        self.pet = None

    def show_menu(self):
        """Display main menu options"""
        print("\nWhat would you like to do?")
        options = [
            "Feed your pet",
            "Play with your pet",
            "Put pet to sleep",
            "Teach a trick",
            "View tricks",
            "Check status",
            "Quit"
        ]
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

    def start(self):
        """Start the pet game"""
        print("Welcome to Digital Pet Simulator!")
        pet_name = input("What would you like to name your pet? ").strip()
        self.pet = Pet(pet_name)
        self.run()

    def run(self):
        """Main game loop"""
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-7): ").strip()
            
            actions = {
                '1': lambda: print(self.pet.eat()),
                '2': lambda: print(self.pet.play()),
                '3': lambda: print(self.pet.sleep()),
                '4': self._teach_trick,
                '5': lambda: print(self.pet.tricks.list_tricks()),
                '6': lambda: print(self.pet.get_status()),
                '7': lambda: (print("Goodbye!"), exit())
            }
            
            if choice in actions:
                actions[choice]()
            else:
                print("Invalid choice, please try again.")

    def _teach_trick(self):
        """Handle trick teaching interaction"""
        trick = input("What trick would you like to teach? ").strip()
        if trick:
            print(self.pet.train(trick))
        else:
            print("Please enter a valid trick name.")