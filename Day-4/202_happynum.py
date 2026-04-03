#happy number  - sum of square of each digit until it becomes 1 or 7

num=19
while num>=10:
    sum=0
    while num>0:
        sum+=(num%10)**2
        num//=10
    num=sum  
if num==1 or num==7 :
    print("Happy_Number")
else:
    print("not happy")
    

#approch-02

n=19
while len(str(n))>1:
    n=sum(int(i)**2 for i in str(n))
print("happy") if n==1 or n==7 else print("not happy")
    