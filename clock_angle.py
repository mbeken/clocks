if __name__ == "__main__":
    # function to find angle between two clock hands.
    def find_angle(hour, minute):
        if (hour < 0 or minute < 0 or hour > 12 or minute > 60):
            print('Wrong input')

        if (hour == 12):
            hour = 0

        if (minute == 60):
            minute = 0

        # hour hand angle
        hour_angle = (hour * 360) / 12 + (minute * 360) / (12 * 60)

        # minute hand angle
        minute_angle = (minute * 360) / (60)

        angle = abs(hour_angle - minute_angle)
        angle = min(360 - angle, angle)

        return angle

    hour_hand_val = int(input("Enter hour hand position: "))
    minute_hand_val = int(input("Enter minute hand position: "))

    print("Angle between two hands is: {}".format(find_angle(hour_hand_val,minute_hand_val)))
