

## Product Backlog Item (Sprint Story)

Here is the story that is in the backlog. 

As with all stories, the team may have been optimistic with how much can be done in the time permitted. It's ok to meet some of the acceptance criteria by documenting what you would do in the next sprint! Prioritize your time and make sure you have some technical content to deliver.

### Description:-

As a team<br>
We need a serivce that we can send a time value to and have it return or store an angle value<br>
So that we can use it in downstream processing

URL :
Output JSON :

### Detail:-

We need to calculate the angle between the hands on a clock face. For example input 03:00 would yield 90 degrees.

### Acceptance Criteria:-

1) Code to perform the calculation
    #### URL : http://127.0.0.1:5000//clock_angle/3:15
    #### Output : {
                "context": "Angle for time 3:15 is 7.5 degree."
            }

1) How will you deploy this solution (in code or as a todo list if time is limited). i.e. how and where will this run?
---------------------------------
## Now Deploy the application on GCP
---------------------------------

-On google cloud
----------------
	--create project

-go to GC console generate ssh key
----------------------------------
	---command to generate ssh key: ssh-keygen -t rsa -b 4096 -C "abhilash"
	---cat .ssh/id_rsa.pub

-Add pub key to git hub account
-------------------------------

-GC console: go into your project clone the repo
------------------------------------------------
--run : git clone https://github.com/githubabhilash/clocks.git


-GC console:Now go to project folder
------------------------------------
---run : gcloud app deploy
Note :It will ask region enter the numric value.


2) How will you manage any infrastructure needed?

## Infrastructure needed
----------------------
 We will require GC resources based on the requirements
 i. e.
    - To run no of instances we will require no of CPU i. e. for now instances 1 , 1 cpu will be required.
    - Memory will be required based on resource i.e memory_gb: 0.5
    - disk_size_gb: 10


3) Delivered as a feature branch in the repo fork
   ##  -- featureabhilash branch is created

1) Bonus points for a working deployed solution in GCP that you can demo at the "sprint review" (ie interview)
    -- Deployed this service to on GCP and its running.
1) Any DevOps/Cicd components that would support this feature in a production setting
