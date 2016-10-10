#!/usr/bin/env python3
#-*- coding: utf-8 -*-

__author__ = 'HZC'

'''
async web application
'''

import logging
#设置日志等级，默认为WAENING，只有指定级别或更高级的才会被追踪记录
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from  aiohttp import web

#定义处理http访问请求的方法
def index(request):
	return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html', charset = 'utf-8')
	
async def init(loop):
	#往web对象中加入消息循环，生成一个支持异步IO的对象
	app = web.Application(loop=loop)
	#将浏览器通过GET方式传过来的对根目录的请求转发给index函数处理
	app.router.add_route('GET', '/', index)
	#启动 监听127.0.0.1地址的9000端口
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv

#入口，固定写法
#获取eventloop然后加入运行时间	
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()