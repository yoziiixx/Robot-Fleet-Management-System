from Battery import Battery


class Robot:

    # Represents a robot with an ID, a name, a battery and a status.
    def __init__(self, robot_id : str, name: str, battery : Battery, status : str):
        self.__robot_id = robot_id
        self.__name = name
        self.__battery = battery
        self.__status = status

    # Display
    def show_info(self):
        result = {
            'robot_id' : self.__robot_id,
            'name' : self.__name,
            'battery' : self.__battery.get_level(),
            'status' : self.__status
        }

        info = ""
        for key, value in result.items():
            info += f'{key}: {value}\n'

        return info

    # Actions
    def recharge(self):
        self.__battery.recharge()

    def perform_task(self):
        raise NotImplementedError("Subclasses must implement perform_task()")

    # Getters & Setters
    def get_robot_id(self):
        return self.__robot_id


    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_battery(self):
        return self.__battery

    def get_status(self):
        return self.__status

    def set_status(self, status):
        if status in ("Available", "Busy"):
            self.__status = status
            return True
        else:
            return False




