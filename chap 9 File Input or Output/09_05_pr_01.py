f = open('poesms.txt','r')
data = f.read()
if 'twinkle' in data:
    print("Twinkle is present")
else:
    print("Twinkle is not present")

# print(data)
f.close()