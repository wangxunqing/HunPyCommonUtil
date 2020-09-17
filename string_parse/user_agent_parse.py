#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    @version: v1.0
    @author: HunWong
    @license: Apache Licence 
    @time: 2020/09/17
"""
# request中User-Agent数据解析
# 安装 pip install pyyaml ua-parser user-agents
from user_agents import parse


def user_agent_parse(ua):
    user_agent = parse(ua)
    return str(user_agent).split(' / ')


if __name__ == '__main__':
    print(user_agent_parse(
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'))
