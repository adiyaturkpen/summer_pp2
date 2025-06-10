def palindrome(s):
    s = s.lower().replace(" ", "") 
    if s == s[::-1]:
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")
s=input()
palindrome(s)
