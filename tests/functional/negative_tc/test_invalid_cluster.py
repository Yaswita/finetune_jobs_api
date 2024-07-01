import requests

def test_invalid_tune_key():
    url = "https://studio.tune.app/tune.Studio/ListFinetuneJobs"
    payload = {
        "auth": {
            "organization": "a0a72721-4bd2-4039-a42e-aa6be9565fee",
            "cluster": "random"
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
    assert response.status_code == 401
    if response.status_code == 401:
        if code == "unauthenticated" and message == "rpc error: code = Unauthenticated desc = invalid cluster random":
            print("\nSuccessful Validation of Invaid Tune Key")
            print ("Status Code: ",response.status_code)
            print("Error Message: ",message)
