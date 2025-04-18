class TrickManager:
    """Manages pet tricks and training"""
    def __init__(self):
        self._tricks = []

    @property
    def tricks(self):
        return self._tricks.copy()

    def add(self, trick):
        """Add a new trick if not already known"""
        if trick.lower() not in [t.lower() for t in self._tricks]:
            self._tricks.append(trick)
            return True
        return False

    def list_tricks(self):
        """Return formatted string of all tricks"""
        if not self._tricks:
            return "No tricks learned yet."
        return "\n".join(f"{i+1}. {trick}" for i, trick in enumerate(self._tricks))