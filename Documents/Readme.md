**Assumptions:**
1. Edge devices are configured 
2. Azure Iot hub is configured 
3. Eventhub namespace and Lib is in place


**TODO List:**
1. Team need to add eventhub library service in startup.cs @
line 25 .
2. Team need to add subscribe to an event in startup.cs @ line 55 .
3. Team need to add eventhub library service in startup.cs @ line 25 .
4. Team need to remove AngleController before production as this is for testing the logic with out event.
5. Team need to add database call for saving data in database by following the Datamodel
given.

**Design:**
1. Design diagram is @ Documents/Clock to Angle-Design 
2. Design as follow 
	a. IOT-Hub  is connect to edge device which are in clock . 
	b. It will send data to Eventhub topic. 
	c. Service will listen to that event by subscribing the topic using consumer group. 
	d. service take the time as input calculate the angle and save it to the database.

**Infrastructure:**
1. Team will use Intrastrucre as a code, No manual infrastructure get created.
2. Tool may be used Terraform/puppet/Chef.

**CI/CD:** 
1. We will use CI using Git 
2. For branching we will use Git flow
3. We use Git workflow action for CD to update web app when ever there is a PR merge in the master.
4. Direct merge will be disabled only PR merged will be allowed after review with Sr persons.


For Prduction below are modification need to be done When Pr is raised
for the code 
1. Unit test cases should be pass.
2. Sonarqube should be passed.
3. We will implement slot deployment for App service.
