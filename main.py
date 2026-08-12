import os
import hashlib
from startup import *

def sha256_file(path: str, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()

word_list = "wordlist.csv"
word_list_hash = sha256_file(word_list)
password_database = "passwords.csv"

def main():
    startup_detecting_all_files()


if __name__ == "__main__":
    main()
