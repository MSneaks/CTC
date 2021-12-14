#String Compression. 
def compress(str1):
    res = ""
    all_same = True
    start = 0
    end = len(str1)
    while start < end:
        res+=str(str1[start])
        count = 0
        walker = start
        while walker < end and str1[walker]==str1[start]:
            count+=1
            if count>1:
                all_same = False
            walker+=1
        res+=str(count)
        start = walker
    if all_same == True:
        return str1
    return res


s = "abc"
print(compress(s))
