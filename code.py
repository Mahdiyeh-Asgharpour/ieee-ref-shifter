from docx import Document  # Importing the python-docx library to work with Word documents
import re  # Importing the regular expressions module for pattern matching

# Function to convert Persian digits to English digits
def convert_to_english_numbers(text):
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    trans_table = str.maketrans(persian_digits, english_digits)
    return text.translate(trans_table)

# Function to shift reference numbers in a single run of text
def shift_references_in_run(run, shift_value, pattern):
    # Replacement function to apply the shift to matched reference numbers
    def replace(match):
        numbers_raw = convert_to_english_numbers(match.group(1))  # Convert Persian digits if present
        numbers = [int(n.strip()) for n in numbers_raw.split(',')]  # Extract the individual numbers
        shifted = [str(n + shift_value) for n in numbers]  # Apply the shift
        return f"[{','.join(shifted)}]"  # Return the shifted reference as a string

    new_text = pattern.sub(replace, run.text)  # Replace matching patterns in the run's text
    if new_text != run.text:
        run.text = new_text  # Only update the run if any change was made

# Function to process the entire Word document and shift all reference numbers
def shift_references_in_docx(file_path, shift_value):
    doc = Document(file_path)  # Load the Word document
    pattern = re.compile(r'\[([\d\u06F0-\u06F9,\s]+)\]?\.?')  # Regex to match references like [13, 14]

    # Loop through each paragraph and its runs
    for para in doc.paragraphs:
        for run in para.runs:
            shift_references_in_run(run, shift_value, pattern)  # Apply shifting to each run

    doc.save("3.docx")  # Save the modified document
    print("Done")  # Confirmation message

# Uncomment this line if 'input' was overwritten earlier in your session
# del input

# Get shift value from user input and run the main function
inp = int(input("Enter shift value: "))
shift_references_in_docx("/content/گزارش نهایی 3.docx", inp)
