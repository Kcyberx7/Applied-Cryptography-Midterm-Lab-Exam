from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

# Load private key
with open("ecc_private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Load public key
with open("ecc_public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Read the message
with open("ecc.txt", "rb") as f:
    message = f.read()

# Sign the message
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# Save the signature
with open("ecc_signature.sig", "wb") as f:
    f.write(signature)

print("Message signed successfully!")

# Verify the signature
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("Signature is valid! ✅")
except InvalidSignature:
    print("Signature is invalid! ❌")
