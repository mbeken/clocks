#from google.cloud import pubsub_v1
from google.cloud import datastore
import datetime
import base64

client = datastore.Client('pravin-clock-exercise')


def getAngles(t):

    hh, mm = map(int, t.split(':'))

    # validate the input 
    if (hh < 0 or mm < 0 or hh > 24 or mm > 60): 
        print('The input for time value is Invalid') 

    if (hh >= 12): 
        hh = hh - 12
    if (mm == 60): 
        mm = 0

    # The minute hand moves 360 degree in 60 minute(or 6 degree in one minute) 
    # and hour hand moves 360 degree in 12 hours(or 0.5 degree in 1 minute). 
    # In h hours and m minutes, the minute hand would move (h*60 + m)*6 
    # and hour hand would move (h*60 + m)*0.5.

    hour_angle = 0.5 * (hh * 60 + mm)
    minute_angle = 6 * mm 

    # Find the difference between two angles
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle of two possible angles
    angle = min(360 - angle, angle) 

    return angle


def cf_get_angle(event, context):

    '''
    if context.event_type == 'google.pubsub.topic.publish':
        str_time = base64.b64decode(event['data']).decode('utf-8')
    else:
        str_time = event['data']
    '''
    str_time = event['data']
    angle = int(getAngles(str_time))
    result = f"Angle for time value {str_time} is {angle} degrees"
    print(result)

    key = client.key('ClockAngles')

    ds_table = datastore.Entity(
        key, exclude_from_indexes=['result'])

    ds_table.update({
        'created': datetime.datetime.utcnow(),
        'result': result,
        'input': str_time,
        'angle': angle
    })

    client.put(ds_table)
