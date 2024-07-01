import requests

def test_get_finetune_jobs_with_invalid_job_id():

    url = "https://studio.tune.app/tune.Studio/GetFinetuneJob"
    headers = {
        "X-Tune-Key": "sk-tune-7Y15vdi8OjqQJAae5AjJ7WmJH4kcSlqh6Yg",
        "Content-Type": "application/json"
    }
    payload = {
        "auth": {
            "organization": "a0a72721-4bd2-4039-a42e-aa6be9565fee",
            # "cluster": "<string>"
        },
        "id": "yaswita"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    data = response.json()
    code = data["code"]
    message = data["message"]
    assert response.status_code == 404
    if response.status_code == 404:
        print("\nSuccessful Validation of Invaid Job ID")
        print("Status Code: ", response.status_code)
        print("Error Message: ", message)

