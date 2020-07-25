Description :

-> Computes the clock angle between the hands of the clock hands i.e. hour and minute

-> Sensor are emitting data at low frequency

-> Computation is not a heavy computation so we have can GCP Cloud Functions API which suits best.

-> GCP Pubsub is used to perform the asynchronous execution of the requests.

-> Computed result is to be stored in the targeted data store based on downstream requirement. Decision is yet to made currently stored in bigquery.


Architecture Diagram (ETL):

CLOCK_TIME_TO_PUBSUB_TOPIC -> CLOUD FUNCTION -> TARGET DATA STORE(CLOUDSQL or BIQQUERY)


Componets Used in GCP:

-> Cloud Functions API: Serverless, Easy to Deploy, Support multiple language, Detach and attach to any component.
-> PubSub API: Publisher-Subscriber Model,Asynchronous Scalable, Easy Modification, Secure
-> Bigquery API: Mostly we have used as Target Data Store for further processing


Deployement Guide:
Prerequeste:
GCP Account with required Roles and Permissions.
All mentioned services API are enabled.


Deployment steps :
1. Pubsub:
	- Search Pubsub service API on console
	- Click on create Topic
	- Fill the necessary detail like topic id i.e. "ClockTimeAsInputData" and Encryption as google_auth as default.

2. Cloud Function :
	- Search Cloud Function API on console
	- Name the Cloud Function as "CalculateClockAngleInJava"
	- Memory allocated 128 Mib (As this is temp application right now)
	- Trigger is Cloud Pubsub
	- Select topic we created in Pubsub Topics.
	- Set source code as inline editor and runtime to Java/Python and copy your code from repository to editor.
	- Click on create.
    
3. Target data store: 
    - Working on
