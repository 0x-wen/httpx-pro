# -*- coding: utf-8 -*-
import string
import random


# from faker import Faker


class UserInfo:
    # faker = Faker()
    @classmethod
    def random_username(cls):
        """用faker模块写的随机名"""
        random_str = string.ascii_letters + string.digits
        username = "user" + ''.join(random.sample(random_str,4))
        return username


if __name__ == '__main__':
    print(UserInfo.random_username())