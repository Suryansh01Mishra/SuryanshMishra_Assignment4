# Write
with open("output.txt", 'wt') as fh:
    wr = fh.write(input("Enter text to write in a file :\n ") + "\n")
    if wr > 0:
        print("Data successfully written to file")
    else:
        raise ValueError("Data not written to file")

# Append
with open("output.txt", 'at') as fh:
    ap = fh.write(input("Enter text to append in a file :\n ") + "\n")
    if ap > 0:
        print("Data successfully appended to file")
    else:
        raise ValueError("Data not appended to file")

# Read
with open("output.txt", 'rt') as fh:
    lines = fh.readlines()
    print("The final content of the file is:")
    for line in lines:
        print(line.rstrip("\n"))