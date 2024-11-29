#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : 监控
# Desc      : 启动模块

import wbmonitor, bzmonitor, dymonitor, xhsmonitor
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
	'Connection': 'Keep-Alive',
	'Accept': 'text/html, application/xhtml+xml, */*',
	'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
	'Accept-Encoding': 'gzip, deflate',
	'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
	'Content-Type': 'application/json'
}

#调用的wxpusher平台
def notify_user(contents, summarys):
	url = 'http://wxpusher.zjiecode.com/api/send/message'
	datas = {
		"appToken":"AT_SvHqAVHGp78N79QLpa5sgtLC4pgcyp32",
		"content": contents,
		"summary": summarys,
		"contentType":1,
		"topicIds":[],
		"uids":[
			"UID_2Lk68GKb5e2NYMYRnJ5A1LcDku3U"
		],
		"url": ""
	}
	requests.post(url=url, headers=headers, json=datas).json()

def wbweixin(dicts):
	flag = True
	try:
		summarys = dicts['nickName'] + "发布新微博！\n"
		contents = "标题: "+dicts['text']+"\n"
		notify_user(contents, summarys)
	except Exception as e:
		print(e)
		flag = False
	return flag

def bzweixin(dicts):
	flag = True
	try:
		summarys = dicts['nickName'] + "B站更新了！\n"
		contents = "[B站]"
		notify_user(contents, summarys)
	except Exception as e:
		print(e)
		flag = False
	return flag

def dyweixin(dicts):
	flag = True
	try:
		summarys = dicts['nickName'] + "抖音更新了！\n"
		contents = "[抖音]"
		notify_user(contents, summarys)
	except Exception as e:
		print(e)
		flag = False
	return flag

def xhsweixin(dicts):
	flag = True
	try:
		summarys = dicts['nickName'] + "小红书更新了！\n"
		contents = "[小红书]"
		notify_user(contents, summarys)
	except Exception as e:
		print(e)
		flag = False
	return flag

def main():
	# 微博部分
	w = wbmonitor.WBMonitor()
	w.getWBInfo()
	with open('log/wbIds.txt', 'r') as f:
		text = f.read()
		if text == '':
			w.getWBQueue()
	try:
		newWB = w.startmonitor()
		if newWB is not None:
			print(wbweixin(newWB))#发送邮件成功则输出True
		print('微博部分运行成功')
	except:
		print('微博部分出现问题')

	# B站部分
	b = bzmonitor.bzMonitor()
	b.getBZUrl()
	with open('log/bilibili.txt', 'r') as f2:
		text = f2.read()
		if text == '':
			b.getBZQueue()
	try:
		newBZ = b.startbzmonitor()
		if newBZ is not None:
			print(bzweixin(newBZ))
		print('B站部分运行成功')
	except:
		print('B站部分出现问题')

	# 抖音部分
	d = dymonitor.dyMonitor()
	with open('log/douyin.txt', 'r') as f3:
		text = f3.read()
		if text == '':
			d.getDYQueue()
	try:
		newDY = d.startdymonitor()
		if newDY is not None:
			print(dyweixin(newDY))
		print('抖音部分运行成功')
	except:
		print('抖音部分出现问题')

	# 小红书部分
	x = xhsmonitor.xhsMonitor()
	with open('log/xiaohongshu.txt', 'r') as f4:
		text = f4.read()
		if text == '':
			x.getXHSQueue()
	try:
		newXHS = x.startxhsmonitor()
		if newXHS is not None:
			print(xhsweixin(newXHS))
		print('小红书部分运行成功')
	except:
		print('小红书部分出现问题')

if __name__ == '__main__':
	main()
