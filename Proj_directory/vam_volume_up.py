##[import libraries]

import subprocess
import os
import sys

''' 
importing the Vam_settings from the settings_fun file
'''
from setting_fun import Vam_settings

## sys.argv[1] command for asking 
## sys.argv[2] command for the set volume
## sys.argv[3] is a wake word
## create a object to the Vam_settings() class for smart speaker functionalities

settings = Vam_settings()
### amplitude levels os data should be stored in file.
### if file with same name was there previously then it will delete. 
subprocess.call(['rm','vol_record_file.txt'])
settings.vam_inter_command_sleep() ### set the time delay for the proccessing

'''
step1:
asking the command and run python script, calculate the amplitude levels
'''
settings.vam_wake_word_generation(sys.argv[3]) ### calling function for wake word generation like ok google or alexa
settings.vam_command_generation(sys.argv[1],0) ### calling function for command generation [asking something]
subprocess.call(['python','vam_loudness_mic.py']) ### python script of calculate amplitude

'''
step 2:
again increasing or decreasing the volume levels to calulate amplitude
'''
settings.vam_wake_word_generation(sys.argv[3])
### pass the command for setting the volume levels
settings.vam_command_generation(sys.argv[2],0)
settings.vam_inter_command_sleep()

'''
step 3:
repeate step 1 and calculate amplitude between different volume levels
'''
settings.vam_wake_word_generation(sys.argv[3])
settings.vam_command_generation(sys.argv[1],0)
subprocess.call(['python','vam_loudness_mic.py'])

### script for calculating both amplitide levels
subprocess.call(['python','vam_volume_up_checker.py'])


