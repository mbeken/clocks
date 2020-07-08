import sys
from sys import argv
def angle(hour,minute):
    try:
        if(hour < 0 or minute < 0 or hour > 12 or minute > 60):
            raise Exception("Wrong Input")
        angle_hour=(360/12)*(hour+(minute/60))
        angle_minute=(360/60)*minute
        angle=float(abs(angle_hour-angle_minute))
        outputfile=sys.argv[2]  
        d=open(outputfile,"a")
        d.write("Time = {}:{} \n".format(hour,minute))
        d.write("Angle = {} degree \n".format(angle))
        d.close()
   
    except Exception:
        print("Please Enter valid Hour & Minute") 
inputfile=sys.argv[1]  

f=open(inputfile,"r")
lines=f.readlines()

data = lines[0].split(':')
angle(int(data[0]), int(data[1]))
f.close()
