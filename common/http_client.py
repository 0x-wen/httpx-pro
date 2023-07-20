# -*- coding: utf-8 -*-
import httpx
from loguru import logger
from singleton.singleton import Singleton


@Singleton
class HttpxClient(object):
    def __init__(self, **kwargs):
        self.client = httpx.Client(**kwargs)

    def __getattr__(self, name):
        return getattr(self.client, name)

    def do_request(self, method, url, **kwargs) -> httpx.Response:
        response = None
        try:
            response = self.client.request(method, url, **kwargs)
            response.raise_for_status()
        except httpx.HTTPError as exc:
            logger.error(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        return response

    def __del__(self):
        self.client.close()


HttpxClient.initialize(**dict(base_url="http://192.168.0.207:8080"))
client: HttpxClient = HttpxClient.instance()

if __name__ == '__main__':
    # 单例模式 clint 和 client3是同一个对象
    HttpxClient.initialize(**dict(base_url="http://192.168.0.206"))
    client3 = HttpxClient.instance()
    print(id(client3), client3.base_url)
