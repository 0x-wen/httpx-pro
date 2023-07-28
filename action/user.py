# -*- coding: utf-8 -*-
from common.http_client import HttpxClient, client
from apps.me_manage.api.api import cases_info, CaseInfo
from loguru import logger
from tool.postgresql import pos


# 主要对管理后台所需要的操作步骤的进行一个封装
# class Login(HttpxClient):
#     def admin_login(self):
#         pass
class User(CaseInfo):
    @staticmethod
    def _token(account="admin", pwd="admin123"):
        login = cases_info.get('e504df6039349211dae5ca82e4f94fe3')
        login.parameters = dict(account=account, pwd=pwd, valid_code="6666")
        login_data = dict(method=login.method, url=login.url, json=login.parameters)
        login_res = client.do_request(**login_data).json()
        token = login_res['data']['token']
        logger.info(f"测试：token=：{token}")
        return token

    class Login():
        @staticmethod
        def sign_in_post():  # 登录
            # 定义链接，
            sign_in = cases_info.get('2b3edfd4d56ce0d569e33d5d31893e76')
            logger.info(f"sign_in={sign_in}")
            # 定义传参
            sign_in.parameters = dict(email='1', email_code='2')
            sign_in_data = dict(method=sign_in.method, url=sign_in.url, json=sign_in.parameters)
            # 获取响应
            res = client.do_request(**sign_in_data).json()
            logger.info(f"res={res}")
            pass

        @staticmethod
        def sign_up_post():  # 注册
            # 定义链接，
            sign_up = cases_info.get('56a6b9dd548d8d9c56622ce431821c1e')
            logger.info(f"sign_up={sign_up}")
            # 定义传参
            sign_up.parameters = dict(email='1111@gmail.com')
            sign_in_data = dict(method=sign_up.method, url=sign_up.url, json=sign_up.parameters)
            # 获取响应
            res = client.do_request(**sign_in_data).json()
            logger.info(f"res={res}")

            pass

    class CreateAddress():
        @staticmethod
        def create_address_post():
            # 定义链接，
            create_address = cases_info.get('37dd4c9be6bcf89b7b58df283f2a2cda')
            logger.info(f"create_address={create_address}")
            # 定义传参
            token = User._token()
            create_address.headers = dict(AuthToken=token)
            create_address.parameters = {
                "addr": "string",
                "createdAt": "string",
                "deletedAt": {
                    "time": "string",
                    "valid": 'true'
                },
                "id": 0,
                "updatedAt": "string",
                "uuid": "string"
            }
            sign_in_data = dict(method=create_address.method, url=create_address.url, headers=create_address.headers,
                                json=create_address.parameters)
            # 获取响应
            res = client.do_request(**sign_in_data).json()
            logger.info(f"res={res}")
            pass

    class Kyc():
        @staticmethod
        def kyc_get():
            # 定义链接，
            kyc_get = cases_info.get('2399a4686e5339df49054e656697998b')
            logger.info(f"kyc_get={kyc_get}")
            # 定义传参
            token = User._token()
            kyc_get.headers = dict(AuthToken=token)
            kyc_get.parameters = 'address str'
            sign_in_data = dict(method=kyc_get.method, url=kyc_get.url, headers=kyc_get.headers,
                                json=kyc_get.parameters)
            # 获取响应
            res = client.do_request(**sign_in_data).json()
            logger.info(f"res={res}")

    class Group():
        @staticmethod
        def group_get():
            # 定义链接，
            group_get = cases_info.get('1b1a21a26ad90ea2c65ec19fc72a62fb')
            logger.info(f"group_get={group_get}")
            # 定义传参
            token = User._token()
            group_get.headers = dict(AuthToken=token)
            group_get.parameters = 'address str'
            sign_in_data = dict(method=group_get.method, url=group_get.url, headers=group_get.headers,
                                json=group_get.parameters)
            # 获取响应
            res = client.do_request(**sign_in_data).json()
            logger.info(f"res={res}")

        @staticmethod
        def group_post():
            # 定义链接，
            group_post = cases_info.get('2ca0e8a6cd6e6fc6fba5600eb28eec62')
            logger.info(f"group_post={group_post}")
            # 定义传参
            token = User._token()
            group_post.headers = dict(AuthToken=token)
            group_post.parameters = {
                "admin_address": "string",
                "admin_uuid": "string",
                "chain_group_id": "string",
                "create_at": "string",
                "group_id": "string",
                "id": 0,
                "pet_name": "string",
                "region": "string",
                "review_type": 0
            }
            sign_in_data = dict(method=group_post.method, url=group_post.url, headers=group_post.headers,
                                json=group_post.parameters)
            # 获取响应
            res = client.do_request(**sign_in_data).json()
            logger.info(f"res={res}")

        @staticmethod
        def group_delete():
            # 定义链接，
            group_delete = cases_info.get('07d169b10edfafcab8dcf1fae594422e')
            logger.info(f"group_delete={group_delete}")
            # 定义传参
            token = User._token()
            group_delete.headers = dict(AuthToken=token)
            group_delete.parameters = 'address str'
            sign_in_data = dict(method=group_delete.method, url=group_delete.url, headers=group_delete.headers,
                                json=group_delete.parameters)
            # 获取响应
            res = client.do_request(**sign_in_data).json()
            logger.info(f"res={res}")

    class Member():
        @staticmethod
        def member_get():
            # 定义链接，
            member_get = cases_info.get('1f8a11695cddae935ca95044ef1fbdd0')
            logger.info(f"member_get={member_get}")
            # 定义传参
            token = User._token()
            member_get.headers = dict(AuthToken=token)
            member_get.parameters = 'group_id page page_size'
            sign_in_data = dict(method=member_get.method, url=member_get.url, headers=member_get.headers,
                                json=member_get.parameters)
            # 获取响应
            res = client.do_request(**sign_in_data).json()
            logger.info(f"res={res}")

        @staticmethod
        def member_post():
            member_post = cases_info.get('87b85b1012c7738219006aee61fb5008')
            logger.info(f"member_post={member_post}")
            # 定义传参
            token = User._token()
            member_post.headers = dict(AuthToken=token)
            member_post.parameters = {
                "address": "string",
                "create_at": "string",
                "group_id": "string",
                "id": 0,
                "name": "string",
                "nation": "string",
                "uuid": "string"
            }
            sign_in_data = dict(method=member_post.method, url=member_post.url, headers=member_post.headers,
                                json=member_post.parameters)
            # 获取响应
            res = client.do_request(**sign_in_data).json()
            logger.info(f"res={res}")

        @staticmethod
        def member_delete():
            member_delete = cases_info.get('cacfb63e75806ff55e73344366987adc')
            logger.info(f"member_delete={member_delete}")
            # 定义传参
            token = User._token()
            member_delete.headers = dict(AuthToken=token)
            member_delete.parameters = {
                "address": "string",
                "create_at": "string",
                "group_id": "string",
                "id": 0,
                "name": "string",
                "nation": "string",
                "uuid": "string"
            }
            sign_in_data = dict(method=member_delete.method, url=member_delete.url, headers=member_delete.headers,
                                json=member_delete.parameters)
            # 获取响应
            res = client.do_request(**sign_in_data).json()
            logger.info(f"res={res}")

    class Nft():
        @staticmethod
        def nft_get():
            # 定义链接，
            nft_get = cases_info.get('2fccbb4c129411899a0c706b732a02dc')
            logger.info(f"nft_get={nft_get}")
            # 定义传参
            token = User._token()
            nft_get.headers = dict(AuthToken=token)
            sign_in_data = dict(method=nft_get.method, url=nft_get.url, headers=nft_get.headers)
            # 获取响应
            res = client.do_request(**sign_in_data).json()
            logger.info(f"res={res}")

        @staticmethod
        def nft_post():
            nft_post = cases_info.get('40a2045c9fed0a5a04a523129a9f659c')
            logger.info(f"nft_post={nft_post}")
            # 定义传参
            token = User._token()
            nft_post.headers = dict(AuthToken=token)
            nft_post.parameters = {
                "avatar": "string",
                "uid": "string"
            }
            sign_in_data = dict(method=nft_post.method, url=nft_post.url, headers=nft_post.headers,
                                json=nft_post.parameters)
            # 获取响应
            res = client.do_request(**sign_in_data).json()
            logger.info(f"res={res}")


if __name__ == '__main__':
    # print(User.Login.sign_up_post())
    # print(User.Group.group_post())
    print(User.Nft.nft_post())