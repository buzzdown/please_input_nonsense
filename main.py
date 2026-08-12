import os
import hashlib
from startup import *
from encryption import *

word_list = "wordlist.csv"
word_list_hash = sha256_file(word_list)
password_database = "passwords.csv"

def main():
    startup_detecting_all_files()
    
if __name__ == "__main__":
    main()
