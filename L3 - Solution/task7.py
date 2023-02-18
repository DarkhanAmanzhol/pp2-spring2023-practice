def ispalindrome(string=None):
    index = len(string) - 1
    rightstring = ""
    while 0 <= index:
        rightstring += string[index]
        index = index - 1
    if rightstring == string:
        return True
    return False