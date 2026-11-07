from Battery import Battery


def test_battery():
    battery1 = Battery(80)

    assert battery1.consume(20) == True
    assert battery1.get_level() == 60

    battery1.recharge()
    assert battery1.get_level() == 100