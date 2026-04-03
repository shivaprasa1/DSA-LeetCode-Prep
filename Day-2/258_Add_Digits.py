# Problem: 258 - Add Digits

#logic :
#Extract digit and add each digit 
#take that result number
#again add each digit of that number
#Reapet Until number become single digit

class Solution:
    def addDigits(self, num: int) -> int:
      
        while num >= 10:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit
                num //= 10
            num = total
        return num


#approch - 02
num=123456
while len(str(num))>1:
    sum=0
    for i in str(num):
        sum+=int(i)
    num=sum
print(num)
            