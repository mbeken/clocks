from unittest.mock import Mock

import main


def test_clock_angle():
    main.app.testing = True
    client = main.app.test.test_client(3,0)
    
    r = client.get('/')
    assert r.status_code == 200
    assert '90' in r.data.decode('utf-8')
