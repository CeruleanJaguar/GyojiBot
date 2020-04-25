from game.stats import Stat

class Move:
    name: str
    stats = []
    
    def __init__(self, technique_name: str, primary: Stat, secondary: Stat):
        self.name = technique_name
        self.stats = [primary, secondary]
