*** Settings ***
Documentation    handling dropdowns
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${browser}  chrome
*** Test Cases ***
handle dropdown
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    Click Element    xpath=//a[text()="Dropdown"]

# assert to check if list of dropdown elements is present or not
    Page Should Contain List    id=dropdown
    
    ${options}=  Get List Items    id=dropdown
    Log To Console    ${options}

#Select From List By Label --> takes two arguments: locator, inner text/label
    Select From List By Label    id=dropdown  Option 1
    
    ${select_option}=  Get Selected List Label    id=dropdown
    Log To Console    ${select_option}

    List Selection Should Be    id=dropdown  Option 1
    Sleep    3s

    Close Browser

# robot -d reports -v browser:"edge" dropdown.robot  ---> cross browser testing
# -v --> stands for variables; if we need to change the variable at runtime then the above
# command is used.
