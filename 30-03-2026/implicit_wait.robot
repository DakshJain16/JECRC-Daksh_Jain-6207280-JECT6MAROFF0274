*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/

*** Test Cases ***
implicit wait
    Open Browser    ${url}  chrome
    ${before}  Get Selenium Implicit Wait
    Log To Console    ${before}
    
    Set Selenium Implicit Wait    5s

    ${after}  Get Selenium Implicit Wait
    Log To Console    ${after}

    Close Browser
    
# Get Selenium Implicit Wait --> returns you the time of implicit wait
# Set Selenium Implicit Wait --> this keyword lets you set implicit wait, usually in seconds is recommended.
# Set Browser Implicit Wait --> this keyword lets you set implicit wait for one browser instance,
# if there are multiple browsers then it'll be confined to that browser.
