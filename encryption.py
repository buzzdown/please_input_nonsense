import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

#SHA256 file hashing
def sha256_file(path: str, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()

#AES File encrypting
def encrypt_file(in_path, out_path, password: str) -> None:
    data = open(in_path, "rb").read()

    import hashlib
    key = hashlib.sha256(password.encode("utf-8")).digest()

    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # recommended nonce size for GCM

    ct = aesgcm.encrypt(nonce, data, associated_data=None)

    # store nonce + ciphertext
    open(out_path, "wb").write(nonce + ct)

#AES File decryption
def decrypt_file(in_path, out_path, password: str) -> None:
    blob = open(in_path, "rb").read()
    nonce, ct = blob[:12], blob[12:]

    import hashlib
    key = hashlib.sha256(password.encode("utf-8")).digest()

    aesgcm = AESGCM(key)
    pt = aesgcm.decrypt(nonce, ct, associated_data=None)

    open(out_path, "wb").write(pt)

# Example usage:
# encrypt_file("input.bin", "secret.bin", "password")
# decrypt_file("secret.bin", "recovered.bin", "password")
