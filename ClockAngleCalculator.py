import argparse
import datetime


class ClockAngleCalculator:
    def clock_angle(self, time):
        try:
            hour = time.hour
            minutes = time.minute
            print("Hours in time provided " + str(hour))
            print("Minutes in time provided " + str(minutes))
            ans = abs((hour * 30 + minutes * 0.5) - (minutes * 6))
            return min(360 - ans, ans)
        except Exception as ex:
            raise Exception("Error while calculating the angle between hour and minute hands " + str(ex))

    def input_validation(self, input_time):
        time_format = "%H:%M:%S"
        try:
            time_input = datetime.datetime.strptime(input_time, time_format)
            print (type(time_input))
            print("Input Validation successful, Extracted time " + str(input_time))
            return time_input
        except Exception as e:
            raise Exception("Input validation failed, Please use specified format " + str(time_format) + " Exception raised " + str(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', help='Provide time', required=True)
    args = parser.parse_args()

    clock_angle_calc = ClockAngleCalculator()

    print("Validating the input time format passed in the argument")
    extracted_time = clock_angle_calc.input_validation(args.time)

    print("Starting to calculate angle between hour and minute hand")

    angle_result = clock_angle_calc.clock_angle(extracted_time)

    print('Angle between hour and minute hand: ' + str(angle_result))


# For deployment:
# We can use jenkins deployment pipeline to deploy this file on any machine.
# After deployment we need to execute the below command to execute this code
# python time_angle.py -t 03:45:22 (or any given time)
