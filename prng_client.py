import zmq
import json

def main():
    # Create a ZeroMQ context and a REQ (request) socket.
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")  # Connect to the microservice

    # Test 1: Single Integer PRNG
    request_single = {"type": "single", "N": 10}
    socket.send_json(request_single)
    response = socket.recv_json()
    print("Response for single request:", response)

    # Test 2: Excluded Integer PRNG
    request_excluded = {"type": "excluded", "N": 10, "X": 5}
    socket.send_json(request_excluded)
    response = socket.recv_json()
    print("Response for excluded request:", response)

    # Test 3: Multiple Random Numbers PRNG
    request_multiple = {"type": "multiple", "N": 10, "M": 3}
    socket.send_json(request_multiple)
    response = socket.recv_json()
    print("Response for multiple request:", response)

if __name__ == "__main__":
    main()
