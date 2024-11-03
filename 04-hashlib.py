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

hash_value = "4b7ef7e5b888084daa83b8da109754671006793e01fb55bce607528affcde3e7"
wordlist = "samples/rockyou.txt"
crack_password(hash_value, wordlist)