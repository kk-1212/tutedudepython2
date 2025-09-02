#Task 1:
try:
    print("Reading the file content")
    f = open("sample.txt")
    f1 = f.readlines()
    print("Line 1:- ", f1[0], end='')
    print("Line 2:- ", f1[1])
except FileNotFoundError:
    print("File "'sample.txt'" not found")