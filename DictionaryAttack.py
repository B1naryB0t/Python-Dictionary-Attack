import hashlib
import asyncio
import time

### Function to load the dictionary file from file path. Opens in read mode and splits lines.
def load_passwords(file_path):
    with open(file_path, "r", encoding="latin1") as file:
        passwords = file.read().splitlines()
    return passwords

### Function to hash a password using SHA-256.
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

### Coroutine to check potential hash against target hash
async def check_password(password, target_hash):
    hashed_password = hash_password(password)
    if hashed_password == target_hash:
        return password
    return None

### Main function to perform the dictionary attack with respect to asyncio
async def dictionary_attack(passwords, target_hash):
    tasks = []
    for password in passwords:
        tasks.append(check_password(password, target_hash))
    for task in asyncio.as_completed(tasks):
        result = await task
        if result:
            return result
    return None

### Function to measure time and operate the dictionary attack
def run_attack(file_path, target_hash):
    start_time = time.time()
    passwords = load_passwords(file_path)
    found_password = asyncio.run(dictionary_attack(passwords, target_hash))
    end_time = time.time()
    time_taken = end_time - start_time

    if found_password:
        print(f"Password found: {found_password}")
    else:
        print("Password not found.")

    print(f"Time taken: {time_taken} seconds")

### Correct password accepts user input and generates a target hash. In a real cracking scenario,
### target_hash would be known and populated from the stolen credential document.
correct_password = str(input("Enter the correct password: "))
target_hash = hash_password(correct_password)

### File path directs to dictionary of common passwords. Run attack initiates the cracker.
file_path = "1pt6Mil.txt"
run_attack(file_path, target_hash)