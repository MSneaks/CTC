#Is Unique. Determine if a string has all unique characters
def isUnique(arr):
    seen = {}
    for i in arr:
        if i in seen:
            return False
        else:
            seen[i] = i
    return True

#Follow up. What if you cannot use additional data structures
def isU(arr):
    #We can check each element against all others in n^2 or we can sort in nlogn and check previous element.
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            return False
    return True


arr = ["a","b","c"]
print(isUnique(arr))
print(isU(arr))
