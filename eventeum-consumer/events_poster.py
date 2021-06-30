import requests
contractaddr = '0x3Ff035c4d94Bf59FdDeB779e7cC7deFB71f9F639'

url = "http://localhost:8060/api/rest/v1/event-filter"      #This url may change when deploying the eventeum repository
newRequest = {
    "id": "newRequest_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "newRequest", 

        # From below uncoment and edit only the needed params of the event that will be listened

        #INDEXED PARAMETERS

        #"indexedParameterDefinitions": [
        #    {"position": 0, "type": "FIRST_ITEM_TYPE(IN CAPITAL LETTERS)"},
        #    {"position": 1, "type": "UINT256"}
        #    ],

        #NON-INDEXED PARAMETERS

        "nonIndexedParameterDefinitions": [
            {"position": 0, "type": "UINT256"},
            {"position": 1, "type": "STRING"}
        ] 
    },
    "correlationIdStrategy": {
        "type": "NON_INDEXED_PARAMETER",
        "parameterIndex": 0
    }    
}

updatedRequest = {
    "id": "updatedRequest_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "updatedRequest", 

        # From below uncoment and edit only the needed params of the event that will be listened

        #INDEXED PARAMETERS

        #"indexedParameterDefinitions": [
        #    {"position": 0, "type": "FIRST_ITEM_TYPE(IN CAPITAL LETTERS)"},
        #    {"position": 1, "type": "UINT256"}
        #    ],

        #NON-INDEXED PARAMETERS

        "nonIndexedParameterDefinitions": [
            {"position": 0, "type": "UINT256"},
            {"position": 1, "type": "STRING"}
        ] 
    },
    "correlationIdStrategy": {
        "type": "NON_INDEXED_PARAMETER",
        "parameterIndex": 0
    }    
}

operationThrown = {
    "id": "operationThrown_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "operationThrown", 

        # From below uncoment and edit only the needed params of the event that will be listened

        #INDEXED PARAMETERS

        #"indexedParameterDefinitions": [
        #    {"position": 0, "type": "FIRST_ITEM_TYPE(IN CAPITAL LETTERS)"},
        #    {"position": 1, "type": "UINT256"}
        #    ],

        #NON-INDEXED PARAMETERS

        "nonIndexedParameterDefinitions": [
            {"position": 0, "type": "UINT256"}
        ] 
    },
    "correlationIdStrategy": {
        "type": "NON_INDEXED_PARAMETER",
        "parameterIndex": 0
    }    
}

operationFinished = {
    "id": "operationFinished_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "operation_finished", 

        # From below uncoment and edit only the needed params of the event that will be listened

        #INDEXED PARAMETERS

        #"indexedParameterDefinitions": [
        #    {"position": 0, "type": "FIRST_ITEM_TYPE(IN CAPITAL LETTERS)"},
        #    {"position": 1, "type": "UINT256"}
        #    ],

        #NON-INDEXED PARAMETERS

        "nonIndexedParameterDefinitions": [
            {"position": 0, "type": "UINT256"}
        ] 
    },
    "correlationIdStrategy": {
        "type": "NON_INDEXED_PARAMETER",
        "parameterIndex": 0
    }    
}

playersFilled = {
    "id": "playersFilled_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "playersFilled", 

        # From below uncoment and edit only the needed params of the event that will be listened

        #INDEXED PARAMETERS

        #"indexedParameterDefinitions": [
        #    {"position": 0, "type": "FIRST_ITEM_TYPE(IN CAPITAL LETTERS)"},
        #    {"position": 1, "type": "UINT256"}
        #    ],

        #NON-INDEXED PARAMETERS

        "nonIndexedParameterDefinitions": [
            {"position": 0, "type": "UINT256"}
        ] 
    },
    "correlationIdStrategy": {
        "type": "NON_INDEXED_PARAMETER",
        "parameterIndex": 0
    }    
}

operationStarted = {
    "id": "operationStarted_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "operation_started", 

        # From below uncoment and edit only the needed params of the event that will be listened

        #INDEXED PARAMETERS

        #"indexedParameterDefinitions": [
        #    {"position": 0, "type": "FIRST_ITEM_TYPE(IN CAPITAL LETTERS)"},
        #    {"position": 1, "type": "UINT256"}
        #    ],

        #NON-INDEXED PARAMETERS

        "nonIndexedParameterDefinitions": [
            {"position": 0, "type": "UINT256"}
        ] 
    },
    "correlationIdStrategy": {
        "type": "NON_INDEXED_PARAMETER",
        "parameterIndex": 0
    }    
}

networkReady = {
    "id": "networkReady_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "network_ready", 

        # From below uncoment and edit only the needed params of the event that will be listened

        #INDEXED PARAMETERS

        #"indexedParameterDefinitions": [
        #    {"position": 0, "type": "FIRST_ITEM_TYPE(IN CAPITAL LETTERS)"},
        #    {"position": 1, "type": "UINT256"}
        #    ],

        #NON-INDEXED PARAMETERS

        "nonIndexedParameterDefinitions": [
            {"position": 0, "type": "UINT256"}
        ] 
    },
    "correlationIdStrategy": {
        "type": "NON_INDEXED_PARAMETER",
        "parameterIndex": 0
    }    
}

# The part below is fixed

headers_dict = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "Postman-Token": "616712a3-bf11-bbf5-b4ac-b82835779d51"
}

newRequestPost = requests.post(url, json=newRequest, headers=headers_dict)
updatedRequestPost = requests.post(url, json=updatedRequest, headers=headers_dict)
operationThrownPost = requests.post(url, json=operationThrown, headers=headers_dict)
operationFinishedPost = requests.post(url, json=operationFinished, headers=headers_dict)
playersFilledPost = requests.post(url, json=playersFilled, headers=headers_dict)
operationStartedPost = requests.post(url, json=operationStarted, headers=headers_dict)
networkReadyPost = requests.post(url, json=networkReady, headers=headers_dict)
print(newRequestPost.content)
print(updatedRequestPost.content)
print(operationThrownPost.content)
print(operationFinishedPost.content)
print(playersFilledPost.content)
print(operationStartedPost.content)
print(networkReadyPost.content)
