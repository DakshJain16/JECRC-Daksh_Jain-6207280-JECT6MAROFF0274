*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/windows

*** Test Cases ***
handling windows
    Open Browser   ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Element    xpath=//a[@href="/windows/new"]
    Sleep    2s

    @{windows}  Get Window Handles
    @{titles}   Get Window Titles
    Log To Console    ${titles}

    Switch Window  NEW  #switches to latest window opened( index = -1)
    Sleep    2s
    Page Should Contain    New Window

    Page Should Contain Element    xpath=//h3[text()="New Window"]

    Switch Window  ${windows}[0]
    Sleep    2s
    Close Browser