*** Settings ***
Resource    ../../resources/common_resources.robot
Resource    ../../resources/pages/home_page.robot
Resource    ../../resources/pages/login_page.robot
Resource    ../../resources/pages/search_page.robot
Resource    ../../resources/pages/add_to_cart_page.robot

Suite Setup    Load Environment
Test Setup    Open Application
Test Teardown    Close Application

*** Test Cases ***
TC004 Add Product To Cart
    [Documentation]    testing add to cart
    [Tags]    functional

    Account Handling
    Sleep    2s

    Login Handling    ${USER_EMAIL}  ${USER_PWD}
    Sleep    2s

    Click Home Page

    Search Product    shoes
    Sleep    3s

    Add To Cart

TC005 Verify product added reflects in cart
    [Documentation]    verifying add to cart
    [Tags]    integration

    Account Handling
    Sleep    2s

    Login Handling    ${USER_EMAIL}  ${USER_PWD}
    Sleep    2s

    Click Home Page

    Search Product    shoes
    Sleep    3s

    Verify Cart