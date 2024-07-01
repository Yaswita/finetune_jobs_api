import requests

def test_list_finetune_jobs():
    url = "https://studio.tune.app/tune.Studio/ListFinetuneJobs"
    payload = {
        "auth": {
            "organization": "a0a72721-4bd2-4039-a42e-aa6be9565fee"
            # "cluster": ""
        }
    }
    headers = {
        "X-Tune-Key": "sk-tune-7Y15vdi8OjqQJAae5AjJ7WmJH4kcSlqh6Yg",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)