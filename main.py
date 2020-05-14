import os
import logging
from flask import Flask, render_template, request
from google.cloud import bigquery
from google.cloud.bigquery.client import Client
import datetime

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'keyfile.json'

#credentials = app_engine.Credentials()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/result',methods = ['POST'])
def result():
   if request.method == 'POST':
         #get the inputs from the form
      h = int(request.form['hour'])
      m = int(request.form['minute'])

      if (h < 0 or m < 0 or h > 12 or m > 60): 
            print('Wrong input')
        
      if (h == 12): 
            h = 0

      if (m == 60): 
            m = 0 
      #calculate the hour and minute
      hour_angle = 0.5 * (h * 60 + m) 
      minute_angle = 6 * m    

      #calculate the angle
      angle = abs(hour_angle - minute_angle) 

      angle = min(360 - angle, angle)

        
      client = bigquery.Client()
 # Prepares a reference to the dataset
      dataset_ref = client.dataset('clocks')

      table_ref = dataset_ref.table('angles_details')
      table = client.get_table(table_ref)  # API call

      rows_to_insert = [
            {u'hours': h,
            u'minutes': m,
            u'angle': angle,
            u'updated_on': datetime.datetime.now()
            }
      ]
      client.insert_rows(table, rows_to_insert)  # API request   

      #print the angle in result page
      return render_template("result.html",result = str(angle))

if __name__ == '__main__':
   app.run(debug = True)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
