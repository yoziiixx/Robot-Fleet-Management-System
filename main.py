from Battery import Battery
from DeliveryRobot import DeliveryRobot
from InspectionRobot import InspectionRobot
from Mission import Mission
from RobotFleet import RobotFleet


def main():
    robots = {}
    fleet = RobotFleet()

    while True:
        print("\n===== ROBOT FLEET MANAGEMENT =====")
        print("1. Add Robot")
        print("2. Show All Robots")
        print("3. Create Mission")
        print("4. Assign Mission")
        print("5. Perform Task")
        print("6. Recharge Robot")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            robot_id = input("Robot ID: ").strip()
            name = input("Robot name: ").strip()

            if not robot_id or not name:
                print("Robot ID and name cannot be empty!")
                continue

            if robot_id in robots:
                print("Robot already exists!")
                continue

            print("1. Delivery Robot")
            print("2. Inspection Robot")
            robot_type = input("Choose robot type: ")

            if robot_type not in ("1", "2"):
                print("Invalid robot type!")
                continue

            try:
                level = int(input("Battery level (0-100): "))

                if robot_type == "1":
                    weight = float(input("Maximum weight: "))
                    robot = DeliveryRobot(
                        robot_id, name, Battery(level), weight
                    )

                else:
                    camera = input("Camera resolution: ")
                    robot = InspectionRobot(
                        robot_id, name, Battery(level), camera
                    )

                if fleet.add_robot(robot):
                    robots[robot_id] = robot
                    print("Robot added successfully!")
                else:
                    print("Robot already exists!")

            except ValueError as error:
                print(f"Invalid input: {error}")

        elif choice == "2":
            if not robots:
                print("No robots available!")
            else:
                for robot in robots.values():
                    print(robot.show_info())

        elif choice == "3":
            mission_id = input("Mission ID: ").strip()
            description = input("Description: ").strip()

            if not mission_id or not description:
                print("Mission ID and description cannot be empty!")
                continue

            mission = Mission(mission_id, description)

            if fleet.create_mission(mission):
                print("Mission created successfully!")
            else:
                print("Mission already exists!")

        elif choice == "4":
            mission_id = input("Mission ID: ").strip()
            robot_id = input("Robot ID: ").strip()

            if fleet.assign_mission(mission_id, robot_id):
                print("Mission assigned successfully!")
            else:
                print("Assignment failed!")

        elif choice == "5":
            mission_id = input("Mission ID: ").strip()

            if fleet.execute_mission(mission_id):
                print("Mission completed successfully!")
            else:
                print("Mission failed!")

        elif choice == "6":
            robot_id = input("Robot ID: ").strip()

            if robot_id in robots:
                robots[robot_id].recharge()
                print("Robot recharged successfully!")
            else:
                print("Robot not found!")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()