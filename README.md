# WechatEnterpriseSDK
微信企业号sdk

usage:

	1. 配置 conf.py
    
     		CORPID = "****" # 企业号的corpid
		CORPSECRET = "***" #企业号的corpsecret
	
	2.
		from wechat_sdk import *
		we = WeChatEnterprise()
		# 创建部门
		we.create_department(name, parentid=1, order=None)
		# 其他方法类似， 注意是否有这个权限调用这些接口

注意事项：
发送消息时，如显示发送成功，但并没有收到：
status:True res:{u'errcode': 0, u'errmsg': u'ok'}

请检查agent id是否正确，agent id即是应用id, 可以在"应用中心"，点击应用查看。

TODO：
	1. 只加了一些主动调用的接口， 回调模式没做
