## SuryanshMishra_Assignment4
==================================

# Files, Exceptions, and Errors in Python.

I learn file handlind and exception handling in tutedude python course module 10.

# Task 1
===========
"""""
with open("Sample.txt",'wt') as fh:
    fh.write("This is sample text file.\n")
    fh.write("It has multiple lines.")
"""
#code
try:
    with open("sample.txt", "rt") as fh:
        print("Reading file content:")
        for i, line in enumerate(fh, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

# Task 2
===========

* Write
with open("output.txt", 'wt') as fh:
    wr = fh.write(input("Enter text to write in a file :\n ") + "\n")
    if wr > 0:
        print("Data successfully written to file")
    else:
        raise ValueError("Data not written to file")

* Append
with open("output.txt", 'at') as fh:
    ap = fh.write(input("Enter text to append in a file :\n ") + "\n")
    if ap > 0:
        print("Data successfully appended to file")
    else:
        raise ValueError("Data not appended to file")

* Read
with open("output.txt", 'rt') as fh:
    lines = fh.readlines()
    print("The final content of the file is:")
    for line in lines:
        print(line.rstrip("\n"))

