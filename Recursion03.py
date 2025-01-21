#BackJoon Algorithm NO.25501
#Recursion
import sys
input = sys.stdin.readline

def recursion(s,l,r,N):
    N += 1 # Increment the counter for the recursion depth
    if l >= r:
        print(1, N)
        return
    elif s[l] != s[r]:
        print(0, N)
        return
    else:
        # Continue the recursion with the next characters
        return recursion(s, l+1, r-1, N)

def isPalindrome(s):
    return recursion(s,0,len(s)-1,0)

def main():
    Numb = int(input())
    for _ in range(Numb):
        # Read a word and remove leading/trailing whitespaces
        word = input().strip()
        isPalindrome(word)
    
if __name__ == '__main__':
    main()