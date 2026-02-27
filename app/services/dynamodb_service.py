import boto3
import uuid
from datetime import datetime
from decimal import Decimal

dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
table = dynamodb.Table("resume-analysis")


def convert_floats_to_decimal(obj):
    """
    Recursively convert float → Decimal (required by DynamoDB)
    """
    if isinstance(obj, float):
        return Decimal(str(obj))
    elif isinstance(obj, dict):
        return {k: convert_floats_to_decimal(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_floats_to_decimal(i) for i in obj]
    else:
        return obj


def save_analysis(result: dict):
    analysis_id = str(uuid.uuid4())

    item = {
        "analysis_id": analysis_id,
        "created_at": datetime.utcnow().isoformat(),
        "result": convert_floats_to_decimal(result)
    }

    table.put_item(Item=item)

    return analysis_id


def get_analysis(analysis_id: str):
    response = table.get_item(Key={"analysis_id": analysis_id})
    return response.get("Item")


def list_analyses():
    response = table.scan()
    return response.get("Items", [])