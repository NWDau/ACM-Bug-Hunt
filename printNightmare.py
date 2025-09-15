# No, not *that* PrintNightmare. 
## This is just me being evil with strings. 
string = input("Input a string: ")
strList = list(string)

## print in upper
for i in range(len(strList)):
    print(strList[i].upper(), end="_")

print("\n")

## print backwards
for i in range(len(strList)-1, -1, -1):
    print(strList[i], end="")
  
print("\n")

## print in that spongebob sarcasm meme case??? i guess??? look, i'm very tired.
for i in range(len(strList)):
    if(i%2 = 0): print(strList[i].upper(), end="")
    else: print (strList[i].lower(), end="")

print("\n")

## remove integers
for i in range(len(strList)):
    if(strList[i].isnumeric()):
        print("INTEGER DETECTED AT INDEX: ", i, "\nREMOVING INTEGER.")
        strList[i] = ""
for i in range(len(strList)):
    print(strList[i], end="")
