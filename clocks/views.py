import json

from django.http import HttpResponse
from clocks.constants import HOUR_HAND_ANGLE, MINUTE_HAND_ANGLE


def clock_hand_angle(request, time, *args, **kwargs):
    """
    This method will calculate and return clock face angle.
    :param request: django request object.
    :param time: time string object in the for "HH:MM"
    :return: JsonResponse object
    """
    response = {"data": {}}
    status = 200
    try:
        t_lst = time.split(":")
        if all([len(t_lst) == 2, t_lst[0].isdigit() and t_lst[1].isdigit()]):
            hrs = 0 if int(t_lst[0]) == 12 else int(t_lst[0])
            mins = 0 if int(t_lst[1]) == 60 else int(t_lst[1])
            if 0 <= hrs <= 12 and 0 <= mins <= 60:
                h_angle = HOUR_HAND_ANGLE * (hrs * 60 + mins)
                m_angle = MINUTE_HAND_ANGLE * mins
                angle = abs(h_angle - m_angle)
                angle = min(360 - angle, angle)
                response["data"] = {"time": time, "angle": angle}
            else:
                status = 400  # Bad request
                response["data"] = {"message": "Invalid time format. Please input time in 12 hours clock format."}
        else:
            status = 400  # Bad request
            response["data"] = {"message": "Invalid time format. It should be in 'HH:MM' format."}
    except Exception as e:
        status = 500
        print(e.__str__())
        response["data"] = {"message": "Internal Server Error"}
    return HttpResponse(json.dumps(response), status=status, content_type="application/json")
