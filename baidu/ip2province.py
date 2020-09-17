#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    @version: v1.0
    @author: HunWong
    @license: Apache Licence
    @time: 2020/09/17
"""
import json
import requests

# 百度地图开放平台 http://lbsyun.baidu.com/
ak = '百度地图开放平台中配置的访问应用AK'


def ip2province(ip):
    url = f"https://api.map.baidu.com/location/ip?ak={ak}&ip={ip}&coor=bd09ll"
    response = json.loads(requests.get(url).text)
    if response.get('status') == 0 and response.get('address'):
        print(response.get('address'))
        print(dict(response=response))
        try:
            province = response.get('address').split('|')[1]
        except ValueError:
            return dict(msg='数据解析失败', code=response.get('status'), data={}, status_code=200)
        return dict(msg='查询成功', code=response.get('status'), data=dict(province=province), status_code=200)
    return dict(msg='查询失败', code=response.get('status'), data=response, status_code=404)


if __name__ == '__main__':
    print(ip2province('14.215.177.39'))
    print(ip2province('www.baidu.com'))
