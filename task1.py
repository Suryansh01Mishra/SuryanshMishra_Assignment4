"""""
with open("Sample.txt",'wt') as fh:
    fh.write("This is sample text file.\n")
    fh.write("It has multiple lines.")
"""
#code
try:
    with open("sample.txt", "r") as fh:
        print("Reading file content:")
        for i, line in enumerate(fh, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")