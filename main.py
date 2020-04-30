"""
    _author_ = Arpit Rawal
    Funciton gets deploy on google cloud functions
"""
def clock_angle(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
    """
    request_json = request.get_json()
    request_args = request.args
    if request.args and 'hrs' in request.args:
        hrs = int(request.args.get('hrs'))
        mins = int(request.args.get('mins'))
    elif request_json and 'hrs' in request_json:
        hrs = int(request_json['hrs'])
        mins = int(request_json['mins'])
    elif request_args and 'hrs' in request_args:
        hrs = int(request_args['hrs'])
        mins = int(request_args['mins'])
    else:
        ans_str = "Cannot compute due to some error"

    if (0 <= int(hrs) <= 12 and 0 <= int(mins) <= 59):
        degree_per_min = 6
        degree_per_hour = 30
        degree_intern = 0.5

        if hrs == 12:
            hrs = 0

        angle_between = abs(hrs*degree_per_hour - mins*degree_per_min + mins*degree_intern)
        ans_str = "Angle between clock hands {0} hrs and {1} mins is {2}-> ".format(hrs,mins,str(angle_between))
        ans_str = "Angle -> " + str(angle_between)

    else:
        ans_str = "Invalid Input, cannot compute, Try Again"
    return ans_str
