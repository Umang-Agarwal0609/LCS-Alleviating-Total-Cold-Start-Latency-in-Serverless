from container import Worker, Container
import time

class Scheduler:
    def __init__(self):
        self.worker_pool = {}  # Holds worker_id -> Worker mapping

    def add_worker(self, worker):
        self.worker_pool[worker.worker_id] = worker

    def select_worker(self):
        # Select the worker with the fewest active containers
        return min(self.worker_pool.values(), key=lambda w: len([c for c in w.containers if c.status != 'released']))

class LCSScheduler(Scheduler):
    def __init__(self, warm_time):
        super().__init__()
        self.warm_time = warm_time
        self.cold_start_count = 0
        self.warm_start_count = 0

    def handle_request(self, function_id):
        # Use dynamic worker selection instead of a fixed worker
        worker = self.select_worker()
        selected_container = None
        timestamp = time.time()
        
        # Find the least recently used container in the chosen worker
        idle_containers = [c for c in worker.containers if c.status == 'idle']
        if idle_containers:
            selected_container = min(idle_containers, key=lambda c: c.last_used_time)
            selected_container.status = 'executing'
            selected_container.update_usage()
            self.warm_start_count += 1
            print(f"[{timestamp}] Warm start for function {function_id} on worker {worker.worker_id}")
        else:
            # No idle container, initiate a cold start
            new_container = Container()
            new_container.status = 'executing'
            worker.add_container(new_container)
            self.cold_start_count += 1
            selected_container = new_container
            print(f"[{timestamp}] Cold start for function {function_id} on worker {worker.worker_id}")

        # Simulate processing the function request and set container back to idle
        time.sleep(1)
        selected_container.status = 'idle'
        selected_container.update_usage()
        
        # Release containers that exceed warm time
        self.update_container_status(worker)

    def update_container_status(self, worker):
        current_time = time.time()
        for container in worker.containers:
            if container.status == "idle" and (current_time - container.last_used_time > self.warm_time):
                container.status = "released"
