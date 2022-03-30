import boto3

AWS_REGION = "ap-south-1"

ssm_client = boto3.client("ssm", region_name=AWS_REGION)

new_string_parameter = ssm_client.put_parameter(
    Name='InstType',
    Description='EC2 Instance type for Dev environment',
    Value='t3.micro',
    Type='String',
    Overwrite=True,
    Tier='Standard',
    DataType='text')

print(
    f"String Parameter created with version {new_string_parameter['Version']} and Tier {new_string_parameter['Tier']}"
)
