*** Settings ***
Library         OperatingSystem
Library         String
Library         vam_automate.py

*** Keywords ***

test_case_result
        ${Result}=    Get File    result_file.txt
	Log    ${Result}
        Should Be Equal As Strings    ${Result}    Test case passed...
	

Run_test_cases
    ${TextFileContent}=    Get File    vaf_test_cases.csv
    :FOR  ${data}  IN   ${TextFileContent}
    \   @{lines_of_test_cases}=    Split to lines    ${data}
        :FOR    ${test_data}    IN    @{lines_of_test_cases}
	\       Set tags     test_case-${test_data[0]}
	\       testcases    ${test_data}
	\       test_case_result


mykeyword2
	Log    hiii

mykeyword
	:FOR    ${index}    IN RANGE    10
	\        mykeyword2	



*** Test Cases ***

test file2
	Run_test_cases



 
