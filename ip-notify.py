import json
from urllib2 import urlopen
import os
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

# Configuration

DEST_ADDR = "you@email.com"
FROM_ADDR = "thismachine@email.com"

def send_update(ip):
    performDebugging = True
    msg = MIMEText('The new ip is: '+ ip)
    msg['To'] = DEST_ADDR
    msg['From'] = FROM_ADDR
    msg['Subject'] = 'Ip changed'

    p = Popen(['/usr/sbin/sendmail', '-t'], stdin=PIPE)
    p.communicate(msg.as_string())

def ip_log_check(ip):
    # load the log file
    try:
        f = open("ip.log", "a+b")
        log = f.readlines()
    except IOError:
        print "There was an error opening the log file"

    # Get the last ip logged in the log file.
    if len(log) > 0:
        last_ip = log[-1:][0].strip("\n")
    else:
        last_ip = ""

    if ip == last_ip:
        return True
    
    f.write(ip + "\n")
    return False
    

if __name__ == "__main__":
    ip = json.load(urlopen('http://httpbin.org/ip'))['origin']

    if not(ip_log_check(ip)):
        send_update(ip)

