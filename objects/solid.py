
class Solid():
    """
    a base class for all solids
    used to identify
    """
    def __init__(self):
        self.type = "solid"

    def check(self):
        if self.health <= 0:
            return "dies"
