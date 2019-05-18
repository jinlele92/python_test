#输出国际象棋棋盘
# Lele Jin 2018.11.17
import sys
for i in range (8):
    for j in range(8):
        if (i + j) % 2 != 0:
            print(chr(42), end='')
           # print(chr(219), end='')
        else:
            print(' ', end='')
    print('\n', end='')
str = input('please input a string:\n')
letter = 0
space = 0
digit = 0
other = 0
for i in str:
    if i.isalpha():
        letter += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        digit += 1
    else:
        other +=1
print('letter = %d, space = %d, digit = %d, others = %d' %(letter, space, digit,other))