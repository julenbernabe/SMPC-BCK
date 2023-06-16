import requests
import os

contractaddr = os.popen('cd ../marketplace; truffle networks --network ethereum | grep marketplace').read().split(" ")[-1][:-1]

url = "http://localhost:8060/api/rest/v1/event-filter"      #This url may change when deploying the eventeum repository
newRequest = {
    "id": "newRequest_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "new_campaign", 

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
        "eventName": "updated_campaign", 

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

scientistReady = {
    "id": "scientistReady_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "scientist_ready", 

        # From below uncoment and edit only the needed params of the event that will be listened

        #INDEXED PARAMETERS

        #"indexedParameterDefinitions": [
        #    {"position": 0, "type": "FIRST_ITEM_TYPE(IN CAPITAL LETTERS)"},
        #    {"position": 1, "type": "UINT256"}
        #    ],

        #NON-INDEXED PARAMETERS

        "nonIndexedParameterDefinitions": [
            {"position": 0, "type": "UINT256"},
            {"position": 0, "type": "UINT256"}
        ] 
    },
    "correlationIdStrategy": {
        "type": "NON_INDEXED_PARAMETER",
        "parameterIndex": 0
    }    
}

executionFinished = {
    "id": "executionFinished_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "execution_finished", 

        # From below uncoment and edit only the needed params of the event that will be listened

        #INDEXED PARAMETERS

        #"indexedParameterDefinitions": [
        #    {"position": 0, "type": "FIRST_ITEM_TYPE(IN CAPITAL LETTERS)"},
        #    {"position": 1, "type": "UINT256"}
        #    ],

        #NON-INDEXED PARAMETERS

        "nonIndexedParameterDefinitions": [
            {"position": 0, "type": "UINT256"},
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
        "eventName": "players_filled", 

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

executionReady = {
    "id": "executionReady_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "execution_ready", 

        # From below uncoment and edit only the needed params of the event that will be listened

        #INDEXED PARAMETERS

        #"indexedParameterDefinitions": [
        #    {"position": 0, "type": "FIRST_ITEM_TYPE(IN CAPITAL LETTERS)"},
        #    {"position": 1, "type": "UINT256"}
        #    ],

        #NON-INDEXED PARAMETERS

        "nonIndexedParameterDefinitions": [
            {"position": 0, "type": "UINT256"},
            {"position": 0, "type": "UINT256"}
        ] 
    },
    "correlationIdStrategy": {
        "type": "NON_INDEXED_PARAMETER",
        "parameterIndex": 0
    }    
}

executionSuccessful = {
    "id": "executionSuccessful_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "execution_successful", 

        # From below uncoment and edit only the needed params of the event that will be listened

        #INDEXED PARAMETERS

        #"indexedParameterDefinitions": [
        #    {"position": 0, "type": "FIRST_ITEM_TYPE(IN CAPITAL LETTERS)"},
        #    {"position": 1, "type": "UINT256"}
        #    ],

        #NON-INDEXED PARAMETERS

        "nonIndexedParameterDefinitions": [
            {"position": 0, "type": "UINT256"},
            {"position": 0, "type": "UINT256"}
        ] 
    },
    "correlationIdStrategy": {
        "type": "NON_INDEXED_PARAMETER",
        "parameterIndex": 0
    }    
}

executionFailed = {
    "id": "executionFailed_" + contractaddr,
    "contractAddress": contractaddr,
    "eventSpecification": {
        "eventName": "execution_failed", 

        # From below uncoment and edit only the needed params of the event that will be listened

        #INDEXED PARAMETERS

        #"indexedParameterDefinitions": [
        #    {"position": 0, "type": "FIRST_ITEM_TYPE(IN CAPITAL LETTERS)"},
        #    {"position": 1, "type": "UINT256"}
        #    ],

        #NON-INDEXED PARAMETERS

        "nonIndexedParameterDefinitions": [
            {"position": 0, "type": "UINT256"},
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
scientistReadyPost = requests.post(url, json=scientistReady, headers=headers_dict)
executionFinishedPost = requests.post(url, json=executionFinished, headers=headers_dict)
playersFilledPost = requests.post(url, json=playersFilled, headers=headers_dict)
executionReadyPost = requests.post(url, json=executionReady, headers=headers_dict)
executionSuccessfulPost = requests.post(url, json=executionSuccessful, headers=headers_dict)
executionFailedPost = requests.post(url, json=executionFailed, headers=headers_dict)
print(newRequestPost.content)
print(updatedRequestPost.content)
print(scientistReadyPost.content)
print(executionFinishedPost.content)
print(playersFilledPost.content)
print(executionReadyPost.content)
print(executionSuccessfulPost.content)
print(executionFailedPost.content)
