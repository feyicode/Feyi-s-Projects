marks = int(input("Enter a number between 0 and 100"))

print("Your grade is:")
if marks < 50:
    print("U")
elif marks > 50 and marks < 69:
    print("Pass")
elif marks > 70 and marks < 89:
    print("Merit")
elif marks > 90 and marks <100:
    print("Distinction")
else:
    print("Invalid")