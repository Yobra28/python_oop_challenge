from attributes import AttributeManager
from tricks import TrickManager


class Pet:
    """Main Pet class using composition"""
    def __init__(self, name):
        self.name = name
        self.attributes = AttributeManager()
        self.tricks = TrickManager()

    def eat(self):
        """Reduce hunger and slightly increase happiness"""
        self.attributes.hunger.value -= 3
        self.attributes.happiness.value += 1
        return f"{self.name} eats happily. Hunger decreases, happiness increases!"

    def sleep(self):
        """Restore energy"""
        self.attributes.energy.value += 5
        return f"{self.name} takes a nap. Energy restored!"

    def play(self):
        """Increase happiness at the cost of energy and hunger"""
        if self.attributes.energy.value >= 2:
            self.attributes.energy.value -= 2
            self.attributes.happiness.value += 2
            self.attributes.hunger.value += 1
            return f"{self.name} plays excitedly!"
        return f"{self.name} is too tired to play right now."

    def train(self, trick):
        """Teach the pet a new trick"""
        if self.tricks.add(trick):
            self.attributes.happiness.value += 1
            return f"{self.name} learned a new trick: {trick}!"
        return f"{self.name} already knows how to {trick}."

    def get_status(self):
        """Generate complete status report"""
        status = [
            f"\n{self.name}'s Status:",
            f"Hunger: {self.attributes.hunger}",
            f"Energy: {self.attributes.energy}",
            f"Happiness: {self.attributes.happiness}"
        ]
        
        for msg in self.attributes.get_status_messages():
            status.append(f"{self.name} is {msg}")
            
        return "\n".join(status)