# LCS : Alleviating Total Cold Start Latency in Serverless 
Applications with LRU Warm Container Approach 

Serverless computing has emerged as a popular paradigm, 
enabling developers to deploy applications without the complexities of server management. 
However, one of its critical drawbacks is cold start latency—delays that occur when a function is triggered, 
but no prewarmed environment is available to execute it. These cold starts can significantly impact the performance 
and responsiveness of applications, particularly in latency-sensitive or highfrequency invocation scenarios. 
In this report, we present an innovative solution, the Least Recently Used (LRU) Warm Container Selection (LCS) 
strategy, which maintains a pool of prewarmed containers to minimize cold starts. By intelligently managing this 
pool using an LRU strategy, combined with affinity-aware scheduling, our approach dynamically adjusts container 
allocation based on demand patterns. This reduces cold start occurrences, optimizes resource utilization, and 
enhances user experience. Our findings demonstrate that LCS effectively mitigates cold start latency, striking 
a balance between performance and resource efficiency in serverless applications. 

## Installation

To install this project, follow these steps:
1. Clone the repository: https://github.com/Umang-Agarwal0609/LCS-Alleviating-Total-Cold-Start-Latency-in-Serverless
## Usage

To run the project, use the following command:
```bash
python3 main.py
