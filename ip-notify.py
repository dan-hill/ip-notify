import json
from urllib2 import urlopen
import os
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

def sendUpdate(ip):
    performDebugging = False
    msg = MIMEText('The new ip is: '+ ip)
    msg['To'] = 'thirtyseventhirty@gmail.com'
    msg['From'] = 'dan@linux-dev'
    msg['Subject'] = 'Ip changed'

    p = Popen(['/usr/sbin/sendmail', '-t'], stdin=PIPE)
    p.communicate(msg.as_string())

ip = json.load(urlopen('http://httpbin.org/ip'))['origin']    
log = os.popen("tail -10 ip-log").readlines()

print ip,
print log,

if ip in log:
else:
    with open('ip-log', 'w') as f:
        f.write(ip)
        sendUpdate(ip)
