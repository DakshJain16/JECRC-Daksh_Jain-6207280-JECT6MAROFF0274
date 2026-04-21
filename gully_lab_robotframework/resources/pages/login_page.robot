*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/login_page_loc.robot

*** Keywords ***
Login Handling
    [Documentation]    Login
    [Arguments]    ${email}  ${pwd}
    
    Click Element    ${email_field}
    Log    clicking on account email
    Input Text    ${email_field}  ${email}
    Sleep    2s

    Click Element    ${password_field}
    Log    clicking on password
    Input Text    ${password_field}  ${pwd}
    Sleep    2s

    Click Button    ${sign_in_btn}
    Log    clicking on sign in button
    Sleep    2s

    Page Should Contain    Account
    Page Should Contain    Log out

Invalid Login Credentials
    [Documentation]    Invalid Login
    [Arguments]    ${email}  ${pwd}

    Click Element    ${email_field}
    Log    clicking on account email
    Input Text    ${email_field}  ${email}
    Sleep    2s

    Click Element    ${password_field}
    Log    clicking on password
    Input Text    ${password_field}  ${pwd}
    Sleep    2s

    Click Button    ${sign_in_btn}
    Log    clicking on sign in button
    Sleep    2s

    Page Should Contain    Incorrect email or password.
