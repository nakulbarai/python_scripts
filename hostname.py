import boto3
import os
ec = boto3.client('ec2' , region_name='us-east-2' , aws_access_key_id='XXXXX',
    aws_secret_access_key='XXXXXXX')
custom_filter = [{'Name': 'tag:Name', 'Values': ['nakul-test*' ]}]
reservations = ec.describe_instances(Filters=custom_filter)
for r in reservations['Reservations']:
            for i in r['Instances']:
                instance_id = i['InstanceId']
                print (instance_id)
                for t in i['Tags']:
                    if t['Key'] == 'Name':
                        iname = t['Value']
                        if (iname != "nakul-test-01") and (iname != "nakul-test-02"):
                            hostname= "nakul-test-01"
                            os.system('hostname %s' % hostname)
                            response = ec.create_tags(
                                            Resources=[
                                                    instance_id,
                                                        ],
                                                        Tags=[
                                                        {
                                                        'Key': 'Name',
                                                        'Value': hostname
                                                        },
                                                            ]
                                                            )
                        if (iname != "nakul-test-01") and (iname == "nakul-test-02"):
                            hostname= "nakul-test-01"
                            os.system('hostname %s' % hostname)
                            response = ec.create_tags(
                                            Resources=[
                                                    instance_id,
                                                        ],
                                                        Tags=[
                                                        {
                                                        'Key': 'Name',
                                                        'Value': hostname
                                                        },
                                                            ]
                                                            )
                        if (iname == "nakul-test-01") and (iname != "nakul-test-02"):
                            hostname= "nakul-test-02"
                            os.system('hostname %s' % hostname)
                            response = ec.create_tags(
                                            Resources=[
                                                    instance_id,
                                                        ],
                                                        Tags=[
                                                        {
                                                        'Key': 'Name',
                                                        'Value': hostname
                                                        },
                                                            ]
                                                            )
