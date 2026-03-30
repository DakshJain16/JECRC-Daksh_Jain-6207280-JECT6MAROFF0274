*** Settings ***
Documentation    handling checkboxes
Library    SeleniumLibrary

*** Variables ***
${url1}  https://the-internet.herokuapp.com/
${url2}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Checkboxes
    [Documentation]    herokuapp checkboxes
    Open Browser    ${url1}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//a[text()="Checkboxes"]
    # Click Element is used for clicking the element
    Page Should Contain Checkbox    xpath=(//input[@type="checkbox"])[1]

    Select Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    2s
    Unselect Checkbox    xpath=(//input[@type="checkbox"])[2]
    Sleep    2s

    Close Browser

Handling Checkboxes2
    [Documentation]    test automation practice
    Open Browser    ${url2}  chrome
    Maximize Browser Window
    Sleep    2s

    # checkboxes
    Select Checkbox    xpath=//input[@id="saturday"]
    Sleep    1s
    Select Checkbox    xpath=//input[@id="wednesday"]
    Sleep    1s
    Select Checkbox    xpath=//input[@id="monday"]
    Sleep    1s

    # radio button
    Click Element    xpath=//input[@id="male"]
    Sleep    1s

    Click Element    xpath=//input[@id="female"]
    Sleep    1s

    Close Browsers



    