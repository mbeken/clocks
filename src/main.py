import base64


def compute_clock_angle(event, context):
    """ Calculate the angle between the clock hands
    Args:
        event (dict): Event payload.
    
    """
    # decode the event_load
    time = base64.b64decode(event["data"]).decode("utf-8")
    print(f"input data : {time}")

    # split the input time
    time_split = time.split(":")
    hour = int(time_split[0])
    minute = int(time_split[1])

    try:
        # Validate the input time range
        if hour < 0 or minute < 0 or hour > 12 or minute > 60:
            raise ValueError
        # Calculte hande between hour and minute hands
        # Angle of each hand respective 12 o'clock
        hour_angle = 30 * hour + 0.5 * minute
        minute_angle = 6 * minute
        angle = abs(hour_angle - minute_angle)

        # Finding out the smallest angle between the hands
        angle = min(angle, (360 - angle))
    except ValueError:
        print(f"Incorrect time range provided : {hour : minute}")
    except Exception:
        print(f"Exception raised in compute_clock_angle() with time = {time}")
    print(f"Angle between hande for time {time} : {angle} degree")
    # TODO
    # Load the data into the datastore for downstream processing
