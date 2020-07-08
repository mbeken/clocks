# Compute clock angle job 

## Description : Computes the clock angle between the hands of the clock hands i.e. hour and minute 

### Archtecture :
As the the sensor are emitting data at low frequency and computation logic is not compute heavy we have selected Cloud Function service for the performing serverless computing. Pubsub is used to perform the asynchronous execution of the request. Computed result is to be stored in the targeted data store based on downstream requirement. Decision is yet to made.
#### Architecture Diagram :

##### SENSOR PUSH -> COMPUTE_CLOCK_ANGLE_TOPIC -> CLOUD FUNCTION -> TARGET DATA STORE(CLOUDSQL or BIQQUERY) 

#### Componets Used  :
1. Pubsub Topic : act as messaging queue for asynchronous communication between the request
2. Cloud Function : Server less computing platform for the computational workloads
3. Bigquery or CloudSQL (Target Data Store): {TODO} Data Store for downstream processing 

### Deployement Guide :

#### Prerequeste:
1. GCP Account
2. All mentioned services to be enabled and have permission to use it.
#### Deployment steps :

##### Pubsub setup :
1. Search Pubsub service on console
2. Click on create topic icon
3. Fill the necessary detail like topic id i.e. "compute_angle_topic"  and encryption as google_auth.

#### Cloud function :
1. Search Cloud Function on console
2. Fill the requested details like Name, Trigger, Topic, Add Code etc.
    1. Name the job as "calculate_angle_between_clock_hands"
    2. Memory allocated 256 Mib
    3. Trigger is Cloud Pubsub
    4. Select topic we created in pubsub topic.
    5. Set source code as inline editor and runtime to Python 3.7 and copy main.py from repository
    to editor.
    6. Click on create icon.

#### Target data store: WIP



