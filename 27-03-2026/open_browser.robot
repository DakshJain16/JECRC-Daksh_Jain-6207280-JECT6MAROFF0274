# structure of robot file
# *** Settings ***
#
# *** Variables ***
#
# *** Test Cases ***
#
# *** Keywords ***
#

*** Settings ***
Documentation  Opening of Browsers
Library  SeleniumLibrary

# three types of variables:
# 1. scalar variables - ${url}  https://www.cricbuzz.com/
# 2. list variables - @{}
# 3. dictionary variables- &{}

*** Variables ***
# scalar variables
${url}  https://www.cricbuzz.com/ 

# list variables
@{bikes}  ktm  kwasaki  honda  pulsar

# dictionary variables
&{cars}  nissan=gtr  honda=civic  bmw=m5
*** Test Cases ***
Opening Chrome Browser
    [Documentation]  Chrome Browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  chrome

    Maximize Browser Window

    Log  navigated to cricbuzz
#    Log To Console  navigated to cricbuzz
    Log To Console    ${bikes}[1]
    Log To Console    ${cars.nissan}
    Sleep  3s

    # here for sleep we can give it in formats like
    # Sleep 3s  --> good practice
    # Sleep 3  --> by default, seconds
    # Sleep 5 minutes  --> can use minutes also
    # Sleep 5 minutes 3s

    Close Browser

    # we have 3 different methods for closing browser:-
    # Close Window
    # Close Browser
    # Close All Browsers

Opening Firefox Browser
    [Documentation]  Chrome Browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  firefox
    Maximize Browser Window

    Log  navigated to cricbuzz
    Log To Console  navigated to cricbuzz
    Sleep  3s

    # Close Browser

Opening Edge Browser
    [Documentation]  Chrome Browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  edge
    Maximize Browser Window

    Log  navigated to cricbuzz
    Log To Console  navigated to cricbuzz
    Sleep  3s

    # Close Browser
    Close All Browsers

# we use command robot -d reports -t "testcase_name" filename.robot to run a specific test case
# for example-  robot -d reports -t "Opening Chrome Headless Browser" open_browser.robot
Opening Chrome Headless Browser
    # headless mode runs for chrome and firefox bowsers not for edge
    [Documentation]  Chrome headless Browser navigating to https://www.cricbuzz.com/
    # [Tags] are used for grouping test cases
    # for running test cases grouped under a tag use command: robot -d reports -i "smoke" open_browser.robot
    # robot -d reports -i/-e "tag_name" filename.robot  ---> command to run for tags
    # here '-i' means include --> for including the test cases grouped under tag
    # use '-e' to exclude a group
    [Tags]    smoke
    # smoke, functional, integration, regression --> Tags
    Open Browser  https://www.cricbuzz.com/  headlesschrome
    Maximize Browser Window

    Log  navigated to cricbuzz
    Log To Console  navigated to cricbuzz
    Sleep  3s

    Close Browser

Opening Edge Browser
    Open Edge Browser

*** Keywords ***
Open Edge Browser
    [Documentation]  Chrome Browser navigating to https://www.cricbuzz.com/
    [Tags]    smoke
    Open Browser  ${url}  edge
    Maximize Browser Window

    Log  navigated to cricbuzz
    Log To Console  navigated to cricbuzz
    Sleep  3s

    Close Browser