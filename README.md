# cloud-functions

Function to calculate angle between 2 hands of clock.
    Deployed on Gcloud as cloud function.
    responds to all http request


# deployed url(Mandatory to pass Parameters) : https://us-central1-ind-coe.cloudfunctions.net/clock_angle_between_hands_m?h=03&m=00

google-repository: github_manix049_cloud_angle_m

follows CI-CD : any update pushed to git gets auto deployed.

git commit --> same git repository gets cloned to google repository --> trigger is fired for cloud build --> cloud build completes --> changes visible.

Respository consist of :
------------------------
1) Main.py --> this is main file where code is kept
2) test_main.py
3) requirements.txt
4)cloudbuild.yaml
5)read.me



