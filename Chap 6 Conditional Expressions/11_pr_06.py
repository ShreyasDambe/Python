marks=int(input("Enter Your marks:\n"))

if(marks>90 and marks<100):
    print("Your Grade is Excellent!")
elif(marks>80 and marks<90):
    print("Your Grade is A!")
elif(marks>70 and marks<80):
    print("Your Grade is B!")
elif(marks>60 and marks<70):
    print("Your Grade is C!")
elif(marks>50 and marks<60):
    print("Your Grade is D!")

else:
    print("You Are Fail...")