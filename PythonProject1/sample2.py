#Task 2

a = input("Enter text to write to the file: ")

f1 = open("output.txt","w")
f1.write(a)
print ("Data successfully written 'output.txt'")
f1.close()

b = input("Enter additional text to append: ")
f1= open("output.txt","a")
f1.write("\n"+b)
print ("Data successfully appended")
f1.close()

print ("Final contents of 'output.txt':")
f1 = open("output.txt","r")
print(f1.read())
f1.close()