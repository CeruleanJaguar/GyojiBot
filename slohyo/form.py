from discord import User
from game.moves.defenses import Defense
from game.moves.kimiarite import Kimiarite
from game.moves.tachiai import Tachiai
from game.stats import Stat, Base_die
from typing import List

class Form():
    user: User
    opponent: User
    day: int = 0
    base_die: Base_die
    stats: List[Stat] = []
    tachiai: Tachiai
    
    win_kimiarite: Kimiarite
    win_use_focus = False
    win_use_fatigue = False

    power_counter: Defense
    weight_counter: Defense
    footwork_counter: Defense
    skill_counter: Defense
    spirit_counter: Defense
    defense_use_focus = False
    defense_use_fatigue = False

    counter_primary_kimiarite: Kimiarite
    counter_secondary_kimiarite: Kimiarite
    counter_use_focus = False
    counter_use_fatigue = False

    loop: int = 0
    matta_stategy: str = ""
    monoii_strategy: str = ""

