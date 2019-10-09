# code=utf-8
'''
作者：Francis.zhao
github:https://github.com/Francis009zhao
时间：2018-12-13
'''

import tushare as ts

data = ts.get_stock_basics()
'''
    因为recent_data的数据类型是DataFrame，所以，以后可以将所有的数据reshape为DataFrame
    就可以用下面一句话搞定，将数据存储到本地。哦耶！！！
'''
data.to_csv('./data/stock.csv', sep=',', header=True, index=True, encoding='gbk')

print(data.head())