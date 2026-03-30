*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Simple Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="myFunctionAlert()"]
    Sleep    2s
    Handle Alert
    Sleep    2s
    
    Close Browser
    
Confirmation Alert Accept
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="myFunctionConfirm()"]
    Sleep    2s
    Handle Alert
    Sleep    2s
    Page Should Contain    You pressed OK!
    
    ${text}  Get Text    id=demo
    Log To Console    ${text}
    Sleep    2s
    Close Browser

Confirmation Alert Dismiss
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="myFunctionConfirm()"]
    Sleep    2s
    Handle Alert  action=DISMISS
    Sleep    2s
    Page Should Contain    You pressed Cancel!

    ${text}  Get Text    id=demo
    Log To Console    ${text}
    Sleep    2s
    Close Browser

Prompt Alert Accept
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="myFunctionPrompt()"]
    Sleep    2s
    Input Text Into Alert    Harry Potter
    Sleep    2s
    Page Should Contain    Hello Harry Potter! How are you today?

    ${text}  Get Text    id=demo
    Log To Console    ${text}
    Sleep    2s
    Close Browser

Prompt Alert Dismiss
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Button    xpath=//button[@onclick="myFunctionPrompt()"]
    Sleep    2s
    Input Text Into Alert    Harry Potter  action=DISMISS
    Sleep    2s
    Page Should Contain    User cancelled the prompt.

    ${text}  Get Text    id=demo
    Log To Console    ${text}
    Sleep    2s
    Close Browser