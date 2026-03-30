*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling single iframe
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    
    Select Frame    id=singleframe
    
    Input Text    xpath=//input[@type="text"]  Min
    Sleep    2s
    
    Unselect Frame
    Close Browser
    
Handling multiple iframes
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Element    xpath=//ul[@class="nav nav-tabs "]/descendant::a[text()="Iframe with in an Iframe"]
    Sleep    2s

    Select Frame    xpath=//iframe[@src="MultipleFrames.html"]
    Log To Console    xpath=//h5
    Select Frame    xpath=//div[@class="iframe-container"]/iframe
    Input Text    //input[@type="text"]    text
    Sleep    2s
    Unselect Frame  #switches to default

    Close Browser