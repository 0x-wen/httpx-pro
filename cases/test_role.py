# -*- coding: utf-8 -*-
import inspect

from apps.me_manage.api.api import cases_info, CaseInfo
from common.http_client import client
from loguru import logger
from tool.name import UserInfo
import pytest
from apps.me_manage.datas.login_data.test_data_login_list import login_data_list
from tool.read_yml import read_yaml, read_json


class TestRole():
    # token = get_wang_token()
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

    # @pytest.mark.skip
    def test_role_get001(self, get_wang_token):
        "查询接口 get"
        # 通过接口id找到接口，等下定义接口用
        # 定义token
        token, role_name = self.test_role_post001(get_wang_token)
        logger.info(f"{inspect.stack()[0][3]},token = {token},role_name = {role_name}")
        role_case: CaseInfo = cases_info.get("6869cbf4530638e81365206520a95ef2")
        logger.info(f"role_case:{role_case}")

        # 定义入参,必备请求头token和参数
        role_case.headers = dict(AuthToken=token)
        # 定义接口信息,请求方法，url,入参
        test_data = dict(method=role_case.method, url=role_case.url, headers=role_case.headers)
        # 接收响应
        res = client.do_request(**test_data).json()
        logger.info(f"res={res}")
        role_id = [i['v0'] for i in res['data'] if i['v3']==role_name]
        # for i in res['data']:
        #     if i['v3'] == role_name:
        #         role_id = i['v0']
        #         return role_id
        logger.info(f"{inspect.stack()[0][3]}role_id = {role_id}")
        # 断言
        # assert res['code'] == 0
        assert role_name in [i['v3'] for i in res['data']]
        return token, ''.join(role_id),role_name

    # @pytest.mark.skip
    def test_role_put001(self, get_wang_token):
        "更新接口 PUT"
        token, role_id,role_name = self.test_role_get001(get_wang_token)
        # 通过接口id找到接口，等下定义接口用
        role_case: CaseInfo = cases_info.get("257055bc79f0487ce606166e1b793f2d")
        # 定义token
        # 定义入参,必备请求头token和参数
        role_case.headers = dict(AuthToken=token)
        role_case.parameters = {"role_id": role_id, "role_name": role_name,
                                "role_list": [{"module_name": "group", "operate": "POST"},
                                              {"module_name": "group", "operate": "DELETE"},
                                              {"module_name": "group", "operate": "PUT"},
                                              {"module_name": "group", "operate": "GET"}]}
        # 定义接口信息,请求方法，url,入参
        test_data = dict(method=role_case.method, url=role_case.url, headers=role_case.headers,
                         json=role_case.parameters)
        # 接收响应
        res = client.do_request(**test_data).json()
        logger.info(f"res={res}")
        # 断言
        assert res['code'] == 0
        assert "Successfull to update role policy" in res['message']
        assert 1 == 1
        return token, role_id

    # @pytest.mark.skip

    # @pytest.mark.skip
    def test_role_delete001(self, get_wang_token):
        "角色管理接口 delete删除角色，这里注意看下数据库 "
        # 通过接口id找到接口，等下定义接口用
        # 定义token
        token, role_id = self.test_role_put001(get_wang_token)
        # token = get_wang_token
        # logger.info(f"token={token},role_id = {role_id}")
        role_case: CaseInfo = cases_info.get("b417d565c9663a79f3d26b74c74dde3a")

        # 定义入参,必备请求头token和参数
        role_case.headers = dict(AuthToken=token)
        role_name = "自动化测试用户1"
        role_case.parameters = {"role_id": role_id}
        # role_case.parameters = {"role_name": role_name, "role_list": [{"module_name": "kyc", "operate": "POST"},
        #                                                               {"module_name": "kyc", "operate": "DELETE"},
        #                                                               {"module_name": "kyc", "operate": "PUT"},
        #                                                               {"module_name": "kyc", "operate": "GET"},
        #                                                               {"module_name": "group", "operate": "POST"}]}
        # 定义接口信息,请求方法，url,入参
        test_data = dict(method=role_case.method, url=role_case.url, headers=role_case.headers,
                         params =role_case.parameters)
        # 接收响应
        res = client.do_request(**test_data).json()
        logger.info(f"res={res}")
        # 断言
        assert res['code'] == 0
        assert "Successfull remove the role and its permission" in res['message']
        assert 1 == 1
        # return token, role_name
