import itchat

itchat.auto_login()

user = itchat.search_friends(name=u'王亚华')[0]
user.send(u'机器人say hello')