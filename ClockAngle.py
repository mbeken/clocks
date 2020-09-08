import sys
import logging
import argparse


def calc_angle(hour, minute):
    """
    argument: hour - The hour value of the time
    argument: minute - The minute value of the time
    output: The angle between the hands of the clock in degrees
    """
    # validate the input
    try:
        if hour < 0 or minute < 0 or hour > 24 or minute > 60:
            logging.error('Wrong input')
            return -1

        # if minute is 60 we do not need to calculate the angle for the minute hand as it is a new hour
        if minute == 60:
            minute = 0
            hour += 1

        # if the hour is 12 , we do not need to calculate the angle for the hour hand
        if hour >= 12:
            hour = hour - 12

        # Calculate the angles moved by hour and minute hands with
        hour_angle = 0.5 * (hour * 60 + minute)
        minute_angle = 6 * minute

        # Find the difference between two angles
        angle = abs(hour_angle - minute_angle)

        # Return the smaller angle of two
        angle = min(360 - angle, angle)

        return angle

    except Exception as exception:
        logging.error(exception)
        raise exception


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # add arguments to the parser
    parser.add_argument('--time', type=str, help='the time value which comprises hour and minute')

    # parse the arguments
    args = parser.parse_args()

    # get the arguments value
    hour, minute = args.time.split(':')
    hour = int(hour.strip())
    minute = int(minute.strip())
    print('Angle between hour ' + str(hour) + ' and minute ' + str(minute) + ' is :', calc_angle(hour, minute))
