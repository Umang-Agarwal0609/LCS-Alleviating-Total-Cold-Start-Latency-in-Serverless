# LRU-Based Container Scheduler

This project implements a **Least Recently Used (LRU) Container Scheduler** designed to handle function requests efficiently by minimizing cold starts. The scheduler dynamically manages multiple containers across workers, reusing idle containers within a specified warm time to reduce latency and optimize resource utilization. It is designed to scale across multiple workers and function IDs, distributing load evenly using a dynamic worker selection strategy.

## Project Structure

- **container.py**: Defines the `Container` and `Worker` classes.
  - `Container` tracks creation time, last used time, and status (idle, executing, or released).
  - `Worker` manages a list of containers and assigns containers to handle function requests.
  
- **scheduler.py**: Implements the `Scheduler` and `LCSScheduler` classes.
  - `Scheduler` provides basic worker management.
  - `LCSScheduler` extends `Scheduler` with LRU-based container management, dynamically selecting workers based on load and reusing idle containers to minimize cold starts.

- **main.py**: Simulates and tests the scheduler’s performance with multiple workers and function IDs.
  - Initializes the scheduler, adds workers, and simulates requests with random delays.
  - Collects and prints statistics on cold and warm starts, and visualizes the data in graphs.

## Features

- **Dynamic Worker Selection**: Routes each request to the worker with the fewest active containers, distributing load effectively across workers.
- **Cold and Warm Start Tracking**: Tracks cold and warm starts to measure performance, showing the scheduler's effectiveness in reusing containers.
- **Scalability**: Supports any number of workers and functions, adapting to high loads while minimizing resource consumption.

## Requirements

- Python 3.x
- Required Python packages:
  - `matplotlib` (for visualizations)
  - `random` (for generating random delays between requests)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Umang-Agarwal0609/LCS-Alleviating-Total-Cold-Start-Latency-in-Serverless
2. Install dependencies:
   ```bash
   pip install matplotlib

## Usage
```bash
python main.py


## Project Goals

This project demonstrates:

- **Minimizing Cold Starts**: By dynamically managing containers, the scheduler reduces the need for new container initialization.
- **Efficient Load Distribution**: Using a dynamic selection strategy, the scheduler balances requests across multiple workers.
- **Scalability and Flexibility**: Supports flexible scaling with any number of workers and functions, making it suitable for high-demand environments.

## Future Improvements

Potential enhancements include:

- **Adaptive Warm Time**: Dynamically adjust warm time based on request patterns.
- **Advanced Load Balancing**: Implement additional strategies (e.g., round-robin or priority-based) for routing requests.

