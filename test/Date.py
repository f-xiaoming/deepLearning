import datetime

'''strptime()方法分析表示根据格式的时间字符串'''
dtstr = input('Enter the datetime :(20200218):')
dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
another_dtstr = dtstr[:4]+'0101'
another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
print(int((dt-another_dt).days)+1)
