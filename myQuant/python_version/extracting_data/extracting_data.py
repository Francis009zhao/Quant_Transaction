# # coding=utf-8
# from __future__ import print_function, absolute_import,unicode_literals
# from gm.api import *
#
# set_token('Francis009')
# data = history(symbol='SHSE.600000', frequency='1d', start_time='2015-01-01', end_time='2015-12-31', fields='open,high,low,close')
# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *
import xlwt
import xlsxwriter

def init(context):
    # 在init中一次性拿到所有需要的instruments信息
    # global instruments
    instruments = get_history_instruments(symbols='SZSE.000001,SZSE.000002',
                                          start_date=context.backtest_start_time,
                                          end_date=context.backtest_end_time)
    # 将信息按symbol,date作为key存入字典
    context.ins_dict = {(i.symbol, i.trade_date.date()): i for i in instruments}
    subscribe(symbols='SZSE.000001,SZSE.000002', frequency='1d')
    # print(type(context.ins_dict))
    # print(instruments)
    # print('............................................')
    # return instruments
    '''
    在本函数内以下定义是将数据输出为excel表格代码
    '''
    workbook = xlsxwriter.Workbook('./00000102_excel.xlsx')
    worksheet = workbook.add_worksheet()

    # 设定格式，等号左边格式名称自定义，字典中格式为指定选项
    # bold：加粗，num_format:数字格式
    bold_format = workbook.add_format({'bold': True})
    # 将二行二列设置宽度为15(从0开始)
    worksheet.set_column(1, 1, 15)
    # 用符号标记位置，例如：A列1行
    worksheet.write('A1', 'symbol', bold_format)
    worksheet.write('B1', 'sec_level', bold_format)
    worksheet.write('C1', 'multiplier', bold_format)
    worksheet.write('D1', 'margin_ratio', bold_format)
    worksheet.write('E1', 'pre_close', bold_format)
    worksheet.write('F1', 'upper_limit', bold_format)
    worksheet.write('G1', 'lower_limit', bold_format)
    worksheet.write('H1', 'adj_factor', bold_format)
    worksheet.write('I1', 'is_suspended', bold_format)
    worksheet.write('J1', 'settle_price', bold_format)
    worksheet.write('K1', 'position', bold_format)
    worksheet.write('L1', 'pre_settle', bold_format)
    worksheet.write('M1', 'trade_date', bold_format)

    row = 1
    col = 0
    for item in instruments:
        worksheet.write_string(row, col, str(item['symbol']))
        worksheet.write_string(row, col + 1, str(item['sec_level']))
        worksheet.write_string(row, col + 2, str(item['multiplier']))
        worksheet.write_string(row, col + 3, str(item['margin_ratio']))
        worksheet.write_string(row, col + 4, str(item['pre_close']))
        worksheet.write_string(row, col + 5, str(item['upper_limit']))
        worksheet.write_string(row, col + 6, str(item['lower_limit']))
        worksheet.write_string(row, col + 7, str(item['adj_factor']))
        worksheet.write_string(row, col + 8, str(item['is_suspended']))
        worksheet.write_string(row, col + 9, str(item['settle_price']))
        worksheet.write_string(row, col + 10, str(item['position']))
        worksheet.write_string(row, col + 11, str(item['pre_settle']))
        worksheet.write_string(row, col + 12, str(item['trade_date']))
        row += 1
    workbook.close()

def on_bar(context, bars):
    print(context.ins_dict[(bars[0].symbol, bars[0].eob.date())])



if __name__ == '__main__':
    run(strategy_id='7b4cea19-bb53-11e9-98c2-3c2c3098973f',
        filename='extracting_data.py',
        mode=MODE_BACKTEST,
        token='cedb0080f5889f76792bd8fb0f09411b3e87c6ae',
        backtest_start_time='2018-06-17 13:00:00',
        backtest_end_time='2018-08-21 15:00:00')
    # excel_data = [{'symbol': 'SZSE.000001', 'sec_level': 1, 'multiplier': 1.0,
    #                'margin_ratio': 1.0, 'pre_close': 8.8100004196167,
    #                'upper_limit': 9.69, 'lower_limit': 7.93,
    #                'adj_factor': 117.153036649639, 'is_suspended': 0,
    #                'settle_price': 0.0, 'position': 0, 'pre_settle': 0.0,
    #                'trade_date': 'datetime.datetime(2018, 8, 20, 0, 0, tzinfo=tzfile())'
    #                }]
    # generate_excel(excel_data)