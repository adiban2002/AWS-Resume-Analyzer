import os
import json
import boto3
from botocore.exceptions import ClientError

REGION = "ap-south-1"
ENDPOINT_NAME = "resume-analyzer-endpoint"


runtime_client = boto3.client(
    "sagemaker-runtime",
    region_name=REGION
)


def get_similarity_score(resume_text: str, jd_text: str) -> dict:
    try:
        payload = {
            "resume": resume_text,
            "jd": jd_text
        }

        response = runtime_client.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType="application/json",
            Body=json.dumps(payload)
        )

        result = json.loads(response["Body"].read().decode())

        return result

    except ClientError as e:
        return {
            "error": "SageMaker client error",
            "details": str(e)
        }

    except Exception as e:
        return {
            "error": "Unexpected error while invoking SageMaker",
            "details": str(e)
        }