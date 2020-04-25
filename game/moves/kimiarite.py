from game.transitions import Transition
from game.stats import Stat
from game.moves.move import Move

class Kimiarite(Move):
    category: Transition
    code: str

    def __init__(self, kimiarite_category: Transition, technique_name: str, kimiarite_code: str, primary: Stat, secondary: Stat):
        super(self, technique_name, primary, secondary)
        self.category = kimiarite_category
        self.code = kimiarite_code

