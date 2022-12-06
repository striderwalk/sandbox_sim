class Solid:
    """
    a base class for all solids
    used to identify
    """

    def __init__(self):
        self.type = "solid"

    def check_temp(self):
        is_max_temp = self.__class__.max_temp is not None
        if is_max_temp and self.temp > self.__class__.max_temp:
            return {"type": self.to_liquid()}

        if self.__class__.min_temp > self.temp:
            self.temp = self.__class__.min_temp

    def check(self):
        if self.health <= 0:
            return {"type": "dies"}
