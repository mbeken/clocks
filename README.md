# Clock Exercise

This is a spark Streaming application which reads data from Kafka topic in read time,
 calculates angle between hands of clock and inserts data into database.

**Environment:**

    1. GCP
    2. Pub/Sub of Kafka Installed
    3. MySQL instance
    4. Dataproc Cluster


## Deployment Steps: 
Setup a Kafka cluster and create a Kafka topic where data would be published

Configure the kafka into config.properties file by updating server and topic name values

Format of data to be published in Kafka topic shout be eg : 12.30, 01.22.
 
Create an MySQL instance. Create a database and table into MySQL.
Schema of table should be : 
*(TIME FLOAT, ANGLE FLOAT)*

Configure the config.properties file for MySQL values

## Code Build
Use below command to build jar :

*sbt package*

## Execute jar
*java -cp clockangle.jar com.schlumberger.clock.CalculateClockAngle*