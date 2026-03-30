*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
handling windows
    Open Browser  ${url}  chrome
    Maximize Browser Window

    Scroll Element Into View    id=PopUp

    Click Element    id=PopUp

    @{windows}  Get Window Handles
    @{titles}  Get Window Titles
    Log To Console    ${titles}

    Switch Window  NEW
    Log Title
    Log To Console    ${titles}[-1]


    Switch Window  ${windows}[0]
    Log Title
    ${title}  Get Title
    Log To Console    ${title}

    Close Browser
