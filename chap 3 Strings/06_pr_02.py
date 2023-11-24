letter='''Dear <|NAME|>
Greetings from XYZ Coding House.we are happy to tell you about your Selection
you are selected...!!!
Have a Great Day Ahead!
Thanks and Regards,
XYZ Teams.

<|DATE|>
'''

name=input("Enter Your Name:")
date=input("Enter Date:")

letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)

print(letter)