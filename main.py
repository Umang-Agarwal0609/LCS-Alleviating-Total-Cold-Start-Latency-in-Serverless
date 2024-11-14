import time
import random
from scheduler import LCSScheduler
from container import Worker
import matplotlib.pyplot as plt

# Parameters for testing
warm_time = 60
scheduler = LCSScheduler(warm_time)

# Create multiple workers dynamically
num_workers = 5  # Change this number to test with different numbers of workers
for i in range(1, num_workers + 1):
    scheduler.add_worker(Worker(worker_id=i))

# Lists to store data for plotting
cold_starts = []
warm_starts = []
delays = []
timestamps = []

# Simulate requests with random delays and multiple function IDs
function_ids = [101, 102, 103, 104]  # Example function IDs
for i in range(10):
    # Log timestamp before request
    timestamps.append(time.time())
    
    # Handle requests for each function ID
    for function_id in function_ids:
        scheduler.handle_request(function_id)
    
    cold_starts.append(scheduler.cold_start_count)
    warm_starts.append(scheduler.warm_start_count)
    
    # Generate a random delay, log it, and then wait
    delay = random.uniform(10, 60)
    delays.append(delay)
    print(f"Sleeping for {delay:.2f} seconds before next request")
    time.sleep(delay)

# Final data collection for total cold/warm starts
total_requests = scheduler.cold_start_count + scheduler.warm_start_count
cold_start_rate = (scheduler.cold_start_count / total_requests) * 100 if total_requests > 0 else 0
print(f"Total cold starts: {scheduler.cold_start_count}")
print(f"Total warm starts: {scheduler.warm_start_count}")
print(f"Cold start rate: {cold_start_rate:.2f}%")

# Plotting the data
plt.figure(figsize=(12, 6))

# Plot cold starts and warm starts over time
plt.subplot(1, 2, 1)
plt.plot(timestamps, cold_starts, label="Cold Starts", color="red", marker="o")
plt.plot(timestamps, warm_starts, label="Warm Starts", color="green", marker="o")
plt.xlabel("Time")
plt.ylabel("Number of Starts")
plt.title("Cold vs Warm Starts Over Time")
plt.legend()

# Plot delay between requests
plt.subplot(1, 2, 2)
plt.plot(range(len(delays)), delays, color="blue", marker="o")
plt.xlabel("Request Number")
plt.ylabel("Delay (seconds)")
plt.title("Delay Between Requests")

plt.tight_layout()
plt.show()
