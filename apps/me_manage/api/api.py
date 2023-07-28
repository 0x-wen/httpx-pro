# -*- coding: utf-8 -*-
import hashlib
from dataclasses import dataclass

import yaml

from common.http_client import client


@dataclass
class CaseInfo:
    """dataclass数据类装饰器，将类变成数据类，不需要去定义类的__init__,__eq__,__repr__都会自动添加"""
    name: str
    description: str
    url: str
    method: str
    headers: dict
    parameters: dict


class API(object):
    client.client.auth = ("admin", "admin")

    def get_open_api(self):
        res = client.do_request("GET", "/swagger/doc.json")
        interfaces = res.json()['paths']
        return interfaces

    def extract_case_info(self, swagger_data: dict) -> dict[str, CaseInfo]:
        """提取请求信息，这个应该是把swagger的paths里的各种请求方法转成dict"""
        cases_info = dict()
        for path, methods in swagger_data.items():
            for method, method_data in methods.items():
                s = f"{path}+{method}"
                id = hashlib.md5(s.encode()).hexdigest()
                name = method_data.get("summary", "")
                description = method_data.get("description", "")
                url = path
                method = method.upper()
                headers = {param["name"]: param["description"] for param in method_data.get("parameters", []) if
                           param["in"] == "header"}
                parameters = {}
                data = dict(name=name, description=description, url=url, method=method, headers=headers,
                            parameters=parameters)
                cases_info[id] = CaseInfo(**data)
        return cases_info

    def case_file_bp(self):
        with open("api.yml", "w") as f:
            yaml.dump(self.get_open_api(), f)

        with open("../datas/case.yml", "w") as f:
            yaml.dump(self.extract_case_info(self.get_open_api()), f)

    def generate_cases(self):
        return self.extract_case_info(self.get_open_api())


api = API()
cases_info = api.generate_cases()

if __name__ == '__main__':
    api.case_file_bp()
    print(f"Total interface use cases:{len(cases_info)}")
#
#

    # print("1111111")
    # c = CaseInfo(name="as", description="a", url="asd", method="as", headers={"a": "1"}, parameters={"as": "asd"})
    # print(c)
