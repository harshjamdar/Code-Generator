
# Code Generator

This Python script generates unique codes with a fixed prefix and saves them to multiple text files.
## Features

- Customizable code length: You can specify the number of digits in the generated codes.
- Optional fixed prefix: You can choose to include a fixed prefix (4-8 letters) at the beginning of each code.
- Unique code generation: The program ensures that all generated codes are unique.
- File splitting: If the number of codes exceeds a maximum per file, the codes are split into multiple files.
- Zipping: All generated files are zipped into a single "codes.zip" archive for easy distribution.
- (Optional) File deletion: You have the option to delete the individual text files after zipping.


- Cross platform


## Usage
- Clone or download the repository.
- Run the script: ```python code_generator.py```
- Enter the fixed prefix: Provide a prefix between 4 and 8 characters.
- Enter the number of codes to generate: Specify the desired number of unique codes.

## Uses 
- Promotional codes: Generate unique coupon codes for marketing campaigns or discounts.
- Gift card codes: Create unique codes for gift cards or vouchers.
- Serial numbers: Generate serial numbers for products or software licenses.
- Access codes: Create temporary access codes for events or online resources.
- User IDs: Generate unique user IDs for online platforms or applications.
- Password generation (with modifications): While this code isn't specifically designed for password generation, it could be adapted to create random passwords with certain complexity requirements.

## Examples
```
Enter the fixed prefix (4-8 letters): ABCD
Enter the number of codes to generate: 1000
Codes generated and saved to 4 files (code_1.txt, code_2.txt, code_3.txt, code_4.txt)

```

## Customization
- You can adjust the max_codes_per_file variable to change the maximum number of codes stored in each file.
- The code generation logic can be modified within the generate_code() function to suit specific requirements.

## Dependencies
- Python 3.x
- random and string modules (included in the standard library)

## License

[MIT](https://choosealicense.com/licenses/mit/)

