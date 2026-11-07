from Battery import Battery
from Robot import Robot


class DeliveryRobot(Robot):

    def __init__(self, robot_id : str, name: str, battery : Battery, max_weight : int):
        super().__init__(robot_id, name, battery, "Available")
        self.set_max_weight(max_weight)

    # Actions
    def perform_task(self):
        return self.get_battery().consume(20)

    # Display
    def show_info(self):
        info = super().show_info()
        info += f"max_weight: {self.__max_weight}\n"
        return info

    # Getter & Setter
    def get_max_weight(self):
        return self.__max_weight

    def set_max_weight(self, max_weight):
        if max_weight >= 0:
            self.__max_weight = max_weight
        else:
            raise ValueError("Max weight must be positive")