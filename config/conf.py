# -*- coding: utf-8 -*-
import yaml


# @classmethod
def read_config():
    with open(file="../tool/postgresql.yml", mode='r') as p:
        data = yaml.safe_load(p)
        return data['dev']

config = read_config()
if __name__ == '__main__':
    # print(read_config())
    print(read_config())
    # print(config())