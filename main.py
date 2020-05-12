from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/calcAngle',methods=['get'])
def calcAngle():
    hour = int(request.args.get('hour',0))
    minute = int(request.args.get('minute',0))
    if (hour < 0 or minute < 0 or hour > 12 or minute > 60):
        print('Wrong input')
    if (hour == 12):
        hour = 0
    if (minute == 60):
        minute = 0

    # Calculate the angles moved by
    # hour and minute hands with
    # reference to 12:00
    hour_angle = 0.5 * (hour * 60 + minute)
    minute_angle = 6 * minute

    # Find the difference between two angles
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle of two
    # possible angles
    angle = str(int(min(360 - angle, angle)))

    return angle
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
