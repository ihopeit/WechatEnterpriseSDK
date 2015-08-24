from wechat_sdk import *
we = WeChatEnterprise(agentid=0)

#print(we.get_user('david'))

status,res = we.send_msg_to_user('test from py wechat',safe=0)

print("status:%s res:%s" % (status,res))
