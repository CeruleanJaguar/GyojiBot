from game.transitions import Transition
from game.moves.move import Move
from game.stats import Stat


class Tachiai(Move):
    allowed_transitions = []

    def __init__(self,  technique_name: str, primary: Stat, secondary: Stat):
        super(self, technique_name, primary, secondary)


class Powerful(Tachiai):
    def __init__(self, primary: Stat, secondary: Stat):
        super(self, "Powerful Charge", primary, secondary)
        self.allowed_transitions = [Transition.POWER, Transition.WEIGHT]


class Reserved(Tachiai):
    def __init__(self, primary: Stat, secondary: Stat):
        super(self, "Reserved", primary, secondary)
        self.allowed_transitions = [Transition.FOOTWORK, Transition.SPIRIT]


class Low(Tachiai):
    def __init__(self, primary: Stat, secondary: Stat):
        super(self, "Low", primary, secondary)
        self.allowed_transitions = [Transition.POWER, Transition.SKILL]


class Surprise(Tachiai):
    def __init__(self, primary: Stat, secondary: Stat):
        super(self, "Surprise", primary, secondary)
        self.allowed_transitions = [Transition.WEIGHT, Transition.SPIRIT]


class Lateral(Tachiai):
    def __init__(self, primary: Stat, secondary: Stat):
        super(self, "Lateral", primary, secondary)
        self.allowed_transitions = [Transition.FOOTWORK, Transition.SKILL]
