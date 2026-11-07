from Robot import Robot
from Battery import Battery


def test_robot():
    robot = Robot("R001", "Atlas", Battery(80), "Available")

    # Test robot information
    assert robot.get_battery().get_level() == 80

    # Test battery recharge
    robot.get_battery().consume(30)
    robot.recharge()
    assert robot.get_battery().get_level() == 100

    # Test robot status
    robot.set_status("Busy")
    assert robot.get_status() == "Busy"

    # Test robot name
    robot.set_name("Atlas 2")
    assert robot.get_name() == "Atlas 2"