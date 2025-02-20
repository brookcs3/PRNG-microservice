import zmq
import random
import json

def main():
    # Create a ZeroMQ context and a REP (reply) socket.
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")  # Bind to port 5555 for incoming requests

    print("PRNG Microservice is running and listening on port 5555...")
    
    while True:
        # Wait for the next request from a client
        request = socket.recv_json()
        print("Received request:", request)

        # Determine the type of request and process accordingly
        response = {}
        req_type = request.get("type")
        
        if req_type == "single":
            N = request.get("N")
            # Return a random integer between 1 and N (inclusive)
            response["random_number"] = random.randint(1, N)
        
        elif req_type == "excluded":
            N = request.get("N")
            X = request.get("X")
            # Ensure the excluded number is not returned
            num = random.randint(1, N)
            while num == X:
                num = random.randint(1, N)
            response["random_number"] = num

        elif req_type == "multiple":
            N = request.get("N")
            M = request.get("M")
            # Generate a list of M random integers between 1 and N (inclusive)
            response["random_numbers"] = [random.randint(1, N) for _ in range(M)]
        
        else:
            response["error"] = "Invalid request type"

        # Send the response back to the client
        socket.send_json(response)

if __name__ == "__main__":
    main()
