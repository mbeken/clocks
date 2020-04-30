"""
###########
    Author: Dheeraj Tingloo
    Created Date: 27-April-2020
    Use Case: Calculating angle between clock hands!
###########
"""
from flask import Flask, render_template, request, jsonify

APP = Flask(__name__)


@APP.route('/')
def index():
    """Calling default web page."""
    return render_template('index.html')


@APP.route('/cal_clock_angle')
def cal_clock_angle():
    """
        Getting arguments from user.
        Using abs() to make generalised formula.
        And return calculation back to web call in JSON format.
    """
    hrs = request.args.get('hrs', 0, type=str)
    mins = request.args.get('min', 0, type=str)

    # Input validation for hours and minutes.
    if 1 <= int(hrs) <= 12 and 0 <= int(mins) < 60:
        angle = float(abs(11 / 2 * int(mins) - 30 * int(hrs)))
    else:
        return jsonify(result="Error in input hours or minutes.")

    return jsonify(result=" {}:{} makes the following angle {}°".format(hrs, mins, angle))


if __name__ == "__main__":
    APP.run(host='0.0.0.0', debug=True)
