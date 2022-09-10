class Solid:
    """
    a base class for all solids
    used to identify
    """

    def __init__(self):
        self.type = "solid"


    def check_temp(self):
        if self.temp  > type(self).max_temp:
            return self.to_liquid()

    def check(self):
        if self.health <= 0:
            return "dies"


