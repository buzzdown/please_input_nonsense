import time
from encryption import encrypt_file, decrypt_file
import csv

def passwords():
    pass

def secrets():
    pass

def start_app():
    time.sleep(1)
    print("Starting PIN...")
    time.sleep(1)
    is_running = True

    print()
    print("##########")
    print("Welcome to P.I.N.")
    print("##########")
    print()

    while is_running:
        print("1) Passwords")
        print("2) Secrets")
        print("3) Exit")
        print()
        choice = input("Enter a number (1-3): ")
        print()

        if choice == '1':
            passwords()
            print()
        elif choice == '2':
            secrets()
            print()
        elif choice == '3':
            print("Goodbye, Have a nice day :)")
            is_running = False
        else:
            print("Major err.")
