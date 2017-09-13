def is_palindrome(input_string):
    for i in range(len(input_string)//2):
       if input_string[i] != input_string[-i - 1]:
           return False
    return True
print(is_palindrome(input()))