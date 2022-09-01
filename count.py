file1 = open('lyrics.txt', 'r')
x = 0
cou = 0
listcount = []
filelist = file1.readlines()
file1.close()

'''Counting the number of words in a file and then finding the longest word and its location'''
for ln in filelist:
    cou = len(ln)
    listcount.append(cou)
    x += 1
print(f'The number of words in the file lyrics.txt is {x}')