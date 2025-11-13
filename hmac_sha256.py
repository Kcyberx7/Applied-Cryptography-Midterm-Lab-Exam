import hmac
import hashlib

# Key for HMAC
key = b'secretkey123'

# Read the data
with open("data.txt", "rb") as f:
    data = f.read()

# Create HMAC using SHA-256
hmac_result = hmac.new(key, data, hashlib.sha256).hexdigest()

print("HMAC-SHA256:", hmac_result)
