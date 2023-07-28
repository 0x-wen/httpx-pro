# -*- coding: utf-8 -*-
import inspect

from apps.me_manage.api.api import cases_info, CaseInfo
from common.http_client import client
from loguru import logger
from tool.name import UserInfo
import pytest
@pytest.mark.usefixtures('get_wang_token')
class TestRole():
    token ='s'
    def test_role_post001(self, get_wang_token):
        # 创建一个角色，定义好一个角色权限
        pass
