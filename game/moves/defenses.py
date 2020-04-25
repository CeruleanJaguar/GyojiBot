from game.moves.move import Move
from game.transitions import Transition
from game.moves.kimiarite import Kimiarite
from game.stats import Stat
from typing import List

class Defense(Move):
    transitions: List[Transition]
    disallowed: Kimiarite

    def __init__(self, technique_name: str, primary: Stat, secondary: Stat, cannot_use_against: Kimiarite, transition1: Transition, transition2: Transition):
        super(technique_name, primary, secondary)
        self.transitions = [transition1, transition2]
        self.disallowed = cannot_use_against

