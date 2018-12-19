import csv
import time
import subprocess
import os
import sys
from setting_fun import Vam_settings


settings = Vam_settings()
with open('vaf_settings.csv') as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter=",")
        for setting in readCSV:
                print setting

minutes = (int)(sys.argv[3])
print (minutes)

### read the data of command line arguments
### pass the conditions to validate
### if we check one condition then pass '1' else pass '0'

command2 = "is there any reminders for me"

list1 = (sys.argv[1]).split(";")
conditions = '|'.join(list1)
print(conditions)

list2 = (sys.argv[4]).split(";")
conditions2 = '|'.join(list2)
print(conditions2)
arg = sys.argv[2]

subprocess.call(['python','vam_record_transcribe.py',conditions2,arg,'1'])

time.sleep(minutes * 60)

settings.vam_wake_word_generation(setting['wake_word'])
settings.vam_command_generation(command2,0)
subprocess.call(['python','vam_record_transcribe.py',conditions,arg,'0'])


