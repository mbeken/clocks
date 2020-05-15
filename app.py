"""
code for calculate angle
"""
import os
from flask import Flask, render_template, request, json
from clock import Clock_Angle
app = Flask(__name__)

@app.after_request
def add_header(newr):
    """
    to add header
    """
    newr.headers["Pragma"] = "no=cache"
    newr.headers["Expires"] = "0"
    newr.headers["Cache-Control"] = "public, max-age=0"
    return newr

@app.route("/home", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])

def home():
    """
    home to calculate angle
    """
    answer = ""
    if "fHour" in request.form and "fMins" in request.form:
        hour = request.form["fHour"]
        minutes = request.form["fMins"]
        answer = Clock_Angle(hour, minutes).checkValues()
    return render_template("Home.html", pageData=json.dumps(answer))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))  
    