# Problem: 2520 - Count Digits
#logic:
#Extract each digit
#check if that digit is dividion by that org number
#if it is divided then count each number of that 

class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        count = 0
        while temp > 0:
            digit = temp % 10
            if digit != 0 and num % digit == 0:
                count += 1
            temp //= 10
        return count

#approch - 02
num=12
count=0
for i in str(num):
    if num%int(i)==0:
        count+=1
print(count)