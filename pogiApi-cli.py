# Prerequisite: Python Requests Library - https://docs.python-requests.org/
# - to install: https://docs.python-requests.org/en/master/user/install/#install
import json
import sys
from random import randint

# Import requests library
try:
    import requests
except Exception as ex:
    print("You need to install python's request library to connect to PogiAPI.")
    print("Install instruction is in https://requests.readthedocs.io/en/master/user/install/#install.")
    sys.exit()

# Required Variables
pogi_url = 'https://sandbox.simplyrfid.com/api' # Enter your Pogi server URL here (default: https://sandbox.simplyrfid.com/api)
user_id = '' # Enter your Pogi user ID here
user_pwd = '' # Enter your Pogi password here

# Wrapper class to easily find API calls
class PogiApi:
    @staticmethod
    def _postRequest(apiRequest):
        apiResponse = requests.post(pogi_url, json=apiRequest)
        if apiResponse.status_code == 200:
            return json.loads(apiResponse.text)
        else:
            return None

    @staticmethod
    def getToken(user_id, user_pwd):
        print('Signing in as:', user_id)

        apiResponse = PogiApi._postRequest({
            "op": "token-get",
            "userId": user_id,
            "password": user_pwd
            })
        if apiResponse is None:
            print("There was a problem connecting to the server")
            return None
        elif "token" not in apiResponse:
            print(apiResponse["message"])
            return None
        else:
            print('Log in (via token-get) succesful. User:', user_id)
            return apiResponse["token"]

    @staticmethod
    def postIdCurrent(token):
        apiResponse = PogiApi._postRequest({
            "op": "id-current",
            "token": token
            })
        return apiResponse

    @staticmethod
    def postIdGet(token, tag):
        apiResponse = PogiApi._postRequest({
            "op": "id-get",
            "token": token,
            "tag": tag
            })
        return apiResponse

    @staticmethod
    def postIdDelete(token, tag):
        apiResponse = PogiApi._postRequest({
            "op": "id-delete",
            "token": token,
            "tag": tag
            })
        return apiResponse

    @staticmethod
    def postIdAdd(token):
        payload = {
            "addHistory": "true",
            "op": "id-add",
            "token": token,
            "name": "Test Tag",
            "external_id": "408189-0000000" + str(randint(100, 999)),
            "tagId": "2FAA000000000000000" + str(randint(10000, 99999))
        }
        apiResponse = PogiApi._postRequest(payload)
        return apiResponse
      
    @staticmethod
    def postIdUpdate(token, tag, field, value):
        payload = {
            "addHistory": "true",
            "addMissing": "false",
            "op": "id-update",
            "tagId": tag,
            "token": token,
            field: value
        }
        apiResponse = PogiApi._postRequest(payload)
        return apiResponse

# Ask for action
def inputAction():
    print("\n==================================================")
    print("1. Fetch items (id-current)")
    print("2. Fetch item details (id-get)")
    print("3. Add item (id-add)")
    print("4. Update item (id-update)")
    print("5. Delete item (id-delete)")
    print("0. Exit")
    op = input("Enter op: (0-5): ")
    return op

def displayResponse(apiResponse):
    fmtjson = json.dumps(apiResponse, sort_keys=True, indent=2)
    print(fmtjson)

# =========================================
# Main routine
# =========================================
if __name__ == "__main__":
    if not user_id or not user_pwd:
        print('Missing username and password. Please update the following variables in pogiApi-cli.py:')
        print('1. user_id')
        print('2. user_pwd')
        print('These information should be available on your welcome email.')
        sys.exit()
    token = PogiApi.getToken(user_id, user_pwd)
    if not token:
        sys.exit()
    while True:
        action = inputAction()
        if action == "1":
            apiResponse = PogiApi.postIdCurrent(token)
            displayResponse(apiResponse)
        elif action == "2":
            tag = input("Enter Tag/RFID: ")
            apiResponse = PogiApi.postIdGet(token, tag)
            displayResponse(apiResponse)
        elif action == "3":
            apiResponse = PogiApi.postIdAdd(token)
            displayResponse(apiResponse)
        elif action == "4":
            tag = input("Enter Tag/RFID: ")
            field = input("Enter field: ")
            newValue = input("Enter new value: ")
            apiResponse = PogiApi.postIdUpdate(token, tag, field, newValue)
            displayResponse(apiResponse)
        elif action == "5":
            tag = input("Enter Tag/RFID: ")
            apiResponse = PogiApi.postIdDelete(token, tag)
            displayResponse(apiResponse)
        elif action == "0":
            break
