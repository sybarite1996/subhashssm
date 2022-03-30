import json
from datetime import date, datetime
import boto3


# Helper method to serialize datetime fields
def json_datetime_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


AWS_REGION = "us-east-1"

ssm_client = boto3.client("ssm", region_name=AWS_REGION)

describe_response = ssm_client.describe_parameters(Filters=[
    {
        'Key': 'Type',
        'Values': [
            'String',
        ]
    },
])

print('Parameters information:')
print(
    json.dumps(describe_response['Parameters'],
               indent=4,
               default=json_datetime_serializer))
