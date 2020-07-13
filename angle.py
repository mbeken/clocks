import time
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/test_angle/<string:data>', methods=['GET'])
def find_angle(data):
    """
       PURPOSE: To convert the given time(00:00 to 23:59 format) in degree
       Return:  It reurn the angle in degree for given time
       Calulation:
                 For hour hand:
                 For hour hand in one hour=360/12
                 DEGREE_MOVEMENET_PER_HRS=30 degree movement
                 then, in one minute it covers:
                                   = 30/60
                                   = 0.5 degree movement
                 DEGREE_MOVEMENT_PER_MIN_FOR_HRS= 0.5 
                 For minute hand:
                 For minute hand in one minute= 360/60
                      DEGREE_MOVEMENET_FOR_MIN= 6 degree movement
                 Since, the hour hand and minute hand moving in same direction
                 so, actual movement is given by = 6-0.5
                        RELATIVE_MOVEMENT_DEGREE = 5.5
                                                 
    """

    # check for validation
    if validate_time(data):
        
        # split the given time in hrs, min
        hour, min = data.split(":")
        hour = 12 if int(hour) == 0 else int(hour)
        
        # To convert hour between 1 to 12
        hour = (int(hour)-12) if int(hour) > 12 else int(hour)
        min=int(min)

        DEGREE_MOVEMENET_PER_HRS=30
        DEGREE_MOVEMENT_PER_MIN_FOR_HRS=0.5
        DEGREE_MOVEMENET_FOR_MIN=6
        RELATIVE_MOVEMENT_DEGREE=5.5
        # Calculate the angle between two hands
        angle=abs(DEGREE_MOVEMENET_PER_HRS*hour-RELATIVE_MOVEMENT_DEGREE*min)
        
        return jsonify({'angle':angle})
    return jsonify({'angle':'Time is not in required format from 00:00 to 23:59'})
        

def validate_time(value):
    #
    """PURPOSE: To validate the input time is  between 00:00 to 23: 59 format
       RETURN :It return true if valid time format else return false
    """

    try:
        time.strptime(value, '%H:%M')
        return True
    except ValueError:
        return False



if __name__ == '__main__':
    app.run(debug=True)




