from flask import Flask, jsonify
import datetime
from constants import DEGREES_PER_HOUR, DEGREES_PER_MIN

app = Flask(__name__)

@app.route('/cal_angle/<string:time>', methods=['GET'])
def return_angle(time):
    """
    A function which takes time '03:00' as input and returns the clockwise angle between hands of clock as response
    To calculate angle, the method used is as follows
    Angle per hour = 30(360/12)
    Angle per min = 6(360/60)
    Angle covered by hour hand = 30 * hour
    Angle covered by minute hand = 6 * minute
    """
    if not check_valid_time(time):
        return jsonify({'response': 'The format for time is not valid, format should be of type "03:00"'})
    hour, minute = [int(i) for i in time.split(':')]
    # Converting hour to range to 1-12
    hour = (hour-12) if hour > 12 else hour
    # Per hour rotation is 30 degrees
    hour_hand_angle = hour * DEGREES_PER_HOUR if hour != 12 else 0
    # Per minute rotation is 6 degrees
    minute_hand_angle = minute * DEGREES_PER_MIN if minute != 60 else 0
    # Calculating final angle
    angle = abs(hour_hand_angle - minute_hand_angle)
    # Return as response
    return jsonify({'response': angle})


def check_valid_time(s):
    """
    To check the validity of the passed argument to return_angle function
    """
    try:
        datetime.datetime.strptime(s, "%H:%M")
        return True
    except Exception:
        return False



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)

