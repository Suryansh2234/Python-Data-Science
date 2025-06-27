num = int(input("Enter a number"))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev *10 + digit
    num = num //10
if original == rev:
    print(f"{original} is a pallinedrome")
else:
    print(f"{original} is not a pallinedrome")
    

