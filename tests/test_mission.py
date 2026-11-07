from Mission import Mission


def test_mission():
    mission1 = Mission("M001", "Deliver package")

    assert mission1.start() == False
    assert mission1.set_robot_id("R001") == True
    assert mission1.start() == True
    assert mission1.complete() == True