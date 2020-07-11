def send_angle(time):
    try:
        hour, minutes = list(map(int, time.split(":")))
        if 24 > hour > 11:
            hour = abs(12 - hour)
        if 0 <= hour < 12 and 0 <= minutes <= 60:
            angle1, angle2 = find_hour_and_minute_angle(hour, minutes)
            angle = abs(angle1 - angle2) #Finding the difference between the angles from 0
            opp_angle = 360 - angle
            response = {"time": time, "angle": angle, "opposite_angle":opp_angle}
            return response
        else:
            response = {"err_msg": "Enter valid colon separated time string"}
            return (response)

    except ValueError:
        response = {"err_msg": "Enter valid colon separated time string"}
        return response

def find_hour_and_minute_angle(hour, minutes):
    '''
    This method returns the angle of hour's hand and minute's hand from the point at which there is 12 considering it as
    0 degree.
    '''
    hour_angle_add = 6 * minutes/12
    hour_angle = (hour*30) + hour_angle_add
    minute_angle = 6 * minutes
    return hour_angle, minute_angle