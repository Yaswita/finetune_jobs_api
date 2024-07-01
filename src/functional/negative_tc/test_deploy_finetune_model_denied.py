import requests


def test_deploy_finetune_model_denied():
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

    job_id = None  # Initialize job_id
    if response.status_code == 200:
        data = response.json()
        # Extract job details from the response
        jobs = data.get('jobs', [])
        if jobs:
            job = jobs[0]
            job_id = job.get('id')
            job_name = job.get('name')
            base_model_id = job.get('meta', {}).get('metadata', {}).get('base_model_id')
            dataset_path = job.get('meta', {}).get('training_config', {}).get('datasets', [{}])[0].get('path')
            dataset_type = job.get('meta', {}).get('training_config', {}).get('datasets', [{}])[0].get('type')
            dataset_format = "json"  # Replace with actual format if known
            gpu = job.get('resource', {}).get('gpu')
            gpu_count = job.get('resource', {}).get('gpuCount')
            disk_size = job.get('resource', {}).get('diskSize')
            max_retries = job.get('resource', {}).get('maxRetries')
            status = job.get('status')
            created_at = job.get('createdAt')
            updated_at = job.get('updatedAt')

    if job_id:
        url = "https://studio.tune.app/tune.Studio/DeployFinetuneJob"
        payload = {
            "auth": {
                "organization": "a0a72721-4bd2-4039-a42e-aa6be9565fe",
                # "cluster": "<string>"
            },
            "job": {
                "id": job_id,
                "name": job_name,
                "baseModel": base_model_id,
                "datasets": [
                    {
                        "path": dataset_path,
                        "type": dataset_type,
                        "format": dataset_format
                    }
                ],
                "resource": {
                    "gpu": gpu,
                    "gpuCount": gpu_count,
                    "diskSize": disk_size,
                    "maxRetries": max_retries
                },
                "featureGates": {},
                "trainingConfig": job.get('meta', {}).get('training_config', {}),
                "meta": job.get('meta', {}).get('metadata', {}),
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        status_code = response.status_code
        data = response.json()
        code = data["code"]
        message = data["message"]
        assert response.status_code == 403  # Ensure the deployment is denied
        if response.status_code == 403:
            if code == "permission_denied" and message == "you don't have permission to perform this action":
                print("\nSuccessful Validation of Permission Denied")
                print("Status Code: ", response.status_code)
                print("Error Message: ", message)
    else:
        assert False, "No jobs found to deploy"


