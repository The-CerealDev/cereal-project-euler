def isPalindrome(number): #palindrome checking function 
    normal = str(number)
    reverse = ""
    for i in range(1,len(normal)+1):
        reverse+=normal[-i] #negative index to reverse the number 
    if reverse == normal:
        return True
    else:
        return False

largest_palindrome = [0,0,0] # [n1,n2,num]
n1 = 100
n2 = 999
num = n1 * n2
# while (n1 != 999):
#     n1 +=1
#     n2 -= 1 
#     num = n1 * n2 
    
    # if isPalindrome(num) == True:
    #     print(f"{n1} x {n2} = {num}")
    #     if num > largest_palindrome:
    #         largest_palindrome = num
    #         print(f"largest = {num}")
    # else:
        # print("-") #incorrect approach to solving this problem 
for n1 in range(100,1000):
    for n2 in range(100,1000):
        num = n1 * n2
        if isPalindrome(num):
            print(f"{n1} x {n2} = {num}")
            if num > largest_palindrome[2]:
                largest_palindrome = n1,n2,num
                print(largest_palindrome)
        
print(largest_palindrome)

#(913, 993, 906609) that's what i get , id say this is a very inefficient approach and i shall improve it 
#correct