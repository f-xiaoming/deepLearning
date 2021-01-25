import numpy as np
import pandas as pd

test_1 = pd.DataFrame(np.random.rand(4, 4),
                      index=list('ABCD'), columns=list('1234'))  # 产生随机数,index行,columns列
test_2 = pd.DataFrame([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]],
                      index=list('1234'), columns=list('ABCD'))  # 自己输入
dic1 = {'name': ['小明', '小红', '狗蛋', '铁柱'],
        'age': [17, 20, 5, 40], 'sex': ['男', '女', '女', '男']}  # 使用字典进行输入
test_3 = pd.DataFrame(dic1, index=list('ABCD'))
print(test_1, '\n')
print(test_2, '\n')
print(test_3, '\n')