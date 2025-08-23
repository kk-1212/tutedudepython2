#Task 1

def fact(b):
    if (b < 2):
        return 1
    else:
        return b * fact(b-1)

a = int(input("Enter ther number: "))
print ("Facrtorial of ",a,"is:", fact(a))
