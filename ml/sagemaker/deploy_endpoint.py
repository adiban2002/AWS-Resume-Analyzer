import boto3
import sagemaker
from sagemaker.pytorch import PyTorchModel

ROLE_ARN = "arn:aws:iam::800557028391:role/SageMakerExecutionRole"
REGION = "ap-south-1"
ENDPOINT_NAME = "resume-analyzer-endpoint"

MODEL_DATA = "s3://aws-resume-analyzer-storage/model.tar.gz"

boto_session = boto3.Session(region_name=REGION)
sagemaker_session = sagemaker.Session(boto_session=boto_session)

print("Using region:", REGION)

model = PyTorchModel(
    model_data=MODEL_DATA,          
    role=ROLE_ARN,
    entry_point="inference.py",
    source_dir=".",                 
    framework_version="2.0",
    py_version="py310",
    sagemaker_session=sagemaker_session
)

print("Model defined.")

predictor = model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large",
    endpoint_name=ENDPOINT_NAME
)

print("✅ Endpoint deployment started!")