from .rules import temp_rules

class Solid:
    """
    a base class for all solids
    used to identify
    """

    def __init__(self):
        self.type = "solid"


    def check_temp(self):
        if self.temp  > temp_rules["solid"]["max"]:
            return self.to_liquid()

    def check(self):
        if self.health <= 0:
            return "dies"


