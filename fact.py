def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

num = int(input('Input a number to compute the factorial: '))
print(f'\nThe factorial of {num} is {fact(num)}')
