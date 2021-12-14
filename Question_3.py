#Replace all spaces in a string with %20
def replaceSpace(str1):
    res = ""
    for i in str1:
        if i == " ":
            res += "%20"
        else:
            res+=i
    return res

s = "Hello I am here"
print(replaceSpace(s))