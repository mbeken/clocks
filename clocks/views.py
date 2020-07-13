from django.http import HttpResponse

def calc_angle_view(request, data):
    result  = calc_angle(data)
    return HttpResponse(result)

def calc_angle(data):
    hour, minute = [int(i) for i in data.split(':')]
    if (minute < 0 or minute > 60):
        return "Minute should be in range of  0 to 59"
    if (hour < 0 or hour > 23):
        return "Invalid hour given"
    if hour in range(12, 25):
        hour = hour - 12

    CONST_PER_HOUR_DEGREE = 30
    CONST_PER_MIN_DEGREE = 6

    hour_angle = hour * CONST_PER_HOUR_DEGREE
    # To calculate total hour covered
    total_hour = hour_angle + (minute / 2)
    minute_angle = minute * CONST_PER_MIN_DEGREE
    angle = abs(total_hour - minute_angle)
    if angle > 180:
        angle = 360 - angle
    return "Angle for time is {} degree.".format(angle)


