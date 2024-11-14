import time

class Container:
    def __init__(self):  # Corrected to __init__
        self.creation_time = time.time()  # When the container was created
        self.last_used_time = time.time()  # Last time the container was used
        self.status = "idle"  # Status can be 'idle', 'executing', or 'released'

    def update_usage(self):
        self.last_used_time = time.time()  # Update the last used time

class Worker:
    def __init__(self, worker_id):  # Corrected to __init__
        self.worker_id = worker_id
        self.containers = []  # List of containers in this worker

    def add_container(self, container):
        self.containers.append(container)
