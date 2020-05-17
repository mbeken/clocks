from google.cloud import bigquery

from google.cloud import storage


#requirements.txt
#oogle-cloud-bigquery>=1.3.0
#oogle-cloud-storage>=1.28.0
#andas>=1.0.3


def export_to_gcs(hrs,mins,angle):
    # BQ Query to get add to cart sessions
    
    bq_client = bigquery.Client(project="ind-coe")

    Query=" Insert into mangesh.clock select cast(%s as int64), cast(%s as int64) , cast(%s as Numeric)" %(hrs,mins,angle)
    query_job = bq_client.query(Query)

    Query="Select Hour, Minute, Angle from mangesh.clock"
    query_job = bq_client.query(Query) # API request

    rows_df = query_job.result().to_dataframe() # Waits for query to finish
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('ind-coe-mangesh')
    blob = bucket.blob('Add_to_Cart.csv')
    blob.upload_from_string(rows_df.to_csv(sep=';',index=False,encoding='utf-8'),content_type='application/octet-stream')


def clock_angle(request):
    """
      {"hrs":"3","mins":"0"}
    """
    request_json = request.get_json()
    request_args = request.args
    if request.args and 'hrs' in request.args:
        hrs = int(request.args.get('hrs'))
        mins = int(request.args.get('mins'))
    elif request_json and 'hrs' in request_json:
        hrs = int(request_json['hrs'])
        mins = int(request_json['mins'])
    elif request_args and 'hrs' in request_args:
        hrs = int(request_args['hrs'])
        mins = int(request_args['mins'])
    else:
        ans_str = "Cannot compute due to some error"

    if (0 <= int(hrs) <= 12 and 0 <= int(mins) <= 59):
        degree_per_min = 6
        degree_per_hour = 30
        degree_intern = 0.5

        if hrs == 12:
            hrs = 0

        angle = abs(hrs*degree_per_hour - mins*degree_per_min + mins*degree_intern)
        # Return the smaller angle of two  
        # possible angles 
        angle = min(360 - angle, angle) 
        ans_str = "Angle -> " + str(angle)

    else:
        ans_str = "Invalid Input, cannot compute, Try Again"
    export_to_gcs(hrs,mins,angle)

    return ans_str

