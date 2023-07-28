# -*- coding: utf-8 -*-
import inspect

from apps.me_manage.api.api import cases_info, CaseInfo
from common.http_client import client
from loguru import logger
from tool.name import UserInfo
from tool.get_token import get_token_admin,get_token_user
import pytest
from apps.me_manage.datas.login_data.test_data_login_list import login_data_list
from tool.read_yml import read_yaml, read_json
from action.manage import Manage
# get_token()

class TestRole():
    admin_token = get_token_admin()
    def test_role001(self):
        # print(self.token)
        # 新建一个角色，
        account = 'testaccount001'
        role_id= Manage.Role.role_creat(role_name='测试角色1',role=True)
        # 新建一个用户，
        Manage.Staff.staff_post(role_id=role_id,account=account)
        # 用这个用户去登录
        user_token = get_token_user(account=account,pwd='111111')
        # 使用这个用户，去操作权限内的操作，
        role_get_res = Manage.Role.role_get_all(token=user_token)
        # logger.info(f"role_get_res={role_get_res}")

        # 使用这个用户，去操作权限外的操作
        # staff_get_res = Manage.Staff.staff_or_id_get()
        # 删除这个用户，
        # 删除这个权限
        # 删除数据库脏数据
        # logger.info(f"token={self.admin_token}")
        assert 1==1