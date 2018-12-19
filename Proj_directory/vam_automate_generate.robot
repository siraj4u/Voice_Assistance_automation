*** Settings ***
Library         OperatingSystem
Library         String
Library         vam_automate.py

*** Keywords ***

test_case_result
        ${Result}=    Get File    result_file.txt
	Log    ${Result}
        Should Be Equal As Strings    ${Result}    Test case passed...
	


*** Test Cases ***




 
test case1
   testcases   1,what is the weather in bangalore,1,NULL,1,vam_record_transcribe,weather;rain;bengaluru;bangalore;cloudy;thunderstorms;temperature;forecast,Right now in Bengaluru cloudy,Its raining in Bengaluru,Pass,Its raining in,weather.wav,1
   test_case_result
   [Tags]   Text_Match

test case2
   testcases   2,set the volume to thirty percent,1,NULL,1,vam_volume_up,tell me about california,set the volume to ninety percent
   test_case_result
   [Tags]   volume_checker

test case3
   testcases   3,what is the date today,1,NULL,1,vam_record_transcribe,2018;wednesday;thursday;friday;monday;tuesday,it will tell today date,Pass
   test_case_result
   [Tags]   Text_Match

test case4
   testcases   7,play lungi dance on gaana,1,my_command.wav,1,vam_record_identify_music,songtitle.wav,yo yo honey singh;lungi dance,
   test_case_result
   [Tags]   music_identifier

