import requests

def test_get_finetune_jobs():
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
    if response.status_code == 200:
        data = response.json()

        # Extract the "id" value
        job_id = None
        jobs = data.get('jobs', [])
        if jobs:
            job_id = jobs[0].get('id')

    url = "https://studio.tune.app/tune.Studio/GetFinetuneJob"
    payload = {
        "auth": {
            "organization": "a0a72721-4bd2-4039-a42e-aa6be9565fee",
            # "cluster": "<string>"
        },
        "id": job_id
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        job_name = data["name"]
        print("\n Get finetune job Successful: Job Name -", job_name)
