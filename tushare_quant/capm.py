import pandas as pd
import tushare as ts

# 获取数据
pro = ts.pro_api()
wanke = pro.daily(ts_code='000002.SZ', start_date='20170101')
pingan = pro.daily(ts_code='601318.SH', start_date='20170101')
maotai = pro.daily(ts_code='600519.SH', start_date='20170101')
wanhua = pro.daily(ts_code='002415.SZ', start_date='20170101')
keda = pro.daily(ts_code='002230.SZ', start_date='20170101')
hs300 = pro.index_daily(ts_code='000300.SH', start_date='20170101')

# 仅保留收益率数据，且用日期作为index
# 然后按照日期排序（增序）
stock_list = [wanke, pingan, maotai, wanhua, keda, hs300]
for stock in stock_list:
    stock.index = pd.to_datetime(stock.trade_date)
df = pd.concat([stock.pct_chg / 100 for stock in stock_list], axis=1)
df.columns = ['wanke', 'pingan', 'maotai', 'wanhua', 'keda', 'hs300']
df = df.sort_index(ascending=True)
df.describe()
