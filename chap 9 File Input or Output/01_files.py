# use open function to read the content of a file!

# f = open('sample.txt','r')
f = open('sample.txt')  #by default read fuction call honar
data = f.read()
print(data)
f.close()