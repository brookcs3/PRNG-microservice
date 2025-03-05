# PRNG Microservice

## Project Overview

This repository contains the PRNG Microservice for CS361. The microservice is implemented in Python and uses ZeroMQ to handle JSON requests. It generates pseudo-random numbers based on user-defined parameters and supports three types of requests:

- **Single Integer PRNG:** Returns a random number between 1 and N.
- **Excluded Integer PRNG:** Returns a random number between 1 and N but excludes a specified number (X).
- **Multiple Random Numbers PRNG:** Returns M random numbers between 1 and N.

## Communication Contract

### How to Request Data

#### Single Integer Request
- **Request:**
  ```json
  {"type": "single", "N": 10}
  ```
  - *N* represents the upper bound (inclusive).

#### Excluded Integer Request
- **Request:**
  ```json
  {"type": "excluded", "N": 10, "X": 5}
  ```
  - *N* is the upper bound.
  - *X* is the number to exclude from the result.

#### Multiple Random Numbers Request
- **Request:**
  ```json
  {"type": "multiple", "N": 10, "M": 3}
  ```
  - *N* is the upper bound.
  - *M* is the number of random numbers requested.

### How to Receive Data

- **Successful Response for Single Integer:**
  ```json
  {"random_number": 7}
  ```
- **Successful Response for Multiple Integers:**
  ```json
  {"random_numbers": [3, 8, 2]}
  ```
- **Error Response (for invalid request types):**
  ```json
  {"error": "Invalid request type"}
  ```

## Example Code for Requesting and Receiving Data

Below is an example Python code snippet that demonstrates how to connect to the microservice, send a request, and receive a response. This example is provided for informational purposes so that you understand how to programmatically interact with the microservice. **Your teammate must write their own code.**

#### Connecting and Requesting a Single Random Number
```python
import zmq
import json

# Create a ZeroMQ context and a REQ (request) socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")  # Connect to the microservice

# Example: Single Integer Request
request_data = {"type": "single", "N": 10}
socket.send_json(request_data)

# Receive the response from the microservice
response = socket.recv_json()
print("Response for single request:", response)
```

#### Connecting and Requesting with an Excluded Integer
```python
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Example: Excluded Integer Request
request_data = {"type": "excluded", "N": 10, "X": 5}
socket.send_json(request_data)

response = socket.recv_json()
print("Response for excluded request:", response)
```

#### Connecting and Requesting Multiple Random Numbers
```python
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Example: Multiple Random Numbers Request
request_data = {"type": "multiple", "N": 10, "M": 3}
socket.send_json(request_data)

response = socket.recv_json()
print("Response for multiple request:", response)
```

## UML Sequence Diagram

The following UML sequence diagram illustrates the interaction between the client and the microservice:

[UML Sequence Diagram](https://github.com/brookcs3/PRNG-microservice/blob/b510db2887b315ca96d3863a4d2b2eb31a43eeab/mermaid-diagram-2025-02-20-092656.png)

**Explanation of the Diagram:**
1. **Client**: This is your `prng_client.py` or any other program sending requests.
2. **Microservice**: This is your `prng_service.py`, which listens on port 5555 for incoming requests.
3. **Send JSON Request**: The client sends a JSON object containing fields such as `"type"`, `"N"`, `"X"`, or `"M"`.
4. **Parse Request & Generate Random Number(s)**: The microservice reads the request, determines which type of random numbers to generate, and processes the request accordingly.
5. **Return JSON Response**: The microservice replies with a JSON object containing the generated number(s) or an error message if the request was invalid.

## Mitigation Plan

- **Teammate:**  
  I implemented Microservice A for **Alec**.

- **Current Status:**  
  The microservice is fully functional and has been tested locally using a dedicated test client.

- **Access Details:**  
  The code is hosted on GitHub at [https://github.com/brookcs3/PRNG-microservice.git](https://github.com/brookcs3/PRNG-microservice.git). Teammates can clone the repository and run the microservice locally using the instructions below.

- **Troubleshooting/Backup Plan:**  
  If you encounter any issues accessing or running the microservice, please contact me at **brooksc3@oregonstate.edu**. I am available before 10PM PST to assist with any problems. If issues persist, we can arrange a troubleshooting session or consider hosting the service on a shared server.

- **Reporting Timeline:**  
  Please report any issues by **February 24** to ensure prompt resolution.

- **Additional Notes:**  
  There are no additional notes; N/A.

## Setup and Running Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/brookcs3/PRNG-microservice.git
   cd PRNG-microservice
   ```

2. **Set Up the Virtual Environment:**
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Microservice:**
   ```bash
   python prng_service.py
   ```
   The service will start and listen on port 5555.

5. **Test the Service:**
   In another terminal (with the virtual environment activated), run:
   ```bash
   python prng_client.py
   ```
   This will send test requests to the microservice and display the responses.
