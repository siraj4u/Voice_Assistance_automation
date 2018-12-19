'''
1) sudo easy_install requests 
2) sudo pip install requests
'''

import sys
import os
import base64
import hmac
import hashlib
import time
import requests  
import re
import subprocess

'''
Replace "###...###" below with your project's host, access_key and access_secret.
'''
access_key = "80e908d2c8d7c6033fee8790152157be"
access_secret = "xIZCoFBMLSeChWeNKnwdzJs9XVm43YHRqf1IGQHM"
requrl = "http://identify-ap-southeast-1.acrcloud.com/v1/identify"


http_method = "POST"
http_uri = "/v1/identify"
data_type = "audio"
signature_version = "1"
timestamp = time.time()

subprocess.call(['rm',sys.argv[1]])

subprocess.call(['rm','result_file.txt'])
string_to_sign = http_method+"\n"+http_uri+"\n"+access_key+"\n"+data_type+"\n"+signature_version+"\n"+str(timestamp)

sign = base64.b64encode(hmac.new(access_secret, string_to_sign, digestmod=hashlib.sha1).digest())

#subprocess.call(['arecord','-d','15','-r','44100','-c','2','songtitle.wav'])
subprocess.call(['arecord','-d','15','-r','44100','-c','2',sys.argv[1]])

my_list = (sys.argv[2]).split(";")
conditions = '|'.join(my_list)
print conditions

# suported file formats: mp3,wav,wma,amr,ogg, ape,acc,spx,m4a,mp4,FLAC, etc
# File size: < 1M , You'de better cut large file to small file, within 15 seconds data size is better

f = open(sys.argv[1], "rb")
sample_bytes = os.path.getsize(sys.argv[1])

files = {'sample':f}
data = {'access_key':access_key,
        'sample_bytes':sample_bytes,
        'timestamp':str(timestamp),
        'signature':sign,
        'data_type':data_type,
        "signature_version":signature_version}

r = requests.post(requrl, files=files, data=data)
r.encoding = "utf-8"

#if re.search(r'\b(Enrique|Hero)\b', r.text, re.I):
if re.search(conditions, r.text, re.I):
    outfile =  open ("result_file.txt","w+")
    outfile.write('Test case passed...')
    outfile.close()
    print('Test case pass..')
else:
    print('Test case fail...')
    outfile =  open ("result_file.txt","w+")
    outfile.write('Test case failed...')
    outfile.close()

