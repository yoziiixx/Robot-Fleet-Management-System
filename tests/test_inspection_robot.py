from Battery import Battery
from InspectionRobot import InspectionRobot


def test_inspection_robot():
    robot2 = InspectionRobot("R002", "Scout", Battery(60), "4K")

    assert robot2.perform_task() == True
    assert robot2.get_battery().get_level() == 45