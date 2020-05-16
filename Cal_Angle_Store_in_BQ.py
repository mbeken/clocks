import argparse
import logging
import time, sys, os, subprocess
from datetime import date

from google.cloud import bigquery
from google.api_core.exceptions import ClientError
from google.oauth2 import service_account
from google.api_core import exceptions

import google.auth
from google.cloud.bigquery import Table, AccessEntry, Dataset

import datetime


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

"Adding Logger"
handler = logging.FileHandler('/home/mangesh_soni/clokc/GetAngleFromClock' + str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.log', mode='w')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

output_handler = logging.StreamHandler(sys.stdout)
output_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - [%(filename)s:%(lineno)d] - %(message)s')
output_handler.setFormatter(formatter)

logger.addHandler(output_handler)

key_path = '/home/mangesh_soni/clokc/login.json'
credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],)

#credentials = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])

BQ_CLIENT = bigquery.Client(credentials=credentials, project="shc-enterprise-data-lake-dev")


#BQ_CLIENT = bigquery.Client()


def bigquery_input(): 
    
    logger.info("Getting  Hour and Minute from Clock Table")

    Query="""
              Select Hour, Minute, ANgle 
              from `shc-enterprise-data-lake-dev.audit_log.clock`
    """

    query_job = BQ_CLIENT.query(
        Query,
        #location="US",
    )
    
    LevelID = [x for x in query_job]
    for x in LevelID:   
        Hour=int(x[0])
        Minute=int(x[1])
        Angle=trigger_function(Hour, Minute)
        bigquery_update_Angle(Hour, Minute, Angle)
        
    

def bigquery_update_Angle(Hour, Minute, Angle):
    logger.info("Updating Angle in Clock Table for Hour and Minute")

    Query="""
              Update `shc-enterprise-data-lake-dev.audit_log.clock` 
              set ANgle= %s
              where Hour = %s and Minute =%s 
    """ %(Angle, Hour, Minute)

    query_job = BQ_CLIENT.query(
        Query,
        #location="US",
    )

    Query="Select * From  `shc-enterprise-data-lake-dev.audit_log.clock` " 

    query_job = BQ_CLIENT.query(
        Query,
        #location="US",
    )

    LevelID = [x for x in query_job]
    for x in LevelID:
        print(x[0], x[1], x[2])
        logger.info("value of Hour is %s , Minute is %s and Calculated Angle is %s " %(x[0], x[1], x[2]))
    





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


def trigger_function(hour_hand, minute_hand):
    """h = input("ebter the hour clock")  #9
    m = input("enter the minute clock") #60"""
    
    hour_hand,minute_hand= int(hour_hand), int(minute_hand)
    
    try:
        logger.info("Function to Calculate angle b/w  hour hand is %s and minute hand is %s " %(hour_hand, minute_hand))
        Angle = calcAngle(int(hour_hand) , int(minute_hand))
        print('Angle ', calcAngle(int(hour_hand) , int(minute_hand))) 
        logger.info("Angle is %s b/w  hour hand is %s and minute hand is %s " %(Angle , hour_hand, minute_hand))
    except Exception as e:
        logger.info("Error in calculating the Angle \n" + str(e) + "\n" )
                
    
    logger.info("Calculation completed : {}".format(datetime.datetime.now()))
    return Angle
    
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
           description=__doc__,
           formatter_class=argparse.RawDescriptionHelpFormatter)

    #parser.add_argument(
    #       'hour_hand', help='',default=12)
    #parser.add_argument(
    #       'minute_hand', help='',default=60)
    #args = parser.parse_args()
    #trigger_function(args.hour_hand,args.minute_hand )
    bigquery_input()
    


