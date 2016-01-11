# (c) Copyright Ievgen Gavrylenko 2015 gavrilenko85@gmail.com
# This script generates full set of loyalty cards package
# Included main card number and barcode and numbers and barcodes for trinkets
import os
import csv
import time
def numgen(num):
    i = 1
    even = 0
    odd = 0
    res = 0
    while i <= 16:
        if i % 2 == 0:
            if int(num[i - 1]) * 2 >= 10:
                even += (int(num[i - 1]) * 2) - 9
            else:
                even += int(num[i - 1]) * 2
        else:
            odd += int(num[i - 1])
        i += 1
    if (even + odd) % 10 == 0:
        res = 0
    else:
        res = 10 - (even + odd) % 10
    return num + str(res)
def bargen(card_num):
    i = 1
    even = 0
    odd = 0
    res_first = 0
    res_second = 0
    while i <= 17:
        if i % 2 == 0:
            odd += int(card_num[i - 1])
        else:
            even += int(card_num[i - 1])
        i += 1
    res_second = int(card_num[-1]) * odd + even
    res_first = int(card_num[-1]) * even + odd
    if res_first % 10 != 0:
        res_first = 10 - res_first % 10
    else:
        res_first = 0
    if res_second % 10 != 0:
        res_second = 10 - res_second % 10
    else:
        res_second = 0
    return card_num + str(res_first) + str(res_second)
smart_first_numbers = '70044200'
# Put your start and end numbers here(generating range)
start_num = 3350001
end_num = 3390000
i = 1
each_row = []
equal_sign = '='
quotes = '"'
file_name = time.strftime('%Y_%m_%d_') + str(start_num) + '_' + str(end_num) + '_' + \
            str(int((end_num - start_num + 1) / 1000)) + 'k'
with open(os.path.join('/Users/admin/Documents/python/' + file_name + '.csv'), 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quotechar='', quoting=csv.QUOTE_NONE)
    spamwriter.writerow(['Card number', 'Card barcode'])
    while start_num <= end_num:
        card_num = numgen(smart_first_numbers + str(start_num) + '1')
        bar_num = equal_sign + quotes + str(bargen(card_num)) + quotes
        card_num = equal_sign + quotes + str(card_num) + quotes
        each_row.append(card_num)
        each_row.append(bar_num)
        spamwriter.writerow(each_row)
        each_row = []
        start_num += 1