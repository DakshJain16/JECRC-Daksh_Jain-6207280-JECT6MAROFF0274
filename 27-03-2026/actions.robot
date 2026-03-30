*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
    
*** Test Cases ***
Handling drag and drop
    [Documentation]    handling drag and drop on herokuapp
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[text()="Drag and Drop"]
    Sleep    2s

    Drag And Drop    id=column-a  id=column-b
    Sleep    2s

    Close Browser
    
Handling Mouse Hover
    [Documentation]    handling hovers on herokuapp
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[text()="Hovers"]
    Sleep    2s

    Mouse Over    xpath=//h5[text()="name: user2"]/ancestor::div[@class="figure"]
    Sleep    2s
    Close Browser

Scroll to the element
    [Documentation]    scrolling on herokuapp
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Scroll Element Into View    xpath=//a[text()="Typos"]
    Sleep    2s
    Close Browser
