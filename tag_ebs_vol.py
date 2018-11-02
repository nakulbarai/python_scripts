import boto3
client = boto3.client('ec2')
custom_filter = [{'Name': 'tag:Name', 'Values': ['trinityprovendpoint-production-test-*' ]}]
response  = client.describe_instances(Filters=custom_filter)
instancelist = []
for reservation in (response["Reservations"]):
 for instance in reservation["Instances"]:
  instancelist.append(instance["InstanceId"])
eid= instancelist
print (eid)


ec2 = boto3.resource('ec2')
index=0
while index <len (eid):
    deviceid = []
    tagid = []
    instance = ec2.Instance(eid[index])
    vol = instance.volumes.all()
    volume_list = [v.id for v in vol]
    vid = volume_list
    response = client.describe_volumes( Filters=[
            {
                'Name': 'attachment.instance-id',
                'Values': [ eid[index]] } ])
    for Volumes in (response["Volumes"]):
        for Attachments in Volumes["Attachments"]:
            deviceid.append(Attachments["Device"])
    response = client.describe_tags( Filters=[
            {
                'Name': 'resource-id',
                'Values': [ eid[index]] } ])
    for Tags in (response["Tags"]):
            tagid.append(Tags["Value"])
    tag_name= tagid[0]
    count = 0
    while count <len(vid):
            ec2 = boto3.resource('ec2')
            volume = ec2.Volume(vid [count])
            number = 0
            while number <len(deviceid):
                tag = volume.create_tags(
                    Tags = [

                        {
                         'Key': 'Name',
                         'Value': tag_name + deviceid[number]
                         }
                         ]
                        )
                number = number+ 1
            count = count +1
    print (tag)
    index = index + 1
    print (vid)
    print (deviceid)
    print (tagid)
