from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/clockangle/<string:data>", methods=['GET'])
def calc_angle(data):
    '''
    A function to calculate angle between hour and minute hand
     data : which contains hour and minute

     Calculation:
      Each minute = (360/6) ==> 6 degree
      Each hour = (360/12) ==>30 degree
    '''
    hour, minute = [int(i) for i in data.split(':')]
    if (minute< 0 or minute > 60):
        return "Minute should be in range of  0 to 59"
    if(hour <0 or hour>23):
        return "Invalid hour given"
    if hour in range(12,25):
        hour=hour-12

    CONST_PER_HOUR_DEGREE=30
    CONST_PER_MIN_DEGREE=6

    hour_angle = hour * CONST_PER_HOUR_DEGREE
    #To calculate total hour covered
    total_hour = hour_angle + (minute/2)
    minute_angle= minute * CONST_PER_MIN_DEGREE
    angle= abs(total_hour - minute_angle)
    if angle>180:
        angle=360 - angle
    return "Angle for time is {} degree.".format(angle)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)