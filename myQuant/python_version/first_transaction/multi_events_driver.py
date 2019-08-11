# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals
from gm.api import *

def init(context):
    subscribe(symbols='SHSE.600000, SZSE.000001', frequency='1d',count=5, wait_group=True)


def on_bar(context, bars):
    for bar in bars:
        print(bar['symbol'], bar['eob'])

if __name__ == "__main__":
    run(strategy_id='7b4cea19-bb53-11e9-98c2-3c2c3098973f',
        filename='multi_events_driver.py',
        mode=MODE_BACKTEST,
        token='cedb0080f5889f76792bd8fb0f09411b3e87c6ae',
        backtest_start_time='2016-06-17 13:00:00',
        backtest_end_time='2018-08-21 15:00:00',
        backtest_adjust=ADJUST_PREV,
        backtest_initial_cash=10000000,
        backtest_commission_ratio=0.0001,
        backtest_slippage_ratio=0.0001)