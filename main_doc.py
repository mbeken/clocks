import argparse
import logging
import time, sys, os, subprocess
from datetime import date
import datetime


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

"Adding Logger"
handler = logging.FileHandler('/home/mangeshsoni82/deploy/clock/GetAngleFromClock' + str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.log', mode='w')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

output_handler = logging.StreamHandler(sys.stdout)
output_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - [%(filename)s:%(lineno)d] - %(message)s')
output_handler.setFormatter(formatter)

logger.addHandler(output_handler)



# Function to Calculate angle b/w  
# hour hand and minute hand  
def calcAngle(h,m): 
          
        # validate the input 
        if (h < 0 or m < 0 or h > 12 or m > 60): 
            print('Wrong input') 
          
        if (h == 12): 
            h = 0
        if (m == 60): 
            m = 0
          
        # Calculate the angles moved by  
        # hour and minute hands with  
        # reference to 12:00 
        hour_angle = 0.5 * (h * 60 + m) 
        minute_angle = 6 * m 
          
        # Find the difference between two angles 
        angle = abs(hour_angle - minute_angle) 
          
        # Return the smaller angle of two  
        # possible angles 
        angle = min(360 - angle, angle) 
          
        return angle




def trigger_function(hour_hand):
    """h = input("ebter the hour clock")  #9
    m = input("enter the minute clock") #60"""
    hour_hand,minute_hand=hour_hand.split(":")
    hour_hand,minute_hand= int(hour_hand), int(minute_hand)
    
    try:
        logger.info("Function to Calculate angle b/w  hour hand is %s and minute hand is %s " %(hour_hand, minute_hand))
        Angle = calcAngle(int(hour_hand) , int(minute_hand))
        print('Angle ', calcAngle(int(hour_hand) , int(minute_hand))) 
        logger.info("Angle is %s b/w  hour hand is %s and minute hand is %s " %(Angle , hour_hand, minute_hand))
    except Exception as e:
        logger.info("Error in calculating the Angle \n" + str(e) + "\n" )
    
    return Angle
                
    
    logger.info("Calculation completed : {}".format(datetime.datetime.now()))
    
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
           description=__doc__,
           formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
           'hour_hand', help='',default=12)
#    parser.add_argument(
#           'minute_hand', help='',default=60)
    args = parser.parse_args()
#    trigger_function(args.hour_hand,args.minute_hand )

    trigger_function(args.hour_hand)



