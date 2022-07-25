
class Soild():
    """
    a base class for all soilds
    used to identify
    """

    def check(self):
        if self.health <= 0:
            return "dies"
