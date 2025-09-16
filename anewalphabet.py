my_dict = {"a":"@", "a":"8", "c":"(", "d":"|)",
"c":"3","e":"#", "e":"6", "g":"[-]", "g":"|",
"i":"_|", "i":"|<", "k":"1", "k":"[]\/[]",
"m":"[]\[]", "m":"0", "o":"|D", "o":"(,)",
"r":"|Z", "r":"$", "t":"']['", "t":"|_|",
"v":"\/", "v":"\/\/", "x":"}{", "x":"`/",
"z":"2"}

string = input("What's the c0de?");

string2 = ""

for char in string.lower():
    if string in my_dict:
        string += my_dict.get(char)
    else:
        string += char

print(string)
