# -*- coding: utf-8 -*-
from apps.me_manage.api.api import CaseInfo, cases_info
from common.http_client import client
from loguru import logger

def get_wang_token():
    login_case: CaseInfo = cases_info.get("e504df6039349211dae5ca82e4f94fe3")
    login_case.parameters = dict(account="wangwang3", pwd="111111", valid_code="644666")
    test_data = dict(method=login_case.method, url=login_case.url, json=login_case.parameters)
    res = client.do_request(**test_data).json()
    logger.info(f"token:{res}")
    logger.info(f"token:{res['data']['token']}")
    assert res['code'] == 0 and res['data']['token'] is not None
    return res['data']['token']

if __name__ == '__main__':
    print(get_wang_token())