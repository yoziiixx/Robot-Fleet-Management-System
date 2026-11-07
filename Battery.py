class Battery:

    # Represents a battery with a charge level between 0 and 100.
    def __init__(self, level : int = 100):
        if 0 <= level <= 100:
            self.__level = level
        else:
            raise ValueError("Invalid battery level")

    # Actions
    def consume(self, amount : int):
        if 0 < amount <= self.__level:
            self.__level -= amount
            return True
        else:
            return False

    def recharge(self):
        self.__level = 100

    # Getter
    def get_level(self):
        return self.__level