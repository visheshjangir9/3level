# import hashlib

# def hash_input(input_data):
#     """Hashes input using SHA-256."""
#     return hashlib.sha256(input_data.encode()).hexdigest()
import hashlib

def hash_input(input_str):
    return hashlib.sha256(input_str.encode('utf-8')).hexdigest()
