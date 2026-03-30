*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Simple Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="jsAlert()"]
    Sleep    5s
    Handle Alert

    Sleep    5s
    Close Browser

Confirmation Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="jsConfirm()"]
    Sleep    2s
    # Handle Alert ---> for clicking OK
    # for clicking Cancel:
    Handle Alert    action=DISMISS


    Sleep    5s
    Close Browser

Prompt Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="jsPrompt()"]
    Sleep    2s
    
    # for entering text and clicking OK
#    Input Text Into Alert    daksh

    # for clicking cancel
    Input Text Into Alert    daksh  action=DISMISS

    Sleep    5s
    Close Browser