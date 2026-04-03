# Problem: 1281 - Subtract Product and Sum

#logic :
#Extract digit
#Do two opertion 
#1) sum+=digit
#2) product*=digit

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_val = 0
        product = 1
        while n > 0:
            digit = n % 10
            sum_val += digit
            product *= digit
            n //= 10

        return product - sum_val


