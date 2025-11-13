import secrets

# Diffie-Hellman parameters (small example for simplicity)
p = 23  # prime modulus
g = 5   # primitive root

# Alice chooses a private key
a_private = secrets.randbelow(p)
# Alice computes public key
A_public = pow(g, a_private, p)

# Bob chooses a private key
b_private = secrets.randbelow(p)
# Bob computes public key
B_public = pow(g, b_private, p)

# Alice computes shared secret using Bob's public key
alice_shared = pow(B_public, a_private, p)
# Bob computes shared secret using Alice's public key
bob_shared = pow(A_public, b_private, p)

# Display results
print("Alice's public key:", A_public)
print("Bob's public key:", B_public)
print("Shared secret computed by Alice:", alice_shared)
print("Shared secret computed by Bob:  ", bob_shared)
print("Shared secrets match:", alice_shared == bob_shared)
