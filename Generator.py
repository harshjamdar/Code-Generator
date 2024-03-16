import random
import string

def generate_code(fixed_prefix, length=16, generated_codes=None):
    if generated_codes is None:
        generated_codes = set()  # Initialize an empty set to store generated codes

    while True:
        if not 4 <= len(fixed_prefix) <= 8:
            raise ValueError("Fixed prefix length must be between 4 and 8 characters.")

        characters = string.ascii_uppercase + string.digits
        remaining_length = length - len(fixed_prefix)
        random_part = ''.join(random.choice(characters) for _ in range(remaining_length))
        code = fixed_prefix + random_part

        if code not in generated_codes:
            generated_codes.add(code)  # Add the unique code to the set
            return code

# Get user input
fixed_prefix = input("Enter the fixed prefix (4-8 letters): ").upper()
num_codes = int(input("Enter the number of codes to generate: "))

# Calculate number of files needed
max_codes_per_file = 300
file_count = (num_codes + max_codes_per_file - 1) // max_codes_per_file

# Generate and save codes to files
generated_codes = set()  # Create a set to track generated codes across files
for file_index in range(1, file_count + 1):
    filename = f"code_{file_index}.txt"
    with open(filename, "w") as file:
        for _ in range(max_codes_per_file):
            if num_codes > 0:
                code = generate_code(fixed_prefix, generated_codes=generated_codes)
                file.write(code + "\n")
                num_codes -= 1

print(f"Codes generated and saved to {file_count} files (code_1.txt, code_2.txt, ...)")