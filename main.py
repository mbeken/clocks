import base64


def angle(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    time = base64.b64decode(event["data"]).decode("utf-8")
    print(time)

    # Reading the time passed to the function
    timelist = time.split(':')
    hour = int(timelist[0])
    minute = int(timelist[1])

    try:
        # Check if the input is in range
        if hour < 0 or minute < 0 or hour > 12 or minute > 60:
            raise Exception

        if minute == 60:
            minute = 0

        # Calculate the angle between the hands of the clock
        angle_hr = 30 * hour + (1 / 2) * minute
        angle_mn = 6 * minute
        angle = abs(angle_hr - angle_mn)

        # Find out the smaller angle
        angle = min(angle, (360 - angle))
        print("the angle between the hands of the clock is " + str(angle))

    except Exception:
        print("wrong input, please enter in range")
