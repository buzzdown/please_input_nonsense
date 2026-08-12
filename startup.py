import os
from encryption import *

word_list = "wordlist.csv"
word_list_hash = sha256_file(word_list)
password_database = "passwords.csv"

def startup_detecting_all_files():
    if os.path.exists(word_list):
        print(f"Found {word_list}.")
    else:
        print(f"No {word_list} found.")

    if os.path.isfile(word_list):
        print(f"{word_list} is a file.")
    else:
        print(f"{word_list} has been corrupted.")

    if word_list_hash ==  "8c3bf3e8592213a9155a9713d654736d6e5cdddcfaf5b1d5e8d6efcdd3fb6fc1":
        print(f"{word_list} seems untouched.")
    else:
        print(f"{word_list} has been compromised. Reinstall the wordlist.csv file.")

    if os.path.exists(password_database):
        print(f"Found {password_database}")
    else:
        print("Error. No password database.")
