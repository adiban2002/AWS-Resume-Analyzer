import boto3

S3_BUCKET = "aws-resume-analyzer-storage"
REGION = "ap-south-1"

s3_client = boto3.client("s3", region_name=REGION)

def upload_file_to_s3(file_path: str, object_name: str):
    s3_client.upload_file(file_path, S3_BUCKET, object_name)

def download_file_from_s3(object_name: str, download_path: str):
    s3_client.download_file(S3_BUCKET, object_name, download_path)