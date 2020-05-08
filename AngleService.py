# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:20:50 2020

@author: prem
"""

from flask import Flask, request
import Angle
app = Flask(__name__)

    
@app.route("/")
def home():
    hr = int(request.args.get("hr"))
    mi = int(request.args.get("mi"))
    angle = Angle.Angle(hr, mi)
    response = "Angle between hour hand %d and minute hand %d is %.1f degrees" % (hr, mi, angle.calculateAngle())
    return response
    
if __name__ == "__main__":
    app.run(debug=True)