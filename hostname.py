import boto3
import os
import itertools
import urllib.request
instanceid = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read().decode()
client = boto3.client('ec2' , region_name='us-east-2' , aws_access_key_id='XXX',
    aws_secret_access_key='XXX')
custom_filter = [{'Name': 'tag:Name', 'Values': ['nakul-test*' ]}]
response  = client.describe_instances(Filters=custom_filter)
instancelist = []
for reservation in (response["Reservations"]):
 for instance in reservation["Instances"]:
  instancelist.append(instance["InstanceId"])
eid= instancelist
print (eid)
ec2 = boto3.resource('ec2',region_name='us-east-2' , aws_access_key_id='XXXXX',
    aws_secret_access_key='XXXX')
index=0
tagid = []
while index <len (eid):
    instance = ec2.Instance(eid[index])
    response = client.describe_tags( Filters=[
            {
                'Name': 'resource-id',
                'Values': [ eid[index]] } ])
    for Tags in (response["Tags"]):
            tagid.append(Tags["Value"])
    index = index + 1
print (tagid)
if not "nakul-test-01" in tagid:
        print("nakul-test-01")
        hostname = "nakul-test-01"
        os.system('hostname %s' % hostname)
        response = client.create_tags( Resources=[ instanceid ],Tags=[ {'Key': 'Name','Value': hostname },])
elif not "nakul-test-02" in tagid:
        print("nakul-test-02")
        hostname = "nakul-test-02"
        os.system('hostname %s' % hostname)
        response = client.create_tags( Resources=[ instanceid ],Tags=[ {'Key': 'Name','Value': hostname },])
else:
    exit()
