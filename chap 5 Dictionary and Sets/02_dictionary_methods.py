myDict = {
    "Fast":"In a Quick Manner",
    "Shreyas":"A Coder",
    "Marks":[1,2,3],
    "anotherdict":{'harry':'a Player'},
     1:2      
}

print(list(myDict.keys()))  #prints the keys of the dictionary
print(myDict.values())     #prints the keys of the dictionary
print(myDict.items())      # prints the keys and values of dictionary
print(myDict)
updateDict={
    "Lovish":"Friend",
    "Sumit":"Frient",
    "Shreyas":"A Dancer"
}

myDict.update(updateDict) #Updates the dictionary by adding the key value pairs from updateDict
print(myDict)

print(myDict.get("Shreyas")) #prints value associated with key"Shreyas"
print(myDict["Shreyas"]) #prints value associated with key"Shreyas"


# The difference between .get and [] Syntax in Distinction
print(myDict.get("Shreyas2")) #Returns None as Shreyas2 is not present in the Dictionary
print(myDict["Shreyas2"])    #throws an error as Shreyas2 is not present in the Dictionary