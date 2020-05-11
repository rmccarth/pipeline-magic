def hello():
    print("maybe next this will ask for a string")
    return "maybe next this will ask for a string"

def parse(stringElement):
    lastCharacter = stringElement[len(stringElement)-1:]
    print("the last character in your string is: " + lastCharacter)
    return lastCharacter

myString = hello()
parse(myString)


