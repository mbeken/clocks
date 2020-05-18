"""
Clock Exercise for Schlumberger Interview
"""
# coding: utf-8

# In[2]:

import os
from flask import Flask, render_template, request
app = Flask(__name__, template_folder='flask_template')
OUTPUT = "e"
@app.route('/', methods=['GET'])
def home():
    """Go to the HTML template"""
    return render_template('angle.html', message=OUTPUT)
@app.route('/user', methods=['POST'])
def reset():
    """ Calculate the clock function """
    try:
        hour = int(request.form['hour'])
        minute = int(request.form['minute'])
        if ((hour >= 1) & (hour <= 12)) & ((minute >= 0) & (minute <= 60)):
            angle = abs((hour * 30 + minute * 0.5)-(minute * 6))
            if angle > 180:
                angle = 360 - angle
            msg = "Angle between %s hours and %s minutes : "%(hour, minute)+str(angle)
        else:
            msg = "Enter correct integer value(Hour=1 to 12, Minute=0 to 60)"
        return render_template('angle.html', message=msg)
    except ValueError:
        msg = "Enter correct integer value(Hour=1 to 12, Minute=0 to 60)"
        return render_template('angle.html', message=msg)
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=False, host='0.0.0.0')
 