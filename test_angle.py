import pytest

from main import app as main_app


def test_root_page():
    response = main_app.test_client().get('/')
    assert response.status_code == 200

def test_result_data_success():
    data = {
        'hour': 3,
        'minute': 0
    }
    response = main_app.test_client().post('/result', data=data)
    assert '90.0' in str(response.data)




