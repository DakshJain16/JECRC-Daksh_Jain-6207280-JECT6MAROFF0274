*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/cart_loc.robot

*** Keywords ***
Add To Cart
    [Documentation]    add to cart functionality
    
    Click Element    ${product_card}
    Sleep    2s
    
    Click Element    ${gender}
    Sleep    2s
    
    Click Element    ${size}
    Sleep    2s
    
    Click Button    ${quantity}
    Sleep    2s
    
    Click Button    ${add_to_cart}
    Sleep    2s
    
Verify Cart
    [Documentation]    verifying add to cart functionality
    
    Click Element    ${product_card}
    Sleep    2s
    
    Click Element    ${gender}
    Sleep    2s
    
    Click Element    ${size}
    Sleep    2s
    
    Click Button    ${quantity}
    Sleep    2s
    
    Click Button    ${add_to_cart}
    Sleep    5s
    
    Click Button    ${cart_icon}

    Page Should Not Contain    Your cart is empty