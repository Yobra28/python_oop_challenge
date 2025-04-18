class PetAttribute:
    """Manages a single pet attribute with min/max bounds"""
    def __init__(self, value=5, min_value=0, max_value=10):
        self._value = value
        self.min = min_value
        self.max = max_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = max(self.min, min(self.max, new_value))

    def __str__(self):
        stars = '★' * self.value
        empty = '☆' * (self.max - self.value)
        return f"{stars}{empty} ({self.value}/{self.max})"


class AttributeManager:
    """Manages all pet attributes"""
    def __init__(self):
        self.hunger = PetAttribute(5)
        self.energy = PetAttribute(5)
        self.happiness = PetAttribute(5)

    def get_status_messages(self):
        """Generate status messages based on attribute values"""
        messages = []
        
        if self.hunger.value >= 8:
            messages.append("very hungry!")
        elif self.hunger.value <= 2:
            messages.append("full and satisfied.")

        if self.energy.value <= 2:
            messages.append("exhausted and needs sleep.")

        if self.happiness.value >= 8:
            messages.append("extremely happy!")
        elif self.happiness.value <= 2:
            messages.append("sad and bored.")
            
        return messages