class Solution(object):
    def romanToInt(self, s):
        #create a dict for the roman numerals
        roman = {"I" : 1, "V": 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        #store the int representation
        num = 0
        #the last digit is always added so ignore it for now, and add it to the total after
        for i in range(len(s) - 1):
            #s[i] is being used as the key for the dict and compares the int representations of the next element
            #since if the next element is larger, you need to subtract it ex. IV = -1 + 5
            if roman[s[i]] < roman[s[i + 1]]:
                num -= roman[s[i]]
            #otherwise add it
            else:
                num += roman[s[i]]
        #add the last element
        num += roman[s[-1]]
        return(num)
    print(romanToInt(0, input()))