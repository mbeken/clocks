# Clock Exercise

---------------------------------------
### Description:-
Clock service will calculate the angle between the hands on a clock face. For example input 03:00 would yield to 90 degrees.<br>
This service will take time value as input and return an angle value in json format, so that can be used in downstream processing.

## Run Locally

Below steps required to run this service locally.

1. Clone git repo.

    ```
    https://github.com/gajanankathar/clocks.git
    ```

2. Setup docker, build & run clocks app docker image.

   ```
    docker-compose run --service-ports web
   ```

3. Visit the application at [http://localhost/services/clocks/angle/12:90](http://localhost/services/clocks/angle/12:90).


## Deploying

List of steps to deploy application in GCP flexible app engine service as:

1. Use the [Google Developers Console](https://console.developer.google.com)  to create a project/app id. (App id and project id are identical)

2. Open google cloud SDK & setup the gcloud tool, if you haven't already.

   ```
   gcloud init
   ```

3. Use gcloud to deploy your app.

   ```
   gcloud app deploy
   ```

4. Access this application using app engine provided public ip/domain & service endpoint [https://clocks-app-277815.df.r.appspot.com/services/clocks/angle/10:34](https://clocks-app-277815.df.r.appspot.com/services/clocks/angle/10:34)




