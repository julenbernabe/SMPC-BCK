import requests

contractaddr = '0x3Ff035c4d94Bf59FdDeB779e7cC7deFB71f9F639'

requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "newRequest_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "updatedRequest_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "operationThrown_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "operationFinished_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "playersFilled_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "operationStarted_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "networkReady_" + contractaddr)