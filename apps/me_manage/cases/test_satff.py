# -*- coding: utf-8 -*-
import inspect

from apps.me_manage.api.api import cases_info, CaseInfo
from common.http_client import client
from loguru import logger
from tool.name import UserInfo
import pytest
@pytest.mark.usefixtures('get_wang_token')
class TestRole():
    token =
    def test_role_post001(self, get_wang_token):
        "角色管理接口 post新增角色 "
        # 通过接口id找到接口，等下定义接口用
        role_case: CaseInfo = cases_info.get("003f21857fb966145c7f74ac7224a1f4")
        logger.info(f"role_case:{role_case}")
        # 定义token
        token = get_wang_token
        # 定义入参,必备请求头token和参数
        role_case.headers = dict(AuthToken=token)
        role_name = UserInfo.random_username()
        role_case.parameters = {"role_name": role_name, "role_list": [{"module_name": "kyc", "operate": "POST"},
                                                                      {"module_name": "kyc", "operate": "DELETE"},
                                                                      {"module_name": "kyc", "operate": "PUT"},
                                                                      {"module_name": "kyc", "operate": "GET"},
                                                                      {"module_name": "group", "operate": "POST"}]}
        # 定义接口信息,请求方法，url,入参
        test_data = dict(method=role_case.method, url=role_case.url, headers=role_case.headers,
                         json=role_case.parameters)
        logger.info(f"{inspect.stack()[0][3]}test_data={test_data}")
        # 接收响应
        res = client.do_request(**test_data).json()
        logger.info(f"res={res}")
        # 断言
        assert res['code'] == 0
        assert "Successfull to create a role" in res['message']
        assert 1 == 1
        logger.info(f"{token},{role_name}")
        return token, role_name
