import requests
import hashlib

# Function to check the password against Pwned Passwords API
def password_checker(sha1_pass):
    # Creating the API URL with the first 5 characters of the hashed password
    url = f"https://api.pwnedpasswords.com/range/{sha1_pass[:5]}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to generate SHA-1 hash of the password
def get_sha1(password):
    # Generating SHA-1 hash and converting it to uppercase
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    return sha1_password

# Function to check if the password has been pwned
def is_pwned(hashes, tail):
    hashes = (line.split(':') for line in hashes.splitlines())
    for h, count in hashes:
        if h == tail:
            return int(count)
    return 0

# Main function to take user input and check password against Pwned Passwords
def main():
    password = input('Please enter the password you want to check: ')
    sha1_pass = get_sha1(password)
    pwned_hashes = password_checker(sha1_pass)

    if pwned_hashes:
        tail = sha1_pass[5:]  # Corrected variable name from sha1_password to sha1_pass
        count = is_pwned(pwned_hashes, tail)
        if count:
            print(f"{password} has been found {count} times in data breaches. Please choose a stronger password.")
        else:
            print(f"{password} has not been found in any known data breaches. It might be secure.")
    else:
        print("Unable to check the password")

if __name__ == '__main__':
    main()