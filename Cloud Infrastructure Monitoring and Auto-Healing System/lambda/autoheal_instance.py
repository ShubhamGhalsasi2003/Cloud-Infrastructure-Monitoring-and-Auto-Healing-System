import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instance_id = event['detail']['instance-id']
    ec2.reboot_instances(InstanceIds=[instance_id])
    return {'status': 'rebooted', 'instance_id': instance_id}