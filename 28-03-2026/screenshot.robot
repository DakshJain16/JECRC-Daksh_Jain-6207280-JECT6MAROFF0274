*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
handling screenshots
    Set Screenshot Directory    ${CURDIR}/Screenshots

    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    5s

    Capture Page Screenshot    fullpage.png
    Sleep    2s

    Scroll Element Into View    xpath=//div[text()="Dhurandhar The Revenge"]
    Capture Element Screenshot    xpath=//img[@alt="Dhurandhar The Revenge"]  dhurandhar.png
    Sleep    2s

    Close Browser

