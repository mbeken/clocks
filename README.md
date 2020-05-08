# clocks
An interview exercise for a devops position

# Brief description of how and where application will run
This is web based application designed in python and deployed as flask web service on python.

This application will be accessed using browser URL (given example below) with request parameters as hour and minute value and hit enter. Angle between hour and minute hand will be displayed on browser.

**Below are instructions to setup this application**

Install flask package in python environment: pip install Flask

Run program – python AngleService.py

Request url with parameters – 

Hr – hour hand value

Mi – minute hand value

http://localhost:5000/?hr=3&mi=15

This application runs on python server as webservice. 

AngleService.py – this file needs to be run. It will host application as webservice on localhost. Use this url to request angle value - http://localhost:5000/?hr=3&mi=15

# Code files
Angle.py – This file contains python code which contains mathematical logic for calculating time value to angle value in degrees.

AngleService.py – This file contains python code which deploys Angle.py code to as webservice using flask api.

# Output
**Request url with parameters**

Hr – hour hand value

Mi – minute hand value

http://localhost:5000/?hr=3&mi=15
