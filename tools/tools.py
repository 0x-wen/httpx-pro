

from common.http_client import client

from apps.me_manage.api.api import CaseInfo, cases_info


def get_token():
    login_case: CaseInfo = cases_info.get("e504df6039349211dae5ca82e4f94fe3")
    login_case.parameters = dict(
        account="admin", pwd="admin123", valid_code="6666")
    test_data = dict(method=login_case.method,
                     url=login_case.url, json=login_case.parameters)
    res = client.do_request(**test_data).json()
    assert res['code'] == 0 and res['data']['token'] is not None
    return res['data']['token']


if __name__ == '__main__':
    print(get_token())
