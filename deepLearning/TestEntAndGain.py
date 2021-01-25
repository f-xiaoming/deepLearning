import numpy as np
import pandas as pd

data1 = pd.DataFrame({
    '天气': ['晴', '晴', '阴', '雨', '雨', '雨', '阴', '晴', '晴', '雨', '晴', '阴', '阴', '雨'],
    '温度': ['高', '高', '高', '低', '低', '低', '低', '低', '低', '低', '低', '低', '高', '低'],
    '湿度': ['高', '低', '高', '高', '高', '低', '低', '高', '低', '高', '低', '高', '低', '高'],
    '起风': [False, True, False, False, False, True, True, False, False, False, True, True, False, True],
    '打球': ['NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES', 'YES', 'YES', 'NO']})
data1[['天气', '温度', '湿度', '起风', '打球']]


# 定义计算熵的函数
def ent(data):
    prob1 = pd.value_counts(data) / len(data)
    return sum(np.log2(prob1) * prob1 * (-1))


# 定义计算信息增益的函数
def gain(data, str1, str2):
    e1 = data.groupby(str1).apply(lambda x: ent(x[str2]))
    p1 = pd.value_counts(data[str1]) / len(data[str1])
    e2 = sum(e1 * p1)
    return ent(data[str2]) - e2


# 测试
if __name__ == '__main__':
    gain_value = gain(data1, '天气', '打球')
    print(gain_value)
