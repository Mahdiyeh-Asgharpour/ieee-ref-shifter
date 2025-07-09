# install python-docx library 
!pip install python-docx

from docx import Document
import re

# This function changes Persian numbers to English numbers
def convert_to_english_numbers(text):
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    trans_table = str.maketrans(persian_digits, english_digits)
    return text.translate(trans_table)

# This function opens the docx file and shifts the reference numbers
def shift_references_in_docx(file_path, shift_value):
    doc = Document(file_path)
    
    # This pattern finds numbers like [1, 2, 3] or [۱،۲،۳]
    pattern = re.compile(r'\[([\d\u06F0-\u06F9,\s]+)\]?\.?') 
    
    for para in doc.paragraphs:
        original_text = para.text

        # This part replaces the old numbers with new shifted ones
        def replace(match):
            numbers_raw = convert_to_english_numbers(match.group(1))  # convert to English digits
            numbers = [int(n.strip()) for n in numbers_raw.split(',')]  # make a list of numbers
            shifted = [str(n + shift_value) for n in numbers]  # add the shift value
            return f"[{','.join(shifted)}]"  # make the new string with shifted numbers

        new_text = pattern.sub(replace, original_text)

        if new_text != original_text:
            # Only change if something is updated
            first_run = para.runs[0]
            first_run.text = new_text  # put new text in the first run
            for run in para.runs[1:]:
                run.text = ''  # clear other runs

    doc.save("#")  # save the file with new name
    print("مراجع دقیق و درست جایگزین شدند.")  # print success message

# Set the path of the file and ask for shift value from user
file_path = "#"
shift_value = int(input("Shift value: "))
shift_references_in_docx(file_path, shift_value)
