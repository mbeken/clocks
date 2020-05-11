from flask import Flask, jsonify
import time

app = Flask(__name__)


@app.route('/clock_angle/<string:data>', methods=['GET'])
def get_clock_angle(data):
    if is_valid_time(data):
        return jsonify(context="Angle for time {} is {} degree.".format(data, cal_culculate_angle(data)))

    return jsonify(context="Please enter the valid format i.e. This time function will accept time b/w 00:00 To 23:59.")


def is_valid_time(value):
    """ This time function will accept time b/w 00:00 to 23:59"""

    try:
        time.strptime(value, '%H:%M')
        return True
    except ValueError:
        return False


def cal_culculate_angle(data):
    """Explanation:
            Hour Calculation :
            ------------------
                A analog clock is divided up into 12 sectors, based on the numbers 1–12. One sector represents
                30 degrees (360/12 = 30).
                so 1 hour = 30 degree
                one minute = 0.5 degree

            Min Calculation :
            -----------------
             a clock represent 360 degree so
             1 min = 360 /60 = 6 degree
     """

    CONST_PER_HOUR_DEGREE = 30
    CONST_PER_MIN_DEGREE = 0.5
    CONST_PER_MIN_DEG_FOR_MIN = 6

    _hour, _min = data.split(":")
    _hour = 12 if int(_hour) == 0 else int(_hour)
    _min = int(_min)

    if int(_hour) > 12:
        _hour = int(_hour) - 12

    # Position of Hour
    h = _hour * CONST_PER_HOUR_DEGREE + _min * CONST_PER_MIN_DEGREE
    # Position of Min
    m = _min * CONST_PER_MIN_DEG_FOR_MIN

    return abs(h - m)


if __name__ == '__main__':
    app.run(debug=True)
