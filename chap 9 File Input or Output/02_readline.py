f = open('sample.txt') 

# for First line
data = f.readline() # readlin() function print only single line
print(data)

# for second line
data = f.readline()
print(data)
f.close()