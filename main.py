from flask import Flask, request, render_template

APP = Flask(__name__ ,template_folder='./template')


def clock_angle(hrs, mins):
    """
    Funciton to create angle betweem hands of clock
    Args:
        hrs: value of hours between 1 to 12
        mins : value of mins between 0 to 59
    """
    degree_per_min = 6
    degree_per_hour = 30
    degree_intern = 0.5

    if hrs == 12:
        hrs = 0

    angle_between = abs(hrs*degree_per_hour - mins*degree_per_min + mins*degree_intern)
    return "Angle1 -> " + str(angle_between)
#        TODO: implement function for data inserting into SQL
#        insert_in_db()


@APP.route('/')
def landing_page():
    """
    Function to call base HTML
    """
    return render_template("index.html")


@APP.route('/', methods=["GET", "POST"])
def index():
    """
    Function to call clock_angle
    """
    str1 = "Nothing to show!!!"
    if request.method == 'POST':
        hrs = int(request.form['hrs'])
        mins = int(request.form['mins'])
        if (0 <= int(hrs) <= 12 and 0 <= int(mins) <= 59):
            str1 = clock_angle(hrs, mins)
        else:
            str1 = "Invalid Data"

    return render_template("index.html", data=str1)

if __name__ == '__main__':
     APP.run(host='0.0.0.0', debug=True)
