*** Settings ***
Documentation    Dropdown Practice
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
handle dropdown
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Scroll Element Into View    id=colors

    Page Should Contain List    id=colors

    Select From List By Label    id=colors  Blue
#    Select From List By Label    id=colors  Blue  Red
#    we can give more than one label, index and value with their respective commands
    Sleep    1s
    Select From List By Index    id=colors  3
    Sleep    1s
    Select From List By Value    id=colors  white
    Sleep    1s
    
    @{select_option}=  Get Selected List Labels    id=colors
    Log To Console    ${select_option}

    Sleep    3s
    Close Browser