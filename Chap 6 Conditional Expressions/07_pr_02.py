sub1=int(input("Enter First subject marks:\n"))
sub2=int(input("Enter Second subject marks:\n"))
sub3=int(input("Enter Third subject marks:\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are Fail because you have less than 33% in one of the Subjects")

elif(sub1+sub2+sub3)/3<40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congratulations! You are passed!")
    