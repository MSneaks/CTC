#Palindrome Permutation. Check if string is a permutation of a palindrome
def palPerm(str1):
    # if its a palindrome all counts of characters will be even except 1 at most. We can ignore spaces
    counts = {}
    for i in str1:
        i = i.lower()
        if i != " ":
            if i in counts:
                counts[i]+=1
            else:
                counts[i] = 1
    odd = 0
    for i in counts:
        if counts[i]%2 == 1:
            odd+=1
    if odd > 1:
        return False
    return True


s = "Tact Cota"
print(palPerm(s))