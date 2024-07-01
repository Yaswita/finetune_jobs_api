# import requests
# import json
# def test_create_finetune_job():
#     url = "https://studio.tune.app/tune.Studio/CreateFinetuneJob"
#
#     payload = {
#         "auth": {
#             "organization": "a0a72721-4bd2-4039-a42e-aa6be9565fee",
#         },
#         "job": {
#             "name": "my-llama",
#             "baseModel": "llama2-07b-base",
#             "datasets": [
#                 {
#                     "path": "vicgalle/alpaca-gpt4",
#                     "type": "alpaca",
#                 }
#             ],
#             "resource": {
#                 "gpu": "nvidia-l4",
#                 "gpuCount": "1",
#                 "diskSize": "30Gi",
#                 "maxRetries": 123
#             },
#             "trainingConfig": {
#                 "num_epochs": 3,
#                 "learning_rate": 0.00002
#             },
#             "meta": {
#                 "quantization": "QUANTIZATION_UNSPECIFIED",
#                 "IsModelMergeJob": True
#             }
#         }
#     }
#
#     headers = {
#         "X-Tune-Key": "sk-tune-7Y15vdi8OjqQJAae5AjJ7WmJH4kcSlqh6Yg",
#         "Content-Type": "application/json"
#     }
#
#     response = requests.post(url, json=payload, headers=headers)
#     print("\n",response.text)
#     assert response.status_code == 200  # Adjust the status code as per your API's expected response
#     assert "success" in response.json()  # Adjust the expected response content as per your API's response
