# Problem: 7 - Reverse Integer

# Logic:
# Extract digits using %10
# Build reverse using rev*10 + digit

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        return sign * rev 
