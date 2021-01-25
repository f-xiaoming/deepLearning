s = "abcdefg12345"
print(s[3:9:1])
print(s[0:10:2])
# print(s[3:9:-1]) 有问题获得54321
# print(s[3:7:2])
# str.strip:去掉字符串前后的所有空格
# str.lstrip:去掉字符串左部的所有空格
# str.rstrip:去掉字符串右部的所有空格
# str.isalpha:判断字符串是否全是由字母构成
# str.isdigit:判断字符串是否全部由数字构成
# str.isalnum:判断字符串是否仅包含字母和数字，而不含特殊字符
s1 = "You are my sunshine"
u1, u2, u3, u4 = s1.split(' ')
print(u1)
# split:分割；jion：合并
# upper/lower/swapcase:大小写相关
# ljust/center/rjust:排版左中
# lower：全转小写
# upper:全转大写
# swapcase:大写转小写，小写转大写
# 变量赋值
# a,b,c=7,8,9
# ord
# chr
# 列表 增长操作 append操作/insert操作/extend操作，extend改变原来的列表，将一个列表追加到一个列表后面
# 列表 缩减操作 pop操作（根据序号进行提取，删除）/remove操作(数据对象)/clear操作(清空)
num = [1, 2, 7, 4, 3, 9, 0]
# num.reverse()
# print(num)
# num.sort()
# print(num)
print(*(reversed(num)))
print(*(sorted(num)))
print(num)
num.append(2)
print(num)
num.pop(0)
print(num)
print(num.index(0))  # 找到0首次出现的位置
# del alist[i] 删除第i个元素
# alist.index(item) 找到item的首次出现的位置
# alist.count(item) 返回item在列表中出现的次数
# alist.remove(item) 将item的首次出现删除
num1 = ['a', 'b', 'c']
print(num + num1)
print(num * 2)
print(sum(num))
print(min(num))
print(max(num))
# tuple
# student = {}
student = dict()
student = dict.fromkeys("name", "age")
bands = {'Marxes': ['more', 'Curly'], 'kk': [True, 'moon']}
print(bands['kk'])
poi = {(100, 100): 'Zhongguancun', (123, 23): 'Pizza'}
print(poi[(100, 100)])
print(poi[(123, 23)])
# key 可以是任意不可变类型（数值/字符串/元组）
# 字典中的元素value没有顺序，可以是任意类型，甚至也可以是字典

# update方法
student1 = {}
student1["name"] = "Tom"
student1["age"] = "20"
student1["gender"] = "male"
print(student1)
# bar = {"course": ["数学", "英语"]}
# student1.update(bar)
# print(student1)
student1["course"] = ['数学', '英语']
print(student1)
student1.update(friends=["Mike", "Alice"])
print(student1)
# del 操作：删除指定标签的数据项
# pop 操作：删除指定标签的数据项并返回数据值
