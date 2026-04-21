*** Settings ***
Resource    ../../resources/common_resources.robot
Resource    ../../resources/pages/login_page.robot
Resource    ../../resources/pages/home_page.robot
Resource    ../../resources/pages/logout_page.robot

Suite Setup    Load Environment
Test Setup    Open Application
Test Teardown    Close Application

*** Test Cases ***
TC002 Logout Functionality
    [Documentation]    Logout of account
    [Tags]    functional
    
    Account Handling
    Login Handling    ${USER_EMAIL}    ${USER_PWD}
    Sleep    2s

    Logout