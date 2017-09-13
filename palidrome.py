class Solution(object):
    def isPalindrome(self, x):
        #Cant be palidrome if its negative or a multiple of 10, so eliminate that 
        if (x < 0 or (x != 0 and x % 10 == 0)):
            return False
        rev = 0
        ori = x
        while(x > 0):
            #interates through each digit of the num, starting with the last one which is found by x%10
            #which is added to the reversed variable. the reversed value is *10 so that each loop will put
            #the digit back into its respective place, ex in 123, x%10 would be 3, and it will loop 3 times
            #so it will end up having to be 300 in the final number
            rev = rev*10 + (x%10)
            #integer division to floor the number
            x //= 10
        #check if its a palindrome
        if(rev == ori):
            return True
        else:
            return False 
    #for debugging
    print(isPalindrome(0, int(input())))