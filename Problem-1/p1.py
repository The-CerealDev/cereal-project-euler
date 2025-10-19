max = 1000
n= 0
sum = 0
while n < max:
    if n % 5 == 0 or n % 3 == 0:
        print(n)
        sum += n 
    n+=1 
    
print(sum)