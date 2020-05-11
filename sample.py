def hello():
    print("hello from jenkins")
    return "hello from jenkins"

def parse(stringElement):
    lastCharacter = stringElement[len(stringElement)-1:]
    print("the last character in your string is: " + lastCharacter)
    return lastCharacter

myString = hello()
parse(myString)


