In dns-update.py file replace respective parameters like 
- domain name(jira.nuxpy.org), 
- hoted ID 
- working dir or create /work/route53 :) 
- install pycurl module 
- populate /etc/rc.local with 
   python3 dns-update.py
   exit 0 
- chomd +x /etc/rc.local ( I am using ubuntu 18)
