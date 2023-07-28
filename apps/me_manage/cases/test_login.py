# -*- coding: utf-8 -*-
from apps.me_manage.api.api import cases_info, CaseInfo
from common.http_client import client
from loguru import logger
import pytest
from apps.me_manage.datas.login_data.test_data_login_list import login_data_list
from tool.read_yml import read_yaml, read_json


# login-id = e504df6039349211dae5ca82e4f94fe3
class TestLogin:
    def setup_class(self):
        print('setup!!class!!!')

    def teardown_class(self):
        print('teardown!!!!class')

    def setup_method(self):
        print('setup!!method!!!')

    def teardown_method(self):
        print('teardown!!!!method')

    def test_login(self, test_module, test_session, test_package):
        login_case: CaseInfo = cases_info.get("e504df6039349211dae5ca82e4f94fe3")
        login_case.parameters = dict(account="admin", pwd="admin123", valid_code="6666")
        test_data = dict(method=login_case.method, url=login_case.url, json=login_case.parameters)
        res = client.do_request(**test_data).json()
        logger.info(f"token:{res}")
        logger.info(f"token:{res['data']['token']}")
        assert res['code'] == 0 and res['data']['token'] is not None

    @pytest.mark.parametrize("tast_data_py", login_data_list)
    def test_login_inexistence_py(self, tast_data_py):
        """不存在的用户，py文件参数化"""

        username = tast_data_py['username']
        password = tast_data_py['password']
        valid_code = tast_data_py['valid_code']

        login_case: CaseInfo = cases_info.get("e504df6039349211dae5ca82e4f94fe3")
        login_case.parameters = dict(account=username, pwd=password, valid_code=valid_code)
        logger.info(f"url={login_case.url}")
        logger.info(login_case.parameters)
        test_data = dict(method=login_case.method, url=login_case.url, json=login_case.parameters)
        res = client.do_request(**test_data).json()
        logger.info(f"response{res}")
        assert res['code'] == 40002
        assert "The user don't register, please check again!" in res['message']

    @pytest.mark.parametrize("tast_data_yml", read_yaml("../datas/login_data/test_data_login_list.yml"))
    def test_login_inexistence_yml(self, tast_data_yml):
        """不存在的用户，yml文件参数化"""

        username = tast_data_yml['username']
        password = tast_data_yml['password']
        valid_code = tast_data_yml['valid_code']

        login_case: CaseInfo = cases_info.get("e504df6039349211dae5ca82e4f94fe3")
        login_case.parameters = dict(account=username, pwd=password, valid_code=valid_code)
        logger.info(f"url={login_case.url}")
        logger.info(login_case.parameters)
        test_data = dict(method=login_case.method, url=login_case.url, json=login_case.parameters)
        res = client.do_request(**test_data).json()
        logger.info(f"response{res}")
        assert res['code'] == 40002
        assert "The user don't register, please check again!" in res['message']
        # assert 1==1

    @pytest.mark.parametrize("tast_data_json", read_json("../datas/login_data/test_data_login_list.json"))
    def test_login_inexistence_json(self, tast_data_json):
        """不存在的用户，json文件参数化"""

        username = tast_data_json['username']
        password = tast_data_json['password']
        valid_code = tast_data_json['valid_code']

        login_case: CaseInfo = cases_info.get("e504df6039349211dae5ca82e4f94fe3")
        login_case.parameters = dict(account=username, pwd=password, valid_code=valid_code)
        logger.info(f"url={login_case.url}")
        logger.info(login_case.parameters)
        test_data = dict(method=login_case.method, url=login_case.url, json=login_case.parameters)
        res = client.do_request(**test_data).json()
        logger.info(f"response{res}")
        assert res['code'] == 40002
        assert "The user don't register, please check again!" in res['message']

    @pytest.mark.parametrize("user,pwd", [("admin", "12345"), ("admin", "1234566"), ("admin", "123444225")])
    def test_login_password_err(self, user, pwd):
        """密码错误，直接参数化"""
        login_case: CaseInfo = cases_info.get("e504df6039349211dae5ca82e4f94fe3")
        login_case.parameters = dict(account=user, pwd=pwd, valid_code="6666")
        logger.info(f"url={login_case.url}")
        logger.info(login_case.parameters)
        test_data = dict(method=login_case.method, url=login_case.url, json=login_case.parameters)
        res = client.do_request(**test_data).json()
        logger.info(f"response{res}")
        assert res['code'] == 50011
        assert "The user don't exist or passwd err" in res['message']
