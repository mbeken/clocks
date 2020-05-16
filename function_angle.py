
def clock_angle(request):
    """
      {"hrs":"3","mins":"0"}
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

        angle = abs(hrs*degree_per_hour - mins*degree_per_min + mins*degree_intern)
        # Return the smaller angle of two  
        # possible angles 
        angle = min(360 - angle, angle) 
        ans_str = "Angle -> " + str(angle)

    else:
        ans_str = "Invalid Input, cannot compute, Try Again"
    return ans_str
