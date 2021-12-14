#Check permutation. Given 2 strings write a method to determine if one is a permutation of the other
def checkPerm(str1,str2):
    #array to represent the count of each letter
    arr = [0]*26
    for i in str1:
        #increment the ascii-97 index
        arr[ord(i)-97] +=1
    for i in str2:
        arr[ord(i)-97]-=1
    for i in arr:
        if i != 0:
            return False
    return True


s1 ="hecllo"
s2= "llehoc"
print(checkPerm(s1,s2))
