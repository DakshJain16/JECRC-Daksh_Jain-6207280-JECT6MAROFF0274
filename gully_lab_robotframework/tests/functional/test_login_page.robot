*** Settings ***
Resource    ../../resources/pages/home_page.robot
Resource    ../../resources/pages/login_page.robot
Resource    ../../resources/common_resources.robot

Suite Setup    Load Environment
Test Setup    Open Application   
Test Teardown    Close Application

*** Test Cases ***
TC001 Successful Login
    [Documentation]    checks log in
    [Tags]    functional

    Account Handling
    Sleep    3s

    Login Handling    ${USER_EMAIL}  ${USER_PWD}
    Sleep    3s
    
TC007 Login With Invalid Credentials
    [Documentation]    login with invalid credentials
    [Tags]    negative
    
    Account Handling
    Sleep    3s
    
    Invalid Login Credentials    abcdef    qwerty123
    Sleep    3s