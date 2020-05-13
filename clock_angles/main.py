from flask import Flask, redirect, request
from lib.helpers import Helpers, DatastoreClient


app = Flask(__name__)


@app.route('/')
def home():
    return redirect('/clock_angles')


@app.route('/clock_angles', methods=['GET'])
def calculate_angles():
    """
    returns the angle between the hour hand and the minute hand

    Request to be sent should be POST and should have a json payload containing
    ifo on location of hour hand and minute hand
    """
    time = request.args.get('time')

    result = Helpers.validate_and_parse_input(time)
    if result:
        hour, minute = result

        hour_angle = 0.5 * (hour * 60 + minute)
        minute_angle = 6 * minute

        angle = abs(hour_angle - minute_angle)
        angle = min(360 - angle, angle)
        DatastoreClient(kind='clock_angle_logs').log_to_datastore(time, angle)

        return Helpers.success(angle)
    else:
        return Helpers.bad_request(r"query parameter time should follow regex ^\d{1,2}:\d{1,2}$ and value should be "
                                   r"between 00:00 and 23:59")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
