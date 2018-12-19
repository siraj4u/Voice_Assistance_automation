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




 
