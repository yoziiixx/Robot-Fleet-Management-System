from Robot import Robot
from Battery import Battery

class InspectionRobot(Robot):

    def __init__(self, robot_id : str, name: str, battery : Battery, camera_resolution : str):
        super().__init__(robot_id , name, battery, "Available")
        self.set_camera_resolution(camera_resolution)

    # Actions
    def perform_task(self):
        return self.get_battery().consume(15)

    # Display
    def show_info(self):
        info = super().show_info()
        info += f"camera_resolution: {self.__camera_resolution}\n"
        return info

    def get_camera_resolution(self):
        return self.__camera_resolution

    # Getter & Setter
    def set_camera_resolution(self, resolution):
        if isinstance(resolution, str) and resolution.strip():
            self.__camera_resolution = resolution
        else:
            raise ValueError("Invalid camera resolution")