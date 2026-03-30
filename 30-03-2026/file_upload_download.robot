*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${check_downloaded}  /Users/dakshjain/Downloads/file.txt
*** Test Cases ***
handling upload
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[@href="/upload"]
    Sleep    2s
    
    ${path}  Normalize Path    ${CURDIR}/sample.txt
    
#    Choose File    id=file-upload  /Users/dakshjain/PycharmProjects/30-03-2026/sample.txt

    Choose File    id=file-upload  ${path}
    Sleep    2s
    Click Button    id=file-submit
    Sleep    2s
    
    Close Browser
    
handling download
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Element    xpath=//a[@href="/download"]
    Sleep    2s
    
    Click Element    xpath=//a[@href="download/file.txt"]
    
    Wait Until Created    ${check_downloaded}  timeout=10s
    
    File Should Exist    ${check_downloaded}

    Log To Console    it downloaded successfully
    
    Close Browser