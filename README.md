# Password Security Checker

This Python script checks the security of a password using the Pwned Passwords API without sending the actual password. It hashes the password using SHA-1 encryption and checks whether it has been compromised in known data breaches.

## Setup

1. Make sure you have Python installed on your system.
2. Install the required Python modules by running: `pip install requests`.

## Usage

1. Clone or download this repository.
2. Run the `password_checker.py` script.
3. Enter the password you want to check when prompted.

The script will generate a SHA-1 hash of the password and query the Pwned Passwords API to determine if it has been compromised. It will inform you if the password has been found in data breaches and suggest choosing a stronger password if necessary.

## How It Works

- `password_checker.py` contains the main functionality of the program.
- It uses the `hashlib` module to generate a SHA-1 hash of the password.
- The script queries the Pwned Passwords API using the first 5 characters of the hash to check for occurrences in known breaches.
- Results are displayed to the user indicating whether the password has been compromised or not.

## Author

Raghav Minhas

## Date

20-11-2023

## Note
- This project demonstrates a basic implementation of password security checking.
- This project is intended for educational purposes and can be customized based on specific requirements. Feel free to modify and enhance the script as needed.



