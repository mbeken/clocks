from unittest.mock import Mock

import main


def test_clock_angle():
    name = 'test'
    data = {'hour': 9,'minute':45}
    req = Mock(get_json=Mock(return_value=data), args=data)

    # Call tested function
    assert main.calc(req) == 'Angle is {}!'.format(angle)


def test_print_hello_world():
    data = {}
    req = Mock(get_json=Mock(return_value=data), args=data)

    # Call tested function
    assert main.calc(req) == 'Angle is {}'.format(angle)
