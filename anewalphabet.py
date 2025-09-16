my_dict = {"a":"@", "b":"8", "c":"(", "d":"|)",
"e":"3","f":"#", "g":"6", "h":"[-]", "i":"|",
"j":"_|", "k":"|<", "l":"1", "m":"[]\/[]",
"n":"[]\[]", "o":"0", "p":"|D", "q":"(,)",
"r":"|Z", "s":"$", "t":"']['", "u":"|_|",
"v":"\/", "w":"\/\/", "x":"}{", "y":"`/",
"z":"2"}

string = input("What's the c0de?")

string2 = ""

for char in string.lower():
    if char in my_dict:
        string2 += my_dict.get(char)
    else:
        string2 += char

print(string2)

