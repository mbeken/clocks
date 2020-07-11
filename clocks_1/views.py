from django.http import HttpResponse
from clocks_1.clock_utils import send_angle
import json

def find_angle(request,time):
    try:
        response = send_angle(time)
    except ValueError:
        response = {"err_msg": "Enter valid colon separated time string"}

    return HttpResponse(json.dumps(response))

