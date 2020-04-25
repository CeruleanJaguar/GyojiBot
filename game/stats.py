class Stat:
    name: str
    value: int


class Power(Stat):
    def __init__(self):
        self.name = "Power"
    

class Weight(Stat):
    def __init__(self):
        self.name = "Weight"


class Footwork(Stat):
    def __init__(self):
        self.name = "Footwork"


class Skill(Stat):
    def __init__(self):
        self.name = "Skill"


class Spirit(Stat):
    def __init__(self):
        self.name = "Spirit"

class Base_die:
    number_of_dice: int = 5
    die_faces: int = 20
