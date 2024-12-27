import hashlib

data = input("Input data for hash: ")
print("SHA256: ", hashlib.sha256(data.encode()).hexdigest())