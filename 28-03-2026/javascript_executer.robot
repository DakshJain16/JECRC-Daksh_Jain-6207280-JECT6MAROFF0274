*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://inc.in/

*** Test Cases ***
Handling js
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

# scrolling to the end of page
    Execute Javascript    window.scrollTo(0,document.body.scrollHeight)
    Sleep    2s

# scrolling to the origin
    Execute Javascript    window.scrollTo(0,0)
    Sleep    2s

# scrolling down by 800 pixels from current position
    Execute Javascript    window.scrollBy(0,800)
    Sleep    2s
    
# scrolling up by 400 pixels from current position
    Execute Javascript    window.scrollBy(0,-400)
    Sleep    3s
    Close Browser