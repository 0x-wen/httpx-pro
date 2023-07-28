# -*- coding: utf-8 -*-
import pytest
from apps.me_manage.api.api import cases_info, CaseInfo
from common.http_client import client
from loguru import logger
import time

@pytest.fixture()
def get_admin_token():
    login_case: CaseInfo = cases_info.get("e504df6039349211dae5ca82e4f94fe3")
    login_case.parameters = dict(account="admin", pwd="admin123", valid_code="6666")
    test_data = dict(method=login_case.method, url=login_case.url, json=login_case.parameters)
    res = client.do_request(**test_data).json()
    # logger.info(f"token:{res}")
    # logger.info(f"token:{res['data']['token']}")
    assert res['code'] == 0 and res['data']['token'] is not None
    return res['data']['token']


@pytest.fixture(scope='class')
def get_wang_token():
    login_case: CaseInfo = cases_info.get("e504df6039349211dae5ca82e4f94fe3")
    login_case.parameters = dict(account="wangwang3", pwd="111111", valid_code="644666")
    test_data = dict(method=login_case.method, url=login_case.url, json=login_case.parameters)
    res = client.do_request(**test_data).json()
    logger.info(f"token:{res}")
    logger.info(f"token:{res['data']['token']}")
    assert res['code'] == 0 and res['data']['token'] is not None
    return res['data']['token']

@pytest.fixture(scope='session')
def test_session():
    logger.info(f"session测试一下会怎样时间={time.asctime()}")
    yield
    logger.info(f"这个结束后执行吗")
    # print("会怎样？？")
    return "会怎样111"

@pytest.fixture(scope='module')
def test_module():
    logger.info(f"module测试一下会怎样时间={time.asctime()}")
    # print("会怎样？？")
    return "会怎样111"

@pytest.fixture(scope='package')
def test_package():
    logger.info(f"test_package测试一下会怎样时间={time.asctime()}")
    # print("会怎样？？")
    return "会怎样111"
    # pass
# if __name__ == '__main__':
#     print(get_wang_token())
#     # pass
