from clock_angles import main
import json


def test_positive():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get("/clock_angles?time=13:0")
    assert r.status_code == 200
    response_json = json.loads(r.data.decode('utf-8'))
    assert {'response': 30.0} == response_json


def test_negative_out_of_bounds():
    main.app.testing = True
    client = main.app.test_client()
    r = client.get("/clock_angles?time=24:40")
    assert r.status_code == 400
    response_json = json.loads(r.data.decode('utf-8'))
    assert_json = {
        'response': {
            'error': r'query parameter time should follow regex '
                     r'^\d{1,2}:\d{1,2}$ and value should be between 00:00 and 23:59'
        }
    }
    assert assert_json == response_json


def test_negetive_invalid_input():
    main.app.testing = True
    client = main.app.test_client()
    r = client.get("/clock_angles?time=2A:40")
    assert r.status_code == 400
    response_json = json.loads(r.data.decode('utf-8'))
    assert_json = {
        'response': {
            'error': r'query parameter time should follow regex '
                     r'^\d{1,2}:\d{1,2}$ and value should be between 00:00 and 23:59'
        }
    }
    assert assert_json == response_json

