# -*- coding: utf-8 -*-
import httpx
from loguru import logger
from singleton.singleton import Singleton



@Singleton
class HttpxClient(object):
    """定义连接"""
    def __init__(self, **kwargs):
        """属性，默认字典传参"""
        self.client = httpx.Client(**kwargs)
        # httpx.Client 和 requests.Session 的作用是类似的

    def __getattr__(self, name):
        """当用.查找属性是，找不到的话，就会调用这个方法"""
        return getattr(self.client, name)

    def do_request(self, method, url, **kwargs) -> httpx.Response:
        """建立连接，返回响应"""
        response = None
        try:
            response = self.client.request(method, url, **kwargs)
            # logger.info(f"url = {response.url}")
            # logger.info(f"kwargs = {kwargs}")
            response.raise_for_status()
        except httpx.HTTPError as exc:
            logger.error(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        return response

    def __del__(self):
        """ del类似于C里面的析构函数，清理实例化，"""
        self.client.close()


HttpxClient.initialize(**dict(base_url="http://192.168.0.207:8080"))
client: HttpxClient = HttpxClient.instance() # 单例模式的实现方式之一。在单例模式中，一个类只能创建一个实例对象，这个对象可以在整个应用程序中被共享和访问。
# def get_token():
#     login_case: CaseInfo = cases_info.get("e504df6039349211dae5ca82e4f94fe3")
#     login_case.parameters = dict(account="wangwang3", pwd="111111", valid_code="644666")
#     test_data = dict(method=login_case.method, url=login_case.url, json=login_case.parameters)
#     res = client.do_request(**test_data).json()
#     logger.info(f"token:{res}")
#     logger.info(f"token:{res['data']['token']}")
#     assert res['code'] == 0 and res['data']['token'] is not None
#     return res['data']['token']

if __name__ == '__main__':
    # 单例模式 clint 和 client3是同一个对象
    HttpxClient.initialize(**dict(base_url="http://192.168.0.206"))
    client3 = HttpxClient.instance()
    print(id(client3), client3.base_url)
