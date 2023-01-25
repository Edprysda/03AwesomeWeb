'''
Author: Exarlos
Date: 2023-01-16 16:18:46
LastEditors: Exarlos
LastEditTime: 2023-01-26 03:38:50
Description: 世界上没有低级的法术,只有低级的法师!
'''
# 廖雪峰的python实战

from aiohttp import web
from datetime import datetime
import time
import json
import os
import aiohttp
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

# 这是一个路由表
routes = web.RouteTableDef()


# 这是一个装饰器-路由遇到这个网址就会调用这个函数
@routes.get('/')
async def hello(request):
    return web.Response(body=b'<h1>Awesome Hello World</h1>', content_type='text/html')


def init():
    # 新建一个app-web服务器，然后把路由表加进去
    app = web.Application()
    app.add_routes(routes)
    # 以前的代码要自建loop和自建跑app的runner，现在都集成了
    web.run_app(app, host='127.0.0.1', port=9000)
    logging.info("Server started at 127.0.0.1:9000...")


if __name__ == '__main__':
    init()
