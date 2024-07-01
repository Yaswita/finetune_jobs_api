import requests

def test_invalid_organisation():
    url = "https://studio.tune.app/tune.Studio/ListFinetuneJobs"
    payload = {
        "auth": {
            "organization": "yaswita-a0a72721-4bd2-4039-a42e-aa6be9565fee"
            # "cluster": ""
        }
    }
    headers = {
        "X-Tune-Key": "sk-tune-7Y15vdi8OjqQJAae5AjJ7WmJH4kcSlqh6Yg",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    code = data ["code"]
    message = data["message"]
    assert response.status_code == 403
    if response.status_code == 403:
        if code == "permission_denied" and message == "you don't have permission to perform this action":
            print("\nSuccessful Validation of Invaid Organisation")
            print ("Status Code: ",response.status_code)
            print("Error Message: ",message)
