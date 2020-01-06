def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

digits = input("enter a number ")
if isDigit(digits)
    print("true")
else:
    print("false")
