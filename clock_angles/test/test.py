from clock_angles import main
import json


def test_positive():
    main.app.testing = True
    client = main.app.test_client()

    r = client.post("/clock_angles", json={'hour_hand': 13, 'minute_hand': 0})
    assert r.status_code == 200
    response_json = json.loads(r.data.decode('utf-8'))
    assert {'response': 30.0} == response_json


def test_negative():
    main.app.testing = True
    client = main.app.test_client()
    r = client.post("/clock_angles", json={'hour_hand': '1', 'minute_hand': 0})
    assert r.status_code == 400
    response_json = json.loads(r.data.decode('utf-8'))
    assert_json = {
        'response':
            {
                'error': 'Invalid arguments sent. Expected integer values between 0 and 24 for '
                         'hour and between 0 and 60 for minute...'
            }
    }

    assert assert_json == response_json


if __name__ == "__main__":
    import sys
    import os

    sys.path.append(os.path.dirname(os.getcwd()))