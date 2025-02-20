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
