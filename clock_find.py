from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/clockangle/<int:hour>/<int:min>")
def calc_angle(hour,min):
    '''
    A function to calculate angle between hour and minute hand
     hour: Input given by user
     min: Input given by user

     Calculation:
      Each minute = (360/6) ==> 6 degree
      Each hour = (360/12) ==>30 degree
    '''

    if (min< 0 or min > 60):
        return "Minute should be in range of  0 to 59"
    if(hour <0 or hour>24):
        return "Invalid hour given"
    if hour in range(12,25):
        hour=hour-12

    CONST_PER_HOUR_DEGREE=30
    CONST_PER_MIN_DEGREE=6

    hour_angle = hour * CONST_PER_HOUR_DEGREE
    #To calculate total hour covered
    total_hour = hour_angle + (min/2)
    minute_angle= min * CONST_PER_MIN_DEGREE
    angle= abs(total_hour - minute_angle)
    if angle>180:
        angle=360 - angle
    return angle

if __name__ == "__main__":
    app.run()