*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary

*** Variables ***
${BASE_URL}    https://petstore.swagger.io/v2

*** Test Cases ***
Add Pet
   [Documentation]    add a new pet to the store
    Create Session    petapi    ${BASE_URL}    verify=True
    ${payload}=    Load Json From File    ${CURDIR}/../data/add_pet.json
    # Load Json From File --> load all json files in the path we give
    
    ${response}=    POST On Session    petapi    /pet    json=${payload}
    
    Should Be Equal As Integers    ${response.status_code}    200
    
    Log To Console    ${response.json()}

Update Pet
   [Documentation]    update an existing pet in the store
    Create Session    petapi    ${BASE_URL}    verify=True
    ${payload}=    Load Json From File    ${CURDIR}/../data/update_pet.json

    ${response}=    PUT On Session    petapi    /pet    json=${payload}

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

    Set Suite Variable    ${PET_ID}    ${response.json()}[id]

Get Pet By Id
   [Documentation]    get pet by id
    Create Session    petapi    ${BASE_URL}    verify=True

    ${response}=    GET On Session    petapi    /pet/${PET_ID}

    Should Be Equal As Integers    ${response.status_code}    200

    Log To Console    ${response.json()}

Find Pet By Status
    [Documentation]    find pets by status
    Create Session    petapi    ${BASE_URL}    verify=True
    
    ${qp}=    Create Dictionary    status=available
    # create query parameter to find pets by status
    
   ${response}=    GET On Session    petapi    /pet/findByStatus    params=${qp}

   Should Be Equal As Integers    ${response.status_code}    200

   Log To Console    ${response.json()}
   
Upload Pet Image
    [Documentation]    upload an image for a pet
    Create Session    petapi    ${BASE_URL}    verify=True
    
    ${form_data}=    Create Dictionary    additionalMetadata=Bruno's img
    ${file_path}=    Set Variable    ${CURDIR}/../data/pet_img.jpeg
    ${file}=    Evaluate    {'file': open($file_path, 'rb')}

    ${response}=    POST On Session    petapi    /pet/55/uploadImage
    ...    data=${form_data}
    ...    files=${file}

    Should Be Equal As Integers    ${response.status_code}    200

Update Pet With Form Data
    [Documentation]    update a pet with form data
    Create Session    petapi    ${BASE_URL}    verify=True

    ${form_data}=    Create Dictionary    
    ...    petId=55
    ...    name=Bella    
    ...    status=sold

    ${response}=    POST On Session    petapi    /pet/55    data=${form_data}

    Should Be Equal As Integers    ${response.status_code}    200

Delete Pet By Id
    [Documentation]    delete pet by id
    Create Session    petapi    ${BASE_URL}    verify=True

    ${response}=    DELETE On Session    petapi    /pet/55

    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.status_code}
