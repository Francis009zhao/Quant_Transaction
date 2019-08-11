# conding=utf-8
from __future__ import print_function, absolute_import, unicode_literals
from gm.api import *

# 初始化
def init(context):
    # pass
    # 使用 schedule 函数进行定时任务配置
    # schedule(schedule_func=algo, date_rule='1d', time_rule='14:50:00')
    subscribe(symbols='SHSE.600000', frequency='1d')

def on_bar(context, bars):
    # 打印当前获取的bar信息
    bar = bars[0]
    print(bar)



# def algo(context):
#     # 购买200股浦发银行
#     order_volume(symbol='SHSE.600000', volume=200, side=OrderSide_Buy, order_type=OrderType_Market,
#                  position_effect=PositionEffect_Open, price=0)
if __name__ == "__main__":
    # run(strategy_id='7b4cea19-bb53-11e9-98c2-3c2c3098973f',
    #     filename='main.py',
    #     token='cedb0080f5889f76792bd8fb0f09411b3e87c6ae',
    #     backtest_start_time='2016-06-17 13:00:00', backtest_end_time='2017-08-21 15:00:00')
    run(strategy_id='7b4cea19-bb53-11e9-98c2-3c2c3098973f',
        filename='main.py',
        mode=MODE_BACKTEST,
        token='cedb0080f5889f76792bd8fb0f09411b3e87c6ae',
        backtest_start_time='2016-06-17 13:00:00',
        backtest_end_time='2017-08-21 15:00:00',
        backtest_adjust=ADJUST_PREV,
        backtest_initial_cash=10000000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001)