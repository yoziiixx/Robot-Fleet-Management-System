from DeliveryRobot import DeliveryRobot
from Battery import Battery


def test_delivery_robot():
    robot1 = DeliveryRobot("R001", "Atlas", Battery(80), 25)

    assert robot1.perform_task() == True
    assert robot1.get_battery().get_level() == 60