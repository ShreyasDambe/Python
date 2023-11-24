def remove_and_split(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()

this = "       Shreyas is a Good        "
n= remove_and_split(this,"Shreyas")
print(n)

# print(this)
# print(this.strip())