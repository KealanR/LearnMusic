import logging
import boto3
from botocore.exceptions import ClientError

bucket = "kr-cpp-project-learn-music"
upload_folder = "uploads/"
download_folder = "downloads/"
s3c = boto3.client('s3')
s3r = boto3.resource('s3')

def upload_to_S3(file_name):
    
    object_name = file_name
    location = upload_folder + file_name
    try:
        response = s3c.upload_file(location, bucket, object_name)
        print(response)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def download_from_s3(file_name):
    try:
        
        location = download_folder + file_name
        s3r.Bucket(bucket).download_file(file_name, location)
        return location
    except ClientError as e:
        logging.error(e)
        return None