*** Settings ***
Library         OperatingSystem
Library         String
Library         vam_automate1.py

*** Keywords ***


Loop_over_data

    ${TextFileContent}=    Get File    vaf_test_cases.csv

    :FOR  ${data}  IN   ${TextFileContent}
    \   Log    ${data}
    \   @{lines}=    Split to lines    ${data}
    \   Log    ${lines}
        :FOR    ${data2}    IN    @{lines}
    	\   	Log    ${data2}
        \       ${words}=  Split String    ${data2}    ,
        \       Log    ${words[0]}
        \       Run Keyword If  '${words[0]}' == '1'	testcases    ${data2}     
        \       Run Keyword If  '${words[0]}' == '2'	testcases    ${data2}        
        \       Run Keyword If  '${words[0]}' == '3'	testcases    ${words[0]}     
        \       Run Keyword If  '${words[0]}' == '4'	testcases    ${words[0]}     
        \       Run Keyword If  '${words[0]}' == '5'	testcases    ${words[0]}     
        \       Run Keyword If  '${words[0]}' == '6'	testcases    ${words[0]}     
        \       Run Keyword If  '${words[0]}' == '7'	testcases    ${words[0]}     


*** Test Cases ***
test file

     Loop_over_data


 
