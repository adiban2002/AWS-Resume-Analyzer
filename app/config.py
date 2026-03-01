import os
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "aws-resume-analyzer-storage")

DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE", "resume-analysis")

APP_NAME = "AWS Resume Analyzer"
APP_VERSION = "1.0.0"

UPLOAD_DIR = "temp_uploads"

SKILL_KEYWORDS = [
    "python", "aws", "docker", "kubernetes", "terraform",
    "linux", "devops", "ci/cd", "jenkins", "ec2", "s3",
    "cloud", "machine learning", "fastapi"
]