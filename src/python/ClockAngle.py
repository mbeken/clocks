import base64

def clockAngle(time):
	timeArray=time.split(":")
	hours=int(timeArray[0])
	minutes=int(timeArray[1])

	if (hours < 0 or hours > 12 or minutes < 0 or minutes > 60):
	    return ('Invalid_Time_Input or Wrong_Value')
	if (hours == 12):
		hours = 0
	if (minutes == 60):
		minutes = 0
		hours += 1;
	if(hours>12):
		hours -= 12;
	hourAngle = (hours * 30)
	minuteAngle = (6 * minutes)
	offset = ((minutes/60)*30)
	correctedHourAngle = hourAngle + offset
	finalAngleValue = abs(correctedHourAngle - minuteAngle)
	finalAngleValue = min(360 - finalAngleValue, finalAngleValue)
	return finalAngleValue
def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    print(clockAngle(base64.b64decode(event['data']).decode('utf-8')))
