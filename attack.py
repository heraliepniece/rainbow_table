import json
import sys
from pathlib import Path

# loads rainbow table
def load_rainbow_table(path = "rainbow.json"):
# create a path object to represent file path
    p = Path(path)
    # if p doesnt exist or is not a file, throws and exits with an error
    if not p.is_file():
        print(f"Rainbow table file '{path}' not found.")
        sys.exit(1)
# open file for reading with utf-8 encoding
    with p.open("r", encoding = "utf-8") as f:
        rainbow_table = json.load(f)
# normalize keys and values (remove whitespace)
    normalized = {}
    # creates a loop to go through the key value pairs
    for k, v in rainbow_table.items():
        # if not a string, skip
        if not isinstance(k, str):
            continue
        # strip whitespace and make lowercase
        key = k.strip().lower()

        # check if key is a valid SHA-256 hash
        if len(key) !=64:
            print(f"Invalid hash length for key '{k}'. Expected 64 characters.")
            continue
        normalized[key] = v if isinstance(v, str) else str(v)

    return normalized

# make a module guard to allow script to be run directly
if __name__ == "__main__":
    # loads rainbow table
    rainbow_table = load_rainbow_table()
    print(f"Loaded rainbow table with {len(rainbow_table)} entries.")
    # user input for target hash, normalize input
    target = input("Enter SHA-256 hex:").strip().lower()
    # check if target is a valid hash
    if len(target) != 64:
        print(f"Invalid hash length for target '{target}'. Expected 64 characters.")
        sys.exit(1)
        # look up target in rainbow table
    pw = rainbow_table.get(target)
    if pw is not None:
        print("Found! Plaintext is:", pw)
    else:
        print("No match found in rainbow table. ")
    
