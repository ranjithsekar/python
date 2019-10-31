userAge = int(input("Enter your age: "))
eligibile = userAge >= 17 and userAge <= 19
print(f"You are eligibility to join college is: {eligibile}")

working = userAge < 15 or userAge > 65
print(f"At {userAge} you will be working?: {working}")
