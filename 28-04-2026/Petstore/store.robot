*** Settings ***
Library    RequestsLibrary
# to interact with api, we use request library; it consists of keywords to interact with api.
Library    Collections
# Collections used to validate dictionaries, lists, etc

*** Variables ***
${BASE_URL}    https://petstore.swagger.io/v2

*** Test Cases ***
Pet inventories
    [Documentation]    get pet inventories by status
    Create Session    petapi    ${BASE_URL}    verify=True
    # create a session, verify=True is for ssl verification --> it removes the warning message 
    # for ssl certificate, if we set it to false, it will not verify the ssl certificate and it 
    # will not remove the warning message.
    
    ${response}=    GET On Session    petapi    /store/inventory
    # response object --> store response in variable --> form of raw string
    
    Should Be Equal As Integers    ${response.status_code}    200
    # validate status code
    
    ${body}=    Set Variable    ${response.json()}
    # doing json parsing, convert raw string to dictionary
    
    Log To Console    ${body}
    Log To Console    ${response.status_code}
    
Place Order
    [Documentation]    place an order for a pet
    Create Session    petapi    ${BASE_URL}    verify=True
    
    ${payload}=    Create Dictionary
    ...    id=12345
    ...    petId=54321
    ...    quantity=1
    ...    shipDate=2026-04-28T06:56:01.396Z
    ...    status=placed
    ...    complete=true
    
    ${response}=    POST On Session    petapi    /store/order    json=${payload}
    # post request to place an order, json=payload is used to send the payload in json format
    
    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=    Set Variable    ${response.json()}
    
    Should Be Equal As Integers    ${body}[id]    12345
    Should Be Equal As Strings    ${body}[status]    placed
    
    Log To Console    ${body}
    Log To Console    ${response.status_code}
    
    Set Suite Variable    ${ORDER_ID}    ${body}[id]
    # set suite variable to use it in other test cases, we can use ${ORDER_ID
    
Get Order By Id
    [Documentation]    get order by id
    Create Session    petapi    ${BASE_URL}    verify=True
    
    # when one api is required to work on other api, it is called api chaining
    # we connect these apis using suite variable, we can use the order id from the previous 
    # test case to get the order details in this test case.
    
    ${response}=    GET On Session    petapi    /store/order/${ORDER_ID}
    
    Log To Console    ${response.status_code}
    Log To Console    ${response.json()}

Delete Order By Id
    [Documentation]    delete order by id
    Create Session    petapi    ${BASE_URL}    verify=True

    ${response}=    DELETE On Session    petapi    /store/order/${ORDER_ID}

    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.status_code}
    
E2E
    Create Session    e2eapi    ${BASE_URL}    verify=True
    ${payload}=    Create Dictionary
    ...    id=12345
    ...    petId=54321
    ...    quantity=1
    ...    shipDate=2026-04-28T06:56:01.396Z
    ...    status=placed
    ...    complete=true
    
    ${res1}=    POST On Session    e2eapi    /store/order    json=${payload}
    
    Should Be Equal As Integers    ${res1.status_code}    200
    ${body}=    Set Variable    ${res1.json()}
    Set Suite Variable    ${ORDER_ID}    ${body}[id]
    
    Log To Console    Created an order
    
    ${res2}=    GET On Session    e2eapi    /store/order/${ORDER_ID}
    
    Should Be Equal As Integers    ${res2.status_code}    200
    
    Log To Console    Got the order by id
    
    ${res3}=    DELETE On Session    e2eapi    /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${res3.status_code}    200

    Log To Console    e2e successful