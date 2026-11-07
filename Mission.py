class Mission:

    def __init__(self, mission_id: str, description: str):
        self.__mission_id = mission_id
        self.__description = description
        self.__status = "Pending"
        self.__robot_id = None

    # Getters
    def get_mission_id(self):
        return self.__mission_id

    def get_robot_id(self):
        return self.__robot_id

    def get_status(self):
        return self.__status

    # Setter
    def set_robot_id(self, robot_id):
        if self.__status == "Pending":
            if robot_id is None or (isinstance(robot_id, str) and robot_id.strip()):
                self.__robot_id = robot_id
                return True
        return False

    # Status transitions
    def start(self):
        if self.__status == "Pending" and self.__robot_id is not None:
            self.__status = "In Progress"
            return True
        return False

    def complete(self):
        if self.__status == "In Progress":
            self.__status = "Completed"
            return True
        return False

    # Display
    def show_info(self):
        result = {
            "mission_id": self.__mission_id,
            "robot_id": self.__robot_id,
            "status": self.__status,
            "description": self.__description
        }

        info = ""
        for key, value in result.items():
            info += f"{key}: {value}\n"

        return info