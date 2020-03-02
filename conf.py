# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "lexinhu/site-Wiki@gh-pages"
}

# 站点设置
site_name = "心湖维基"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "乐心湖"
email = "jialna@qq.com"
author_homepage = "https://www.xn2001.com"
description = "愿此地一片净土,个人维基站"
key_words = ['乐心湖', '维基', '心湖维基', 'blog','技术']
language = 'zh-CN'
external_links = [
    {
        "name": "乐心湖",
        "url": "https://www.xn2001.com",
        "brief": "乐心湖的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${/}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Blog",
        "url": "https://www.xn2001.com",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/lexinhu",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5245109677/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''