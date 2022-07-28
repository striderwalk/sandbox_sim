
class Solid():
    """
    a base class for all soilds
    used to identify
    """
    def __init__(self):
        self.type = "soild"

    def check(self):
        if self.health <= 0:
            return "dies"
