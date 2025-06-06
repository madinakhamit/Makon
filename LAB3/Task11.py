def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    return s == s[::-1]  

text = input("Enter a word or phrase: ")  

if is_palindrome(text):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
