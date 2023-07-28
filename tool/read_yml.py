# -*- coding: utf-8 -*-
import os
import yaml
import json

def read_yaml(yaml_file_path):
    try:
        with open(yaml_file_path, "r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
    except:
        with open(yaml_file_path, "r", encoding="gbk") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
    print(value)
    return value

def read_json(json_file_path):
    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            datas = json.load(f)
    except:
        with open(json_file_path, "r", encoding="gbk") as f:
            datas = json.load(f)
    if not isinstance(datas, list):
        raise ValueError('json文件内的用例数据格式不符护规范')

    print(datas)
    return datas


if __name__ == '__main__':
    # read_yaml(r'../apps/me_manage/datas/login_data/test_data_login_list.yml')
    # read_json(r'../apps/me_manage/datas/login_data/test_data_login_list.json')
    pass
