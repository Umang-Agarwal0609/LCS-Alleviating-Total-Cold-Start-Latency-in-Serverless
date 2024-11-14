# LCS : Alleviating Total Cold Start Latency in Serverless 

LRU-Based Container Scheduler
This project implements a Least Recently Used (LRU) Container Scheduler designed to handle function requests efficiently by minimizing cold starts. The scheduler dynamically manages multiple containers across workers, reusing idle containers within a specified warm time to reduce latency and optimize resource utilization. It is designed to scale across multiple workers and function IDs, distributing load evenly using a dynamic worker selection strategy.

Project Structure
container.py: Defines the Container and Worker classes.

Container tracks creation time, last used time, and status (idle, executing, or released).
Worker manages a list of containers and assigns containers to handle function requests.
scheduler.py: Implements the Scheduler and LCSScheduler classes.

Scheduler provides basic worker management.
LCSScheduler extends Scheduler with LRU-based container management, dynamically selecting workers based on load and reusing idle containers to minimize cold starts.
main.py: Simulates and tests the scheduler’s performance with multiple workers and function IDs.

Initializes the scheduler, adds workers, and simulates requests with random delays.
Collects and prints statistics on cold and warm starts, and visualizes the data in graphs.
Features
Dynamic Worker Selection: Routes each request to the worker with the fewest active containers, distributing load effectively across workers.
Cold and Warm Start Tracking: Tracks cold and warm starts to measure performance, showing the scheduler's effectiveness in reusing containers.
Scalability: Supports any number of workers and functions, adapting to high loads while minimizing resource consumption.
Requirements
Python 3.x
Required Python packages:
matplotlib (for visualizations)
random (for generating random delays between requests)
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/lru-container-scheduler.git
Install dependencies:
bash
Copy code
pip install matplotlib
Usage
Run the Simulation:

bash
Copy code
python main.py
This command will:

Initialize the scheduler with a specified warm time.
Dynamically select workers for each function request.
Collect data on cold and warm starts and simulate delays between requests.
Display final statistics and generate graphs.
View Output:

Total cold starts, Total warm starts, and Cold start rate are displayed in the console.
Graphs show cold vs. warm starts over time and delay patterns, providing insights into scheduler performance.
Code Example
Here’s a basic example of initializing the scheduler with dynamic worker selection:

python
Copy code
from scheduler import LCSScheduler
from container import Worker

# Initialize scheduler with warm time of 60 seconds
scheduler = LCSScheduler(warm_time=60)

# Add multiple workers
for i in range(1, 5):
    scheduler.add_worker(Worker(worker_id=i))

# Simulate handling requests for various function IDs
function_ids = [101, 102, 103, 104]
for function_id in function_ids:
    scheduler.handle_request(function_id)
Project Goals
This project demonstrates:

Minimizing Cold Starts: By dynamically managing containers, the scheduler reduces the need for new container initialization.
Efficient Load Distribution: Using a dynamic selection strategy, the scheduler balances requests across multiple workers.
Scalability and Flexibility: Supports flexible scaling with any number of workers and functions, making it suitable for high-demand environments.
Future Improvements
Potential enhancements include:

Adaptive Warm Time: Dynamically adjust warm time based on request patterns.
Advanced Load Balancing: Implement additional strategies (e.g., round-robin or priority-based) for routing requests.
License
This project is open source and available under the MIT License.

## Installation

To install this project, follow these steps:
1. Clone the repository: https://github.com/Umang-Agarwal0609/LCS-Alleviating-Total-Cold-Start-Latency-in-Serverless

## Usage

To run the project, use the following command:
```bash
python3 main.py
