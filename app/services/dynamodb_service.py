import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
table = dynamodb.Table("resume-analysis")


def save_analysis(result: dict):
    analysis_id = str(uuid.uuid4())

    item = {
        "analysis_id": analysis_id,
        "created_at": datetime.utcnow().isoformat(),
        "result": result
    }

    table.put_item(Item=item)

    return analysis_id


def get_analysis(analysis_id: str):
    response = table.get_item(
        Key={"analysis_id": analysis_id}
    )
    return response.get("Item")


def list_analyses():
    response = table.scan()
    return response.get("Items", [])