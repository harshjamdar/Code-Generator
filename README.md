
# Code Generator

This Python script generates unique codes with a fixed prefix and saves them to multiple text files.
## Features

- Generates codes with a user-specified fixed prefix (4-8 characters).
- Ensures uniqueness of generated codes.
- Distributes codes across multiple files to avoid exceeding a maximum number of codes per file (300 by default).

- Cross platform


## Usage
- Clone or download the repository.
- Run the script: ```python code_generator.py```
- Enter the fixed prefix: Provide a prefix between 4 and 8 characters.
- Enter the number of codes to generate: Specify the desired number of unique codes.
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

