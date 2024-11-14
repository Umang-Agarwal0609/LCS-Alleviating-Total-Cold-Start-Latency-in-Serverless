import time
from scheduler import LCSScheduler
from container import Worker

# Set warm time (in seconds) and initialize scheduler
warm_time = 60
scheduler = LCSScheduler(warm_time)

# Create workers and add them to the scheduler
worker1 = Worker(worker_id=1)
worker2 = Worker(worker_id=2)
scheduler.add_worker(worker1)
scheduler.add_worker(worker2)

# Map function IDs to workers
function_id_1 = 1
function_id_2 = 2
scheduler.worker_pool[function_id_1] = worker1
scheduler.worker_pool[function_id_2] = worker2

# Simulate function requests with delays