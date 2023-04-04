import requests

# Cloud Function to convert CSV to Parquet
def send_event_to_cloud_run(event, context):
     print('Processing file: {}'.format(event['name']))

     # Get the file details from the event
     file_data = event
     bucket_name = file_data['bucket']
     file_name = file_data['name']
     file_path = "gs://{}/{}".format(bucket_name, file_name)
     print('File path: {}'.format(file_path))

     # Convert the file to Parquet using the Cloud Run service
     headers = {'Content-Type': 'application/json'}
     data = {'file_path': file_path,'file_name': file_name, 'bucket_name': bucket_name}
     url = "https://csv-to-parquet-33y7v6wwta-uc.a.run.app"
     response = requests.post(url, headers=headers, json=data)
     print('Conversion response: {}'.format(response.text))
