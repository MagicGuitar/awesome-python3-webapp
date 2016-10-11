#!/usr/bin/env python3
#-*- coding: utf-8 -*-

__author__ = 'HZC'

import asyncio
import orm
import sys
from models import User, Blog, Comment

async def test(loop):
	await orm.create_pool(loop=loop, host='localhost', port=3306, user='www-data', password='www-data', db='awesome')
	u = User(name='Test', email='test@example.com', passwd='1234455', image='about:blank')
	await u.save()
	
if __name__ == '__main__':
	loop=asyncio.get_event_loop()
	loop.run_until_complete(test(loop))
	loop.close()
	if loop.is_closed():
		sys.exit(0)