l1 = [7,9,11,14,66,74,96]
x = 75
newl1 = []

for l in l1:
    if l > x:
        newl1.append(l)

print(f'The original list is {l1}\n')
print(f'All the numbers greater than 75 are {newl1}')
