
def addingorly(str):
    if(str[-3:]=="ing"):
        str= str + "ly"
    else:
        str = str + "ing"
    return str
word= input("Enter a word to modify :")
modifiedstring=addingorly(word)
print("Modified string=",modifiedstring)
Footer
Output

Enter a string you want to modify: playing

Modified string:playeingely
