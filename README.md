Function clock_angle() accepts 2 parameters as json

Input:
Sample JSON:
{
    "hrs":3,
    "mins":0
}
Accessing Function:
1.  curl -X POST "https://us-central1-ind-coe.cloudfunctions.net/clock_repository" -H "Content-Type:application/json"  -d '{"hrs":10,"mins":20}'

2. https://us-central1-ind-coe.cloudfunctions.net/clock_repository?hrs=10&mins=10


Output:
    return string
e.g. 'Angle -> 90.0'

Deploying Method:
    The code automatically push changes to Google cloud function. 
    Google cloud "Source repositroy" has Trigger build on "Google Build" which deploys code to Cloud function "clock_angle".
