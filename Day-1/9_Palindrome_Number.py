# Problem: 9 - Palindrome Number

# Logic:
# Extract digits using %10
# Build reverse using rev*10 + digit
#create temp variable to campare both


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        rev = 0

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        return temp == rev
