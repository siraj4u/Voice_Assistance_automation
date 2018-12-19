import subprocess
import csv


with open('vaf_test_cases.csv') as csvfile2:
                readCSV = csv.reader(csvfile2, delimiter=",")
                fileb = open('robot_base.robot', 'r')
                file1 = open('vam_automate_generate.robot','w')
                file1.write(fileb.read())
		fileb.close()
                i = 1
                for data in readCSV:
                        if data is not None:
                                test_cases = ",".join(str(test_data) for test_data in data)
				#print test_cases

                                file1.write('test case')
                                file1.write(str(i))
                                file1.write('\n')
                                file1.write('   testcases   ')
                                file1.write(test_cases)
				file1.write('\n')
				file1.write('   test_case_result')
				file1.write('\n')
				test_cases = (test_cases).split(",")

				#print test_cases[5]
				if test_cases[5] == 'vam_record_transcribe':
					file1.write('   [Tags]   Text_Match')
				elif test_cases[5] == 'vam_volume_up' or test_cases[5] == 'vam_volume_down' :
					file1.write('   [Tags]   volume_checker')
				elif test_cases[5] == 'vam_record_identify_music':
					file1.write('   [Tags]   music_identifier')
				elif test_cases[5] == 'vam_alarm_transcribe':
					file1.write('   [Tags]   Alarm reminder')
				#file1.write(str(i))
                                file1.write('\n\n')
                                i = i + 1
                file1.close()
