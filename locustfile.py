from locust import HttpUser, task, between


class TestUser(HttpUser):
    wait_time = between(1, 1)

    @task
    def runner(self):
        self.client.get(f'http://{ip_address}:8000/real')
