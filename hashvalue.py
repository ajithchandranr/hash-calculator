import hashlib
import sys

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()

    try:
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                sha256_hash.update(chunk)
    except FileNotFoundError:
        return None
    except IOError:
        return None

    hash_value = sha256_hash.hexdigest()

    return hash_value

# Check if file path is provided as command-line argument
if len(sys.argv) < 2:
    print("Usage: python hash_calculator.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
hash_value = calculate_hash(file_path)

if hash_value is not None:
    print(f"SHA-256 Hash: {hash_value}")
else:
    print("Error calculating hash. File not found or cannot be read.")
