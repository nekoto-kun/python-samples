# Python Examples in Cybersecurity

This repository contains Python examples in cybersecurity referenced from various sources. Python version used in this repository is 3.13.0. Make sure to install the required packages before running the examples.

## Disclaimer

The examples in this repository are for educational purposes only. The author is not responsible for any misuse of the information provided in the examples. The author does not promote any illegal activities.

## How to test

1. Clone the repository
2. Create a virtual environment using `python -m venv venv`
3. Activate the virtual environment using `source venv/bin/activate` (Linux) or `venv\Scripts\activate` (Windows)
4. Install the required packages using `pip install -r requirements.txt`

## About `samples` directory

The `samples` directory is used for storing resources that are used in the examples. The resources are referenced in the examples using relative paths. Due to big file sizes, some resources are not included in the repository. Here is the list of resources that are not included in the repository:

1. `samples/rockyou.txt`: A text file containing a list of common passwords.
2. `samples/user.sqlite`: An SQLite database file containing a table named `users` with columns `id`, `username`, and `password`.