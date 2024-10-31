import hashlib

def crack_password(hash_value, wordlist):
    with open(wordlist, "r", encoding="cp437") as file:
        for line in file:
            line = line.strip()
            hash_object = hashlib.sha256(line.encode())
            hash_hex = hash_object.hexdigest()
            if hash_hex == hash_value:
                print(f"Password found: {line}")
                return
    print("Password not found")

hash_value = "b8e38c8499121373b25139a9e4316807a2b85359f8e2363b3a005a54334a45dc"
wordlist = "samples/rockyou.txt"
crack_password(hash_value, wordlist)