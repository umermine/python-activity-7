#Adding variables
num = int(input("Enter a number "))
sum = 0
temp = num
#Writing code
while temp > 0:
    diget = temp % 10
    sum += diget ** 3
    temp //= 10
if num == sum:
    print(sum," is an Armstrong number")
else:
    print(sum," is not an Armstrong number")