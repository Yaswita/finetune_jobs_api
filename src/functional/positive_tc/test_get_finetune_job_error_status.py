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
        jobs = data.get('jobs', [])
        if jobs:
            job_id = jobs[0].get('id')
            job_status = jobs[0].get('status')
            job_name = jobs[0].get('name')
    if job_status in ("PROVISIONING","ACTIVE","DONE","TERMINATED","KILLED"):
        print("\nPassed")
        print("\nJob Name: "+job_name+"\nJob Status: "+job_status)
    elif job_status == "ERROR":
        print("\nAn error occurred during the fine-tuning process. Check the job logs to identify the cause of the error and troubleshoot accordingly")
