import os
import subprocess

### list object declared
score = list()

'''
the defferent amplitude levels of data can be stored in "vol_record_file.txt"
and we read that file calculate the respective amplitude levels
'''

subprocess.call(['rm','result_file.txt'])
with open("vol_record_file.txt", "r") as f:
  for line in f:
    score.append(str(line.strip()))
print("Maximum Amplitude is  ::  %s" %score[0])
print("Minimum Amplitude is  ::  %s" %score[1])

if (float)(score[0]) > (float)(score[1]) :
	print ("Test case pass")
	os.system('echo "test case passed" | festival --tts')
        outfile =  open ("result_file.txt","w+")
        outfile.write('Test case passed...')
        outfile.close()

else:
	print("Test case failed")
	os.system('echo "ohh its failed" | festival --tts')
        outfile =  open ("result_file.txt","w+")
        outfile.write('Test case failed...')
        outfile.close()



