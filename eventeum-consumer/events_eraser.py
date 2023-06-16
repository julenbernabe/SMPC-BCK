import requests
import os

contractaddr = os.popen('cd ../marketplace; truffle networks --network ethereum | grep marketplace').read().split(" ")[-1][:-1]

requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "newRequest_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "updatedRequest_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "scientistReady_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "executionFinished_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "playersFilled_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "executionReady_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "executionSuccessful_" + contractaddr)
requests.delete("http://localhost:8060/api/rest/v1/event-filter/" + "executionFailed_" + contractaddr)