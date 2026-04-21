*** Variables ***
${product_card}  xpath=(//div[@class="secondary"])[1]/picture/img
${size}  xpath=//label[contains(text(), "UK 10")]
${gender}  xpath=//a[@onclick="showGenderCollection('mens')"]
${quantity}  xpath=//button[@name="plus"]
${add_to_cart}  xpath=//button[@name="add"]
${cart_icon}  xpath=//button[@aria-label="Cart"]