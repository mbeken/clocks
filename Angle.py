class Angle:
    
    def __init__(self, hr, mi):
        self.hr = hr
        self.mi = mi
        
    def calculateAngle(self):
        #calculate per minute degree
        self.perMinDegree = int(360/60)
        #degree for min input
        self.minAngle= int(self.perMinDegree * self.mi)
        #calculate per hour degree
        self.perHourDegree = int(360/12)
        #degree for hour input
        self.hourAngle = int(self.perHourDegree * self.hr)
        #convert mins to hour
        self.minsToHr = self.mi/60
        #degree for mins coverted to hr
        self.minsToHrAngle =  self.minsToHr * self.perHourDegree
        #total hour min angle
        self.hrMinAngleTotal = self.hourAngle + self.minsToHrAngle
        #differnece of hour and min angle
        self.angleBetweenHrMin = self.hrMinAngleTotal - self.minAngle
        return self.angleBetweenHrMin

#angle = Angle(3, 00)
#print(angle.calculateAngle())
#print(angle.angleBetweenHrMin)