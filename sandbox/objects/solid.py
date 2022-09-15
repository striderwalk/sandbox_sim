class Solid:
    """
    a base class for all solids
    used to identify
    """

    def __init__(self):
        self.type = "solid"


    def check_temp(self):
        is_max_temp = type(self).max_temp is not None
        if is_max_temp and self.temp > type(self).max_temp:
            return {"type" : self.to_liquid()}

    def check(self):
        if self.health <= 0:
            return {"type" : "dies"}


