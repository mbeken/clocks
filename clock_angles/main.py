import json

from flask import Flask, redirect, request, Response

app = Flask(__name__)


class Helpers:
    STATUS_OK = 200
    STATUS_BAD_REQUEST = 400
    STATUS_SERVER_ERROR = 500

    @staticmethod
    def standard_response(status, payload):
        json_data = json.dumps({
            'response': payload
        }, sort_keys=True, indent=4, separators=(',', ': '))
        resp = Response(json_data, status=status, mimetype='application/json')
        return resp

    @staticmethod
    def success(payload):
        return Helpers.standard_response(Helpers.STATUS_OK, payload)

    @staticmethod
    def error(status, error_info):
        return Helpers.standard_response(status, {
            'error': error_info
        })

    @staticmethod
    def bad_request(error_info):
        return Helpers.error(Helpers.STATUS_BAD_REQUEST, error_info)

    @staticmethod
    def validate_input(hour: int, minute: int):
        """
        Validates user input
        """
        if type(hour) != int or type(minute) != int:
            return False

        if 0 <= hour <= 24 and 0 <= minute <= 60:
            hour = hour % 12
            minute = minute % 60
            return hour, minute
        else:
            return False


@app.route('/')
def home():
    return redirect('/clock_angles')


@app.route('/clock_angles', methods=['GET', 'POST'])
def calculate_angles():
    """
    returns the angle between the hour hand and the minute hand

    Request to be sent should be POST and should have a json payload containing
    ifo on location of hour hand and minute hand
    """
    if request.method == 'GET':
        return Helpers.bad_request('GET request received. Expected POST with application/json body')

    else:
        request_data = request.get_json()
        result = Helpers.validate_input(request_data['hour_hand'], request_data['minute_hand'])
        if result:
            hour, minute = result

            hour_angle = 0.5 * (hour * 60 + minute)
            minute_angle = 6 * minute

            angle = abs(hour_angle - minute_angle)

            return Helpers.success(min(360 - angle, angle))
        else:
            return Helpers.bad_request("Invalid arguments sent. "
                                       "Expected integer values between 0 and 24 for hour and "
                                       "between 0 and 60 for minute...")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
