
from Robot import Robot
from Mission import Mission


class RobotFleet:

    def __init__(self):
        self.__robots = {}
        self.__missions = {}

    # Add a robot
    def add_robot(self, robot: Robot):
        robot_id = robot.get_robot_id()

        if robot_id not in self.__robots:
            self.__robots[robot_id] = robot
            return True
        return False

    # Remove a robot
    def remove_robot(self, robot_id):
        if robot_id not in self.__robots:
            return False

        robot = self.__robots[robot_id]

        if robot.get_status() == "Busy":
            return False

        for mission in self.__missions.values():
            if (mission.get_robot_id() == robot_id
                    and mission.get_status() == "Pending"):
                mission.set_robot_id(None)

        del self.__robots[robot_id]
        return True

    # Show all robots
    def show_robots(self):
        if not self.__robots:
            print("No robots available")
            return

        for robot in self.__robots.values():
            print(robot.show_info())

    # Create a mission
    def create_mission(self, mission: Mission):
        mission_id = mission.get_mission_id()

        if mission_id not in self.__missions:
            self.__missions[mission_id] = mission
            return True
        return False

    # Assign a mission to a robot
    def assign_mission(self, mission_id, robot_id):
        if mission_id not in self.__missions:
            return False

        if robot_id not in self.__robots:
            return False

        mission = self.__missions[mission_id]
        robot = self.__robots[robot_id]

        if mission.get_status() != "Pending":
            return False

        if robot.get_status() != "Available":
            return False

        for other_mission in self.__missions.values():
            if (other_mission.get_robot_id() == robot_id
                    and other_mission.get_status() != "Completed"
                    and other_mission is not mission):
                return False

        return mission.set_robot_id(robot_id)

    # Execute a mission
    def execute_mission(self, mission_id):
        if mission_id not in self.__missions:
            return False

        mission = self.__missions[mission_id]
        robot_id = mission.get_robot_id()

        if mission.get_status() != "Pending":
            return False

        if robot_id not in self.__robots:
            return False

        robot = self.__robots[robot_id]

        if robot.get_status() != "Available":
            return False

        robot.set_status("Busy")

        try:
            success = robot.perform_task()

            if not success:
                return False

            if mission.start():
                return mission.complete()

            return False

        finally:
            robot.set_status("Available")

    # Show all missions
    def show_missions(self):
        if not self.__missions:
            print("No missions available")
            return

        for mission in self.__missions.values():
            print(mission.show_info())

    # Fleet statistics
    def fleet_statistics(self):
        total_robots = len(self.__robots)
        total_missions = len(self.__missions)

        completed = 0
        pending = 0
        in_progress = 0
        total_battery = 0

        for mission in self.__missions.values():
            if mission.get_status() == "Completed":
                completed += 1
            elif mission.get_status() == "Pending":
                pending += 1
            elif mission.get_status() == "In Progress":
                in_progress += 1

        for robot in self.__robots.values():
            total_battery += robot.get_battery().get_level()

        average_battery = (
            total_battery / total_robots
            if total_robots > 0 else 0
        )

        return {
            "total_robots": total_robots,
            "total_missions": total_missions,
            "completed": completed,
            "pending": pending,
            "in_progress": in_progress,
            "average_battery": round(average_battery, 2)
        }
