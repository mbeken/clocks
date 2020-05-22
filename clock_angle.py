#Code to Calculate the angle between the hour and min hand
#Assumption:- The data is overwritten into the file every 10 mins in "hh:mm" format e.g. 11.40
#The output file is appended in every run.
#The input filepath (file directory along with file name) is passed as first argument.
#The output filepath(file directory along with file name) is passed as second argument.
#The job can be scheduled in cron tab to run every 10 mins.

import sys
from sys import argv
def angle(hour,minute):
    try:
        if(hour < 0 or minute <0 or hour > 12 or minute >60):
            raise Exception("Wrong Input")
        angle_hour=(360/12)*(hour+(minute/60))
        #print(angle_hour)
        angle_minute=(360/60)*minute
        #print(angle_minute)
        angle=float(abs(angle_hour-angle_minute))
        #print("Angle is {} degree".format(angle))
        outputfile=sys.argv[2]  
        d=open(outputfile,"a")
        d.write("The time is {}:{} \n".format(hour,minute))
        d.write("Angle is {} degree \n".format(angle))
        d.close()
   
    except Exception:
        print("Please Enter valid Hour & Minute") 
inputfile=sys.argv[1]  
#print(file)
f=open(inputfile,"r")
lines=f.readlines()
#print(lines[0])
data = lines[0].split(':')
angle(int(data[0]), int(data[1]))
f.close()