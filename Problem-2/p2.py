fib = [1,2]
nextNo = 0
evenSum = 2 
highest = 4*(10**6)
while nextNo < highest:
    nextNo = fib[-1] + fib[-2]
    if nextNo % 2 == 0 and nextNo < highest:
        evenSum += nextNo
        
    fib.append(nextNo)

print(evenSum)