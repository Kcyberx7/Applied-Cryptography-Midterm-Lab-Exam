import hashlib

with open("data.txt", "rb") as f:
    data = f.read()

sha256_hash = hashlib.sha256(data).hexdigest()
print("SHA-256 Hash:", sha256_hash)
