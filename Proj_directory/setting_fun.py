#[import libraries]

import sys
import os
import time
import csv
import subprocess

class Vam_settings:

### definition for the wake word generation
### here data means wake word

	def vam_wake_word_generation(self,data):
		wake_word = ""
		wake_word = data
        	os.system('echo %s | festival --tts' %wake_word)
		self.vam_inter_command_sleep() ## give delay for processing
### definition for the delay

	def vam_inter_command_sleep(self):
		time.sleep(3)   

### definition for the reset the smart speaker settings

	def vam_reset_smart_speaker(self,wake_word,vol_data):
		vas_speaker_volume_setting = ""
		vas_speaker_volume_setting = vol_data
		self.vam_wake_word_generation(wake_word)
		self.vam_command_generation(vol_data,0)
		self.vam_inter_command_sleep()

### definition for the command generation for the smart speaker
### data means a command

	def vam_command_generation(self,data,flag):
		vam_command = ""
		vam_command = data
		if flag == 0:
			os.system("echo %s | festival --tts" %vam_command)
		else:
			subprocess.call(['aplay',vam_command])


