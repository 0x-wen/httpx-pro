# -*- coding: utf-8 -*-
from apps.me_manage.api.api import cases_info, CaseInfo
from common.http_client import client


# login-id = e504df6039349211dae5ca82e4f94fe3
class TestLogin:

    def test_login(self):
        login_case: CaseInfo = cases_info.get("e504df6039349211dae5ca82e4f94fe3")
        login_case.parameters = dict(account="admin", pwd="admin123", valid_code="6666")
        test_data = dict(method=login_case.method, url=login_case.url, json=login_case.parameters)
        res = client.do_request(**test_data).json()
        assert res['code'] == 0 and res['data']['token'] is not None
