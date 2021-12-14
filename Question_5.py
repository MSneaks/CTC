def oneAway(str1,str2):
    def oneExtra(str1,str2):
        if abs(len(str1)-len(str2))<=1:
            return True
        return False
    def oneReplace(str1,str2):
        d1 = {}
        difference = 0
        for i in str1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        first = 0
        for i in str2:
            if i in d1:
                d1[i]-=1
            else:
                if first == 0:
                    first+=1
                else:
                    difference+=1
        for i in d1:
            if d1[i]!=0:
                difference+=1
        if difference <=1:
            return True
        return False
    return oneExtra(str1,str2) and oneReplace(str1,str2)
print(oneAway("pale","bake"))
