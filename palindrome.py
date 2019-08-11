def palindrome(A): 
    B = ''.join(reversed(A)) 
    if (A==B):
        return True
    return False
A=str(input())
C=palindrome(A) 
if (C): 
    print("yes") 
else: 
    print("no")
