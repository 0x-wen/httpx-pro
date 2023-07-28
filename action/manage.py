# -*- coding: utf-8 -*-
import json
import string

from common.http_client import HttpxClient, client
from apps.me_manage.api.api import cases_info, CaseInfo
from loguru import logger
from tool.postgresql import pos


# 主要对管理后台所需要的操作步骤的进行一个封装
# class Login(HttpxClient):
#     def admin_login(self):
#         pass
class Manage(CaseInfo):
    @staticmethod
    def _token(account="admin", pwd="admin123"):
        login = cases_info.get('e504df6039349211dae5ca82e4f94fe3')
        login.parameters = dict(account=account, pwd=pwd, valid_code="6666")
        login_data = dict(method=login.method, url=login.url, json=login.parameters)
        login_res = client.do_request(**login_data).json()
        token = login_res['data']['token']
        logger.info(f"测试：token=：{token}")
        return token

    class Role(object):
        @staticmethod
        def role_id_get(role_name: str, info=False):
            """
            根据角色名称，取得角色id
            :param role_name: 角色名称
            :param info: 这个开关如果打开，就返回该角色的权限信息，而不返回id信息
            :return 角色id
            """
            # 管理员登录
            token = Manage._token()
            # 查询根据名称查询角色Id
            role = cases_info.get('6869cbf4530638e81365206520a95ef2')
            role.headers = dict(AuthToken=token)
            # 返回角色id
            role_data = dict(method=role.method, url=role.url, headers=role.headers)
            role_res = client.do_request(**role_data).json()['data']
            logger.info(f"role_res={role_res}")
            role_id_list = [i['v0'] for i in role_res if i['v3'] == role_name]
            logger.info(f"role_id_list={role_id_list}")
            role_id_str = ""
            if role_id_list == []:
                role_id_str = "查不到改用户，请检查一下用户名称是不是输入错了,也有可能是角色什么权限都没有"
                logger.info(f"{role_id_str}")
                return role_id_str
            else:
                if info:
                    role_data_info = dict(method=role.method, url=role.url, headers=role.headers, params=role_id_str)
                    role_info_res = client.do_request(**role_data_info).json()['data']
                    return role_info_res
                else:
                    role_id_str = role_id_list[0]
                    logger.info(f"role_id_str={role_id_str}")
                    return role_id_str
            # return role_id_str

        @staticmethod
        def role_info_get(role_name: str):
            """
            根据角色名称，取得角色id
            :param role_name: 角色名称
            :return 角色id
            """
            # 管理员登录
            token = Manage._token()
            # 查询根据名称查询角色Id
            role = cases_info.get('6869cbf4530638e81365206520a95ef2')
            role.headers = dict(AuthToken=token)

            # 返回角色id
            role_data_id = dict(method=role.method, url=role.url, headers=role.headers)
            role_res = client.do_request(**role_data_id).json()['data']
            logger.info(f"role_res={role_res}")
            role_id = [i['v0'] for i in role_res if i['v3'] == role_name]
            logger.info(f"role_id={role_id}")
            # role.parameters = "role_id="+role_id[0]
            role.parameters = None
            role_data_info = dict(method=role.method, url=role.url, headers=role.headers, params=role.parameters)
            role_info_res = client.do_request(**role_data_info).json()['data']

            logger.info(f"role_info_res={role_info_res}")
            return role_info_res
            # if role_id == []:
            #     return "查不到改用户，请检查一下用户名称是不是输入错了"
            # else:
            #     return role_id[0]

        @staticmethod
        def role_creat(role_name: str, kyc=False, group=False, staff=False, role=False, project=False, page=False,
                       language=False, content=False):
            """
            创建一个角色，必须要传角色名，其他的参数如果是Ture就是打开对于权限
            :param role_name: 角色名称
            :param kyc: 用户管理权限
            :param group: 群组管理权限
            :param staff: 员工管理权限
            :param role: 角色管理权限
            :param project: CMS项目管理权限
            :param page: CMS项目的页面的管理权限
            :param language: CMS语言权限
            :param content: CMS的内容权限
            :return: 角色id给下一个接口用，如果创建失败，返回None
            """
            # 拿到管理员token
            token = Manage._token()
            # 管理员创建角色，传入相关权限
            role_case: CaseInfo = cases_info.get('003f21857fb966145c7f74ac7224a1f4')
            role_case.headers = dict(AuthToken=token)
            # role_name = "role_name_test444"

            role_case.parameters = {"role_name": role_name, "role_list": []}
            if kyc:
                role_case.parameters["role_list"].extend([
                    {"module_name": "kyc", "operate": "POST"},
                    {"module_name": "kyc", "operate": "DELETE"},
                    {"module_name": "kyc", "operate": "PUT"},
                    {"module_name": "kyc", "operate": "GET"}
                ])
            if group:
                role_case.parameters["role_list"].extend([
                    {"module_name": "group", "operate": "POST"},
                    {"module_name": "group", "operate": "DELETE"},
                    {"module_name": "group", "operate": "PUT"},
                    {"module_name": "group", "operate": "GET"}
                ])
            if staff:
                role_case.parameters["role_list"].extend([
                    {"module_name": "staff", "operate": "POST"},
                    {"module_name": "staff", "operate": "DELETE"},
                    {"module_name": "staff", "operate": "PUT"},
                    {"module_name": "staff", "operate": "GET"}
                ])
            if role:
                role_case.parameters["role_list"].extend([
                    {"module_name": "role", "operate": "POST"},
                    {"module_name": "role", "operate": "DELETE"},
                    {"module_name": "role", "operate": "PUT"},
                    {"module_name": "role", "operate": "GET"}
                ])
            if project:
                role_case.parameters["role_list"].extend([
                    {"module_name": "project", "operate": "POST"},
                    {"module_name": "project", "operate": "DELETE"},
                    {"module_name": "project", "operate": "PUT"},
                    {"module_name": "project", "operate": "GET"}
                ])
            if page:
                role_case.parameters["role_list"].extend([
                    {"module_name": "page", "operate": "POST"},
                    {"module_name": "page", "operate": "DELETE"},
                    {"module_name": "page", "operate": "PUT"},
                    {"module_name": "page", "operate": "GET"}
                ])
            if language:
                role_case.parameters["role_list"].extend([
                    {"module_name": "language", "operate": "POST"},
                    {"module_name": "language", "operate": "DELETE"},
                    {"module_name": "language", "operate": "PUT"},
                    {"module_name": "language", "operate": "GET"}
                ])
            if content:
                role_case.parameters["role_list"].extend([
                    {"module_name": "content", "operate": "POST"},
                    {"module_name": "content", "operate": "DELETE"},
                    {"module_name": "content", "operate": "PUT"},
                    {"module_name": "content", "operate": "GET"}
                ])

            role_data = dict(method=role_case.method, url=role_case.url, headers=role_case.headers,
                             json=role_case.parameters)
            role_res = client.do_request(**role_data).json()
            logger.info(f"role_res = {role_res}")
            # 查询角色,拿到角色id 再返回出去
            role_id = Manage.Role.role_id_get(role_name=role_name)
            logger.info(f"role_le={role_id},type={type(role_id)}")
            return role_id

        @staticmethod
        def role_put(role_name: str, kyc=False, group=False, staff=False, role=False, project=False, page=False,
                     language=False, content=False):
            # 根据角色名称改变角色的权限
            # 拿到管理员token
            token = Manage._token()
            role_case: CaseInfo = cases_info.get('257055bc79f0487ce606166e1b793f2d')
            role_case.headers = dict(AuthToken=token)
            # role_name = "role_name_test444"
            # 查询角色,拿到角色id 再返回出去
            role_id = Manage.Role.role_id_get(role_name=role_name)
            logger.info(f"role_id={role_id},type={type(role_id)}")
            # Manage.Role.get_role_id(role_name=role_name,info=True)

            role_case.parameters = {"role_id": role_id, "role_name": role_name, "role_list": []}
            if kyc:
                role_case.parameters["role_list"].extend([
                    {"module_name": "kyc", "operate": "POST"},
                    {"module_name": "kyc", "operate": "DELETE"},
                    {"module_name": "kyc", "operate": "PUT"},
                    {"module_name": "kyc", "operate": "GET"}
                ])
            if group:
                role_case.parameters["role_list"].extend([
                    {"module_name": "group", "operate": "POST"},
                    {"module_name": "group", "operate": "DELETE"},
                    {"module_name": "group", "operate": "PUT"},
                    {"module_name": "group", "operate": "GET"}
                ])
            if staff:
                role_case.parameters["role_list"].extend([
                    {"module_name": "staff", "operate": "POST"},
                    {"module_name": "staff", "operate": "DELETE"},
                    {"module_name": "staff", "operate": "PUT"},
                    {"module_name": "staff", "operate": "GET"}
                ])
            if role:
                role_case.parameters["role_list"].extend([
                    {"module_name": "role", "operate": "POST"},
                    {"module_name": "role", "operate": "DELETE"},
                    {"module_name": "role", "operate": "PUT"},
                    {"module_name": "role", "operate": "GET"}
                ])
            if project:
                role_case.parameters["role_list"].extend([
                    {"module_name": "project", "operate": "POST"},
                    {"module_name": "project", "operate": "DELETE"},
                    {"module_name": "project", "operate": "PUT"},
                    {"module_name": "project", "operate": "GET"}
                ])
            if page:
                role_case.parameters["role_list"].extend([
                    {"module_name": "page", "operate": "POST"},
                    {"module_name": "page", "operate": "DELETE"},
                    {"module_name": "page", "operate": "PUT"},
                    {"module_name": "page", "operate": "GET"}
                ])
            if language:
                role_case.parameters["role_list"].extend([
                    {"module_name": "language", "operate": "POST"},
                    {"module_name": "language", "operate": "DELETE"},
                    {"module_name": "language", "operate": "PUT"},
                    {"module_name": "language", "operate": "GET"}
                ])
            if content:
                role_case.parameters["role_list"].extend([
                    {"module_name": "content", "operate": "POST"},
                    {"module_name": "content", "operate": "DELETE"},
                    {"module_name": "content", "operate": "PUT"},
                    {"module_name": "content", "operate": "GET"}
                ])

            role_data = dict(method=role_case.method, url=role_case.url, headers=role_case.headers,
                             json=role_case.parameters)
            logger.info(f"role_case.parameters= {role_case.parameters}")
            role_res = client.do_request(**role_data).json()
            logger.info(f"role_res = {role_res}")

            return Manage.Role.role_id_get(role_name=role_name, info=True)
            # pass

        @staticmethod
        def role_delete(role_name=None):
            # 管理员登录
            token = Manage._token()
            # 查询根据名称查询角色Id
            role = cases_info.get('b417d565c9663a79f3d26b74c74dde3a')
            role.headers = dict(AuthToken=token)

            # 通过名字，拿到角色id
            role_id = Manage.Role.role_id_get(role_name=role_name)
            # logger.info(f"role_id={role_id}")
            role.parameters = "role_id=" + role_id
            # role.parameters = role_id
            role_data_info = dict(method=role.method, url=role.url, headers=role.headers, params=role.parameters)
            role_info_res = client.do_request(**role_data_info).json()

            logger.info(f"role_info_res={role_info_res}")
            return role_info_res

    class Staff(object):
        @staticmethod
        def staff_or_id_get(account=None):
            token = Manage._token()

            staff = cases_info.get('d15a0138e904d7dcd4b877616ea18de0')
            # 定义请求 参数就可以
            staff.headers = dict(AuthToken=token)
            page_and_size = "page=1&page_size=100000"
            role_data_info = dict(method=staff.method, url=staff.url, headers=staff.headers, params=page_and_size)
            role_info_res = client.do_request(**role_data_info).json()

            logger.info(f"role_info_res={role_info_res}")
            if account is not None:
                for i in role_info_res['data']['list']:
                    if i['account'] == account:
                        return i['ID']
                # return role_info_res['data']['list']
            else:
                return role_info_res

        @staticmethod
        def staff_post(role_id, account):
            # 拿token登录
            token = Manage._token()
            # 拿角色id
            # role_id = "e78c4ec2-676a-4024-93de-a21489daada3"
            # account="wang123123123211"
            # 定义接口传参
            staff = cases_info.get('57b791c2dd22dcbab1d2277587bb9734')
            staff.headers = dict(AuthToken=token)
            staff.parameters = {"name": "汪汪汪汪汪2", "account": account, "pwd": "111111",
                                "role_id": role_id, "is_actived": "1",
                                "phone": "131111111111", "comment": "123123123"}
            staff_data = dict(method=staff.method, url=staff.url, headers=staff.headers, json=staff.parameters)
            # 传参
            staff_res = client.do_request(**staff_data).json()
            logger.info(f"staff_res = {staff_res}")
            pass

        @staticmethod
        def staff_put(role_id, account, comment):
            # 拿token登录
            token = Manage._token()
            # 拿角色id
            # account="wang12312312321asdas"
            # role_id = "e78c4ec2-676a-4024-93de-a21489daada3"
            # id = Manage.Staff.get_staff_or_id(account=account)
            # 定义接口传参
            staff = cases_info.get('44c36c7d3fe5da033f41f0b94bfbaed1')
            staff.headers = dict(AuthToken=token)
            staff.parameters = {"name": "汪汪汪汪汪2", "portrait": "", "account": account,
                                "role_id": role_id, "is_actived": "1",
                                "phone": "13111111111", "comment": comment, "ID": 55}
            staff_data = dict(method=staff.method, url=staff.url, headers=staff.headers, json=staff.parameters)
            # 传参
            staff_res = client.do_request(**staff_data).json()
            logger.info(f"staff_res = {staff_res}")
            return account

        @staticmethod
        def staff_delete(account: str):
            token = Manage._token()

            staff = cases_info.get('6f31065b894823fb00d2272608425457')
            # 定义请求 参数就可以
            staff.headers = dict(AuthToken=token)
            page_and_size = "account=" + account
            role_data_info = dict(method=staff.method, url=staff.url, headers=staff.headers, params=page_and_size)
            role_info_res = client.do_request(**role_data_info).json()
            logger.info(f"role_info_res={role_info_res}")
            return role_info_res

    class Group(object):
        @staticmethod
        def group_get():
            # 获取所有的群组
            # 拿token
            token = Manage._token()
            # 定义请求信息
            group = cases_info.get('7f4a0ddbf9118141838e7a788caf3870')
            group.headers = dict(AuthToken=token)
            group_data = dict(method=group.method, url=group.url, headers=group.headers)
            res = client.do_request(**group_data).json()
            logger.info(f"res = {res}")
            # 接收响应
            pass

        @staticmethod
        def group_post():
            pass

        @staticmethod
        def group_put():
            # 更新，审核群组
            # 拿token
            token = Manage._token()
            group = cases_info.get('ef67ce022619ab7bdb1b74abcb3b49b3')
            group.headers = dict(AuthToken=token)
            group.parameters = {
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
            group_data = dict(method=group.method, url=group.url, headers=group.headers, json=group.parameters)
            res = client.do_request(**group_data).json()
            logger.info(f"res = {res}")

            # 定义请求信息
            # 接收响应
            pass

        @staticmethod
        def group_delete():
            pass

    class Kyc(object):
        @staticmethod
        def kyc_get():
            # 获取所有的群组
            # 拿token
            token = Manage._token()
            # 定义请求信息
            kyc = cases_info.get('e6b3a3db3280f53b4232806e5bd7de14')
            logger.info(f"kyc={kyc}")
            kyc.headers = dict(AuthToken=token)
            logger.info(f"token={token}")
            group_data = dict(method=kyc.method, url=kyc.url, headers=kyc.headers)
            res = client.do_request(**group_data).json()
            # res_dict = json.load(res)
            # logger.info(f"type{type(res)}")
            res_list = res['data']['list']
            print(type(res_list))
            # r_n = []
            for i in res_list:
                del i['id_card'], i['face_image']

            new_list = res_list
            print(len(new_list))
            return new_list

        @staticmethod
        def kyc_post():
            # 更新，审核kyc
            # 拿token
            token = Manage._token()
            kyc = cases_info.get('6bbe612443c5783553e2c4a174c7097d')
            logger.info(f"kyc_info={kyc}")
            kyc.headers = dict(AuthToken=token)
            kyc.parameters = {
                "Face_id": "string",
                "address": "string",
                "create_at": "string",
                "deleted_at": {
                    "time": "string",
                    "valid": 'true'
                },
                "detect_status": "string",
                "email": "string",
                "face_image": "string",
                "first_name": "string",
                "gender": "string",
                "id": 0,
                "id_card": "string",
                "id_number": "string",
                "invitation_code": "string",
                "last_name": "string",
                "license_type": 0,
                "memo": "string",
                "nation": "string",
                "review_time": "string",
                "review_type": 0,
                "update_at": "string",
                "uuid": "string"
            }
            group_data = dict(method=kyc.method, url=kyc.url, headers=kyc.headers, json=kyc.parameters)
            res = client.do_request(**group_data).json()
            logger.info(f"res = {res}")

            # 定义请求信息
            # 接收响应
            pass

        @staticmethod
        def kyc_put():
            # 更新，审核kyc
            # 拿token
            token = Manage._token()
            kyc = cases_info.get('2696b44db0098da43f4e3f4a7b4e30c3')
            logger.info(f"kyc_info={kyc}")
            kyc.headers = dict(AuthToken=token)
            kyc.parameters = {
                "Face_id": "string",
                "address": "string",
                "create_at": "string",
                "deleted_at": {
                    "time": "string",
                    "valid": 'true'
                },
                "detect_status": "string",
                "email": "string",
                "face_image": "string",
                "first_name": "string",
                "gender": "string",
                "id": 0,
                "id_card": "string",
                "id_number": "string",
                "invitation_code": "string",
                "last_name": "string",
                "license_type": 0,
                "memo": "string",
                "nation": "string",
                "review_time": "string",
                "review_type": 0,
                "update_at": "string",
                "uuid": "string"
            }
            group_data = dict(method=kyc.method, url=kyc.url, headers=kyc.headers, json=kyc.parameters)
            res = client.do_request(**group_data).json()
            logger.info(f"res = {res}")

            # 定义请求信息
            # 接收响应
            pass

        @staticmethod
        def kyc_dele():
            pass


class UserGenerator:
    user_count = 0  # 类属性，用于记录编号计数器的值

    @classmethod
    def generate_user(cls):
        cls.user_count += 1  # 计数器增加一次
        return "自动化测试用的" + str(cls.user_count)  # 返回带有编号的字符串


if __name__ == '__main__':
    # Manage.Group.group_get()
    print(Manage.Kyc.kyc_get())
    # print(pos.host)
    # pos.close()
    # print(pos.select(table='user_roles', columns='*'))
    # role_name = "自动化测试用的3"
    # account = "wang12312312321"
    # for i in range(20):
    #     # role_name = "自动化4，kyc权限"+join(r)
    #     print(i)
    # for i in range(20):
    #     role_name = UserGenerator.generate_user()
    #     Manage.Role.creat_role(role_name=role_name,kyc=True,group=True)
    #     i+=1
    # print(UserGenerator.generate_user())
    # Manage.token(account="wangwang",pwd="111111")
    # print("role_id是：", Manage.Role.creat_role())
    # print(Manage.Role.get_role_info(role_name="自动化4，kyc权限"))
    # print(Manage.Role.get_role_id(role_name="自动化4，kyc权限"))
    # Manage.Role.creat_role(role_name=role_name,kyc=True,project=True)
    # Manage._token()
    # print(Manage.Role.put_role(role_name=role_name))
    # print(Manage.Role.creat_role(role_name="自动化5，kyc权限",kyc=True,group=True,project=True))
    # print(Manage.Role.delete_role(role_name=role_name))
    # print(Manage.Staff.staff_or_id_get(account=account))
    # print(Manage.Staff.get_staff())
    # Manage.Staff.post_staff()
    # Manage.Staff.delete_staff(account="wang1231231232")
    # Manage.Staff.put_staff(comment="测试一下！1111！")
