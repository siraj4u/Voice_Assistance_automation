##[import libraries] ##

import subprocess
import time
import os
import sys
import csv

'''
importing class Vam_settings from the file of setting_fun.py
'''

from setting_fun import Vam_settings

'''
1.Here we read data from the csvfile.
2. Read test_cases from vaf_test_cases.csv, parse based on format:

s.no, command, attempts(integer, non negative - no. of attemts to be performed), aplay_com_file_name (use this if not null, overrides tts setting), add_delay (integer (-/+), val in secs), validation procedure(s), validation parameters, expected response, actual response, test result, logs txt, logs media, cnt. of attempt

3.Pass commands to smart speaker.
4.Whatever output we get from smart speaker, we record data from 'mic' by using pyaudio.
5.match the data (Recorded data of 'mic') with validate conditions.

'''

### read a settings file like (ok google | alexa,language,prefered volume)

def testcases(my_list):

	with open('vaf_settings.csv') as csvfile:
		readCSV = csv.DictReader(csvfile, delimiter=",")
		for setting in readCSV:
        	#	print setting
			pass

### read the test cases like ( commands, validation conditions,audio files etc.)

	test_cases = (my_list).split(",")
			
### Execution process ###	

	settings = Vam_settings()	
	settings.vam_reset_smart_speaker(setting['wake_word'],setting['vas_speaker_volume_setting'])

### 1.Here test_cases[1] is text command for asking the smart speaker (the text is converted to speach), 
### 2.test_cases[3] is audio file command.
### 'flag 0' for the text command and 'flag 1' for the voice command

	settings.vam_wake_word_generation(setting['wake_word'])
	if test_cases[3] == 'NULL':
		settings.vam_command_generation(test_cases[1], 0)
	else:
	#	print (test_cases[3])		
		settings.vam_command_generation(test_cases[3], 1)

### check the time | weather| date.
### test_case[6] passes the validate conditions.
### setting['vas_language'] = en-US

	if test_cases[5] == 'vam_record_transcribe':
		subprocess.call(['python', 'vam_record_transcribe.py',test_cases[6],setting['vas_language'],'0'])

### set the reminder 
### test_cases[7] is how much time it will take for reminder.
### test_cases[6] and test_cases[8] are the checking conditions.
	if test_cases[5] == 'vam_alarm_transcribe':
   	        subprocess.call(['python', 'vam_alarm_transcribe.py',test_cases[6],setting['vas_language'],test_cases[7],test_cases[8]]) 

### check the volume condition {for the max}
### test_case[6] is a commnd for ask information
### test_case[7] is a command for set the volume

	if test_cases[5] == 'vam_volume_up':
              	subprocess.call(['python','vam_volume_up.py',test_cases[6],test_cases[7],setting['wake_word']])

### check the volume condition {for the min}		

	if test_cases[5] == 'vam_volume_down':		
		subprocess.call(['python','vam_volume_down.py',test_cases[6],test_cases[7],setting['wake_word']])

### Find the music 
### test_case[6] is music.wav file
### test_case[7] is check the conditions		

	if test_cases[5] == 'vam_record_identify_music':
		subprocess.call(['python','vam_record_identify_music.py',test_cases[6],test_cases[7]])



'''
1. read data from test_cases.csv file
2. deviding the each test case and pass to the "testcases" function
3. according to the validate

'''

if __name__ == '__main__':
	with open('vaf_test_cases.csv') as csvfile2:
		readCSV = csv.reader(csvfile2, delimiter=",")
                for data in readCSV:
			if data is not None:
				test_cases = ",".join(str(test_data) for test_data in data)
				testcases(test_cases)















