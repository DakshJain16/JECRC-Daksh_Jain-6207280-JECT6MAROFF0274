*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/logout_loc.robot
Resource    ../../locators/home_page_locators.robot

*** Keywords ***
Logout
    [Documentation]    Logout
    
    Click Element    ${account_icon}
    Sleep    2s
    Click Element    ${logout_link}
    Log    logout
    Sleep    5s

    
    