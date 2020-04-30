from flask import escape

def clock_angle_between_hands_m(request):
    """
    Function to calculate angle between 2 hands of clock.
    Deployed on Gcloud as cloud function.
    responds to all http request.

    deployed url: https://us-central1-ind-coe.cloudfunctions.net/clock_angle_between_hands_m?h=06&m=00

    Argument: request (flask.Request): HTTP request object.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_args and 'h' in request_args:
         h = int(request_args['h'])
         m = int(request_args['m'])
    elif request_json and 'h' in request_json:
        h = int(request_json['h'])
        m = int(request_json['m'])

    else:
        out_string = "Wrong input. Time should be entered in 12-hour format. eg ?h=06&m=00"

    if (0 <= int(h) <= 12 and 0 <= int(m) <= 60):
        if (h == 12):
            h = 0
        if (m == 60):
            m = 0
        hour_angle = 0.5 * (h * 60 + m)
        minute_angle = 6 * m

        angle = abs(hour_angle - minute_angle)
        angle = min(360 - angle, angle)   # returns minimum of 2 side of angle

        out_string = "Angle between hour hand & minute hand is : " + str(angle) +" degrees."
    else:
        out_string = "Wrong input. Time should be entered in 12-hour format. eg ?h=06&m=00"
    return out_string