# Explanation:
## Locust Integration: 
- MyUser inherits from HttpUser, which is a base class provided by Locust for HTTP user simulation.
## Task Definition: 
-@task decorator defines a task that simulates a user action. In this case, list_finetune_jobs sends a POST request to url with specified payload and headers.
## Wait Time: 
- wait_time = between(5, 9) specifies a random wait time between 5 and 9 seconds before each task execution,simulating user think time.
## Request Execution: 
-self.client.post is used to send HTTP requests instead of requests.post, as Locust provides its own client for load testing.

# Running Locust:
- To run Locust, save the above code to a file named test_performance.py, and then execute the following command in your terminal: locust -f test_performance.py
- This command starts a web server on http://localhost:8089 where you can configure the number of users to simulate and the hatch rate (how many users to spawn per second). You can then start the test and monitor results through the web interface.