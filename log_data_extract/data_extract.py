#!/usr/bin/env python
# coding=utf-8


def train_log_data_extract(file_path):
    dev_count = 0
    test_count = 0
    dev_data = {
        'ALL': [],
        'FORESTRY': [],
        'PARK': [],
        'UNIT': [],
    }
    test_data = {
        'ALL': [],
        'FORESTRY': [],
        'PARK': [],
        'UNIT': [],
    }
    f1_data = []
    with open(file_path, "r", encoding='utf-8', errors='ignore') as f:
        line = f.readline()
        while line:
            if 'evaluate:dev' in line:
                dev_count = dev_count + 1
                for i in range(10):
                    line = f.readline().replace('\n', '')
                    if 'accuracy' in line:
                        data_list = line.split('-')[-1].strip().split(';')
                        key_value_extract_core(data_list, dev_data, 'ALL')
                    elif 'FOREST' in line:
                        data_list = line.split('FOREST:')[-1].split(';')
                        key_value_extract_core(data_list, dev_data, 'FORESTRY')
                    elif 'PARK' in line:
                        data_list = line.split('PARK:')[-1].split(';')
                        key_value_extract_core(data_list, dev_data, 'PARK')
                    elif 'UNIT' in line:
                        data_list = line.split('UNIT:')[-1].split(';')
                        key_value_extract_core(data_list, dev_data, 'UNIT')
            elif 'evaluate:test' in line:
                test_count = test_count + 1
                for i in range(10):
                    line = f.readline().replace('\n', '')
                    if 'accuracy' in line:
                        data_list = line.split('-')[-1].strip().split(';')
                        key_value_extract_core(data_list, test_data, 'ALL')
                    elif 'FOREST' in line:
                        data_list = line.split('FOREST:')[-1].split(';')
                        key_value_extract_core(data_list, test_data, 'FORESTRY')
                    elif 'PARK' in line:
                        data_list = line.split('PARK:')[-1].split(';')
                        key_value_extract_core(data_list, test_data, 'PARK')
                    elif 'UNIT' in line:
                        data_list = line.split('UNIT:')[-1].split(';')
                        key_value_extract_core(data_list, test_data, 'UNIT')
            elif 'new best test f1 score' in line:
                f1_data.append(line.replace('\n', '').split(':')[-1])
            line = f.readline()
    print(len(f1_data))


def key_value_extract_core(data_list, data_dict, tag):
    temp_list = []
    for data in data_list:
        key_value = data.split(':')
        key = key_value[0].strip()
        value = key_value[1].strip().replace('\t', '').replace('%', '')
        temp_list.append(value.split('  ')[0])
    data_dict[tag].append(temp_list)


if __name__ == '__main__':
    file_path = r'C:\Users\dhz\Desktop\train_log'
    train_log_data_extract(file_path)