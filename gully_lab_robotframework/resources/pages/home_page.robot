*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/home_page_locators.robot

*** Keywords ***
Account handling
    [Documentation]    Account
    Click Element    ${account_icon}
    Log    Clicking on account link
    Sleep  2s

Click Home Page
    [Documentation]    clicking home page
    Click Element    ${home_page}
    Log    Clicking home page
    Sleep    2s
