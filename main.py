import os
import hashlib
from startup import *
from encryption import *
from app import *

word_list = "wordlist.csv"
word_list_hash = sha256_file(word_list)
password_database = "passwords.csv"

def main():
    startup_detecting_all_files()
    start_app()

if __name__ == "__main__":
    main()
