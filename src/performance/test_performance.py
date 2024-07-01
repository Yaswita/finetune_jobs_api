from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(5, 9)  # simulated user wait time between requests

    @task
    def list_finetune_jobs(self):
        url = "https://studio.tune.app/tune.Studio/ListFinetuneJobs"
        payload = {
            "auth": {
                "organization": "a0a72721-4bd2-4039-a42e-aa6be9565fee"
            }
        }
        headers = {
            "X-Tune-Key": "sk-tune-7Y15vdi8OjqQJAae5AjJ7WmJH4kcSlqh6Yg",
            "Content-Type": "application/json"
        }
        # Use self.client to send requests instead of requests.post
        response = self.client.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print("Status Code:", response.status_code)
            print("Response Text:", response.text)
        else:
            print("failure")