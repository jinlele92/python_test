# Topic     : 编程找出10000以内的完全数
# Author    : Lele Jin
# Created   : 11/17/2018
digit = int(input('请输入一个大于1的任意数，可以得到该数的完全数表达式：\n'))
for num in range(2, digit):
    result = []
    flag = num
    for factor in range(1, num):
        if num % factor == 0:
            flag -= factor
            result.append(factor)
    if flag == 0:
        print(num,end='=')
        result_length = len(result)
        for i in range(result_length):
            if i != result_length - 1:
                print(result[i], end='+')
            else:
                print(result[i])