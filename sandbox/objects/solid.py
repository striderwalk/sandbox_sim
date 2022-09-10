class Solid:
    """
    a base class for all solids
    used to identify
    """

    def __init__(self):
        self.type = "solid"


    def check_temp(self):
        if self.temp  > type(self).max_temp:
            return {"type" : self.to_liquid(), "temp" : self.temp}

    def check(self):
        if self.health <= 0:
            return "dies"


