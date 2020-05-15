class Clock_Angle:
    def __init__(self, hour, minutes):
        self.hour= int(hour)
        self.minutes= int(minutes)

    def calAngle(self):
        #hour angle position
        h = (self.hour * 360) / 12 + (self.minutes * 360) / (12 * 60)
        
        #minute angle position
        m = (self.minutes * 360) / (60)        
        angle = abs(h - m)
        
        if angle > 180:
            angle = 360 - angle

        return angle
    
    def checkValues(self):
        result=""
        if (0 <= self.hour <= 12 and 0 <= self.minutes <= 59):
            result = self.calAngle()
        else:
            result = "Incorrect hour and minutes value"
        return result        
