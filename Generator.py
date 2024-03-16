import random
import string
import zipfile

def generate_code(fixed_prefix="", length=16, generated_codes=None):
    if generated_codes is None:
        generated_codes = set()  # Initialize an empty set to store generated codes

    while True:
        if fixed_prefix and not 4 <= len(fixed_prefix) <= 8:
            raise ValueError("Fixed prefix length must be between 4 and 8 characters.")

        characters = string.ascii_uppercase + string.digits
        random_part = ''.join(random.choice(characters) for _ in range(length))
        code = fixed_prefix + random_part

        if code not in generated_codes:
            generated_codes.add(code)  # Add the unique code to the set
            return code

# Get user input
num_digits = int(input("Enter the number of digits for the code: "))
use_fixed_prefix = input("Do you want to use a fixed prefix (yes/no)? ").lower()

if use_fixed_prefix == "yes":
    fixed_prefix = input("Enter the fixed prefix (4-8 letters): ").upper()
else:
    fixed_prefix = ""  # No fixed prefix

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
                code = generate_code(fixed_prefix, num_digits, generated_codes=generated_codes)
                file.write(code + "\n")
                num_codes -= 1

# Zip the generated files
with zipfile.ZipFile("codes.zip", "w") as zip_file:
    for file_index in range(1, file_count + 1):
        filename = f"code_{file_index}.txt"
        zip_file.write(filename)

# Delete the individual text files (optional)
# for file_index in range(1, file_count + 1):
#     filename = f"code_{file_index}.txt"
#     os.remove(filename)

print(f"Codes generated and zipped into codes.zip")