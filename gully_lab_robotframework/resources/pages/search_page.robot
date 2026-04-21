*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/search_loc.robot

*** Keywords ***
Search Product
    [Documentation]    searching product   
    [Arguments]    ${search_prod}
    
    Click Element    ${search_icon}

    Input Text    ${search_input}    ${search_prod}
    Sleep    2s
    Press Keys    ${search_input}    ENTER
    Sleep    2s

Search Non-Existing Product
    [Documentation]    searching non-existing product
    [Arguments]    ${search_prod}

    Click Element    ${search_icon}

    Input Text    ${search_input}    ${search_prod}
    Sleep    2s
    Press Keys    ${search_input}    ENTER
    Sleep    2s

    Page Should Contain    No results found

        