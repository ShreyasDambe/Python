num = int(input("Enter the number: "))
prime = True

for i in range (2,num):
    if(num%i ==0):
        prime = False
        break
if prime:
    print("This Number is Prime")
else:
    print("This number is not prime")
