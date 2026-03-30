#Task 3
# 1. Navigate to amazon
# 2. Click on electronic in tab
# 3. Check on 'boat' checkbox
# 4. click on any product before clicking store the name of product
# 5. switch to new window
# 6. assert the product name is present in the new window
# 7. print the actual price, discounted price and the percentage
# 8. scroll to add to cart and click on the button
# 9. click on cart icon on top right corner
# 10. check if same product has been added

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://www.amazon.in/

*** Test Cases ***
end two end
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Wait Until Location Contains    amazon

    Click Element    xpath=//a[contains(t ext(), "Electronics")]
    Sleep    2s
    Click Element    xpath=(//div[@class="a-section a-spacing-none"])[4]/descendant::i[4]
    Sleep    2s

    ${name}  Get Text    xpath=(//h2[@class="a-size-base-plus a-spacing-none a-color-base a-text-normal"])[7]
    Log To Console    Product Name: ${name}

    Click Element    xpath=(//img[@class="s-image"])[7]
    Sleep    2s
    
    @{windows}  Get Window Handles    
    @{titles}  Get Window Titles

    Switch Window    New
    Sleep    2s

    ${page_title}  Get Text    id=productTitle
    Page Should Contain    ${page_title}
    
    ${actual_price}  Get Text    xpath=//span[@class="a-price a-text-price apex-basisprice-value"]/span
    Log To Console    Actual Price: ${actual_price}
    
    ${discounted_price}  Get Text    xpath=//span[@class="apex-savings-container"]/following-sibling::span/span[2]/span[2]
    Log To Console    Discount Price: ${discounted_price}
    
    ${discount_percent}  Get Text    xpath=//span[@class="apex-savings-container"]/span
    Log To Console    Discount Percent: ${discount_percent}

    Scroll Element Into View    xpath=//input[@id="add-to-cart-button"]
    Sleep    2s
    Click Element    xpath=//input[@id="add-to-cart-button"]
    Sleep    2s
    Click Element    xpath=//a[@id="nav-cart"]
    Sleep    2s

    Page Should Contain    ${page_title}

    Close Browser

