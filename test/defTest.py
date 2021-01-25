def sum_list(alist):
    sum_temp = 0
    for i in alist:
        sum_temp += i
    return sum_temp


print(sum_list)  # 查看函数对象sum_list

my_list = [1, 2, 3, 4, 5]
my_sum = sum_list(my_list)
print("sum of my list :%d" % my_sum)
