# -*- coding: utf-8 -*-
import xlsxwriter


# 生成excel文件
def generate_excel(expenses):
    workbook = xlsxwriter.Workbook('./rec_data.xlsx')
    worksheet = workbook.add_worksheet()

    # 设定格式，等号左边格式名称自定义，字典中格式为指定选项
    # bold：加粗，num_format:数字格式
    bold_format = workbook.add_format({'bold': True})
    # money_format = workbook.add_format({'num_format': '$#,##0'})
    # date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

    # 将二行二列设置宽度为15(从0开始)
    worksheet.set_column(1, 1, 15)

    # 用符号标记位置，例如：A列1行
    worksheet.write('A1', 'sku_id', bold_format)
    worksheet.write('B1', 'sku_title', bold_format)
    worksheet.write('C1', 'id_1', bold_format)
    worksheet.write('D1', 'id_1_doc', bold_format)
    worksheet.write('E1', 'id_2_doc', bold_format)
    worksheet.write('F1', 'id_2_doc', bold_format)
    row = 1
    col = 0
    for item in (expenses):
        # 使用write_string方法，指定数据格式写入数据
        worksheet.write_string(row, col, str(item['sku_id']))
        worksheet.write_string(row, col + 1, item['sku_title'])
        worksheet.write_string(row, col + 2, str(item['id_1']))
        worksheet.write_string(row, col + 3, item['id_1_doc'])
        worksheet.write_string(row, col + 4, str(item['id_2']))
        worksheet.write_string(row, col + 5, item['id_2_doc'])
        row += 1
    workbook.close()


if __name__ == '__main__':
    rec_data = [{'sku_id': 2685373, 'id_1': 16161212, 'id_2': 23853166, 'id_2_doc': u'【分享/吐槽大会】宝宝发烧用退热贴真的有效吗？',
                 'sku_title': u'啾啾 CHUCHU 新宝宝水枕（适用年龄0岁以上）',
                 'id_1_doc': u'宝宝退热捷径，别忘了这些物理降温宝宝体内致热源刺激体温调节中枢导致产热增加、散热减少的症状即为发热。\n'},
                {'sku_id': 2685373, 'id_1': 16161212, 'id_2': 23853166, 'id_2_doc': u'【分享/吐槽大会】宝宝发烧用退热贴真的有效吗？',
                 'sku_title': u'啾啾 CHUCHU 新宝宝水枕（适用年龄0岁以上）',
                 'id_1_doc': u'宝宝退热捷径，别忘了这些物理降温宝宝体内致热源刺激体温调节中枢导致产热增加、散热减少的症状即为发热。\n'},
                {'sku_id': 2685373, 'id_1': 16161212, 'id_2': 23853166, 'id_2_doc': u'【分享/吐槽大会】宝宝发烧用退热贴真的有效吗？',
                 'sku_title': u'啾啾 CHUCHU 新宝宝水枕（适用年龄0岁以上）',
                 'id_1_doc': u'宝宝退热捷径，别忘了这些物理降温宝宝体内致热源刺激体温调节中枢导致产热增加、散热减少的症状即为发热。\n'},
                {'sku_id': 2685373, 'id_1': 16161212, 'id_2': 23853166, 'id_2_doc': u'【分享/吐槽大会】宝宝发烧用退热贴真的有效吗？',
                 'sku_title': u'啾啾 CHUCHU 新宝宝水枕（适用年龄0岁以上）',
                 'id_1_doc': u'宝宝退热捷径，别忘了这些物理降温宝宝体内致热源刺激体温调节中枢导致产热增加、散热减少的症状即为发热。\n'},
                {'sku_id': 2685373, 'id_1': 16161212, 'id_2': 23853166, 'id_2_doc': u'【分享/吐槽大会】宝宝发烧用退热贴真的有效吗？',
                 'sku_title': u'啾啾 CHUCHU 新宝宝水枕（适用年龄0岁以上）',
                 'id_1_doc': u'宝宝退热捷径，别忘了这些物理降温宝宝体内致热源刺激体温调节中枢导致产热增加、散热减少的症状即为发热。\n'}
                ]
    generate_excel(rec_data)