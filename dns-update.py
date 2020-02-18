#!/usr/bin/python3
import json
import os 
from m_curly import  find_ip
IP = find_ip()
RPATH = '/work/route53'

# Json Dictionary  Template 
data = {'Comment': 'Update the A record set', 'Changes':\
        [{'Action': 'UPSERT', 'ResourceRecordSet': {'Name': 'jira.nuxpy.org', \
        'Type': 'A', 'TTL': 60, 'ResourceRecords': [{'Value': '1.2.3.4'}]}}]}
data['Changes'][0]['ResourceRecordSet']['ResourceRecords'][0]['Value'] = IP

# updating the file 
with open(RPATH+'/result.json', 'w') as fIP:
     json.dump(data, fIP)
comm = 'aws route53 change-resource-record-sets --hosted-zone-id "MYID" --change-batch file://' + RPATH + '/result.json'

# Calling os to execute 
os.system(comm)
