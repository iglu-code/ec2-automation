import boto3
import os
instance = os.environ['INSTANCE_ID']
region = os.environ['AWS_REGION']
instances = [instance]
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))

