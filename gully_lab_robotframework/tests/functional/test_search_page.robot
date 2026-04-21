*** Settings ***
Resource    ../../resources/common_resources.robot
Resource    ../../resources/pages/search_page.robot
Resource    ../../resources/pages/login_page.robot
Resource    ../../resources/pages/home_page.robot

Suite Setup    Load Environment
Test Setup    Open Application
Test Teardown    Close Application

*** Test Cases ***
TC003 Search Product
    [Documentation]    Search for a product
    [Tags]    functional

    Account Handling
    Sleep    2s

    Login Handling    ${USER_EMAIL}  ${USER_PWD}
    Sleep    2s

    Click Home Page

    Search Product    shoes
    Sleep    3s

TC008 Search Non-existing Product
    [Documentation]    searching non-existing product
    [Tags]    negative
    
    Account Handling
    Sleep    2s
    
    Login Handling    ${USER_EMAIL}  ${USER_PWD}
    Sleep    2s

    Click Home Page

    Search Non-Existing Product    abc
    Sleep    2s

