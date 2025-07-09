# Shift References in DOCX (IEEE Style)

This script helps update reference numbers when merging multiple parts of a report written in IEEE format.

## Why This Is Useful

In IEEE-style reports, each section often starts its references from `[1]`.  
When merging sections into a single report, this causes duplicated reference numbers.  
Manually fixing them is time-consuming and error-prone.

This script solves the problem by:

- Taking the number of references in the previous sections as input
- Adding that number to all references in the current section
- Converting Persian digits to English (if needed)
- Saving the corrected file as `file_path.docx`

## Example

If your section has:

```
This method is widely used [1, 2, 3].
```

And the previous sections had 5 references, the output becomes:

```
This method is widely used [6, 7, 8].
```

## How to Use

1. Install the required package:
   ```bash
   pip install python-docx
   ```
2. Set the path of your `.docx` file in the code (`file_path`)
3. Run the script and enter the shift value (total references so far)
4. The updated document will be saved as `file_path.docx`

## Notes

- Only works with `.docx` files
- Only updates references in brackets like `[1, 2, 3]`
- Doesn't change references inside tables, footnotes, or endnotes
