from flask import escape
def calc(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and ('hour' in request_json and 'minute' in request_json):
        hour = request_json['hour']
        minute = request_json['minute']
    else:
        hour = 12
        minute = 0
    if (hour < 0 or minute < 0 or hour > 12 or minute > 60):
        print('Wrong input')
    if (hour == 12):
        hour = 0
    if (minute == 60):
        minute = 0

    # Calculate the angles moved by
    # hour and minute hands with
    # reference to 12:00
    hour_angle = 0.5 * (hour * 60 + minute)
    minute_angle = 6 * minute

    # Find the difference between two angles
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle of two
    # possible angles
    angle = str(int(min(360 - angle, angle)))

    return 'Angle is {}'.format(escape(angle))
