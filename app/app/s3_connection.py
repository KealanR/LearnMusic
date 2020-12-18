import logging
import boto3
from botocore.exceptions import ClientError

bucket = "kr-cpp-project-learn-music"
upload_folder = "uploads"
s3 = boto3.client('s3')

def upload_to_S3(file_name):
    
    object_name = file_name
    
    try:
        response = s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True