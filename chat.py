import itchat

downloadWePicturePath = 'weimage/'


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text


@itchat.msg_register(itchat.content.PICTURE)
def picture_reply(msg):
    return "不要给我发图片"


@itchat.msg_register(itchat.content.PICTURE)
def download_files(msg):
    # msg.download(msg['FileName'])   #这个同样是下载文件的方式
    msg['Text'](downloadWePicturePath + msg['FileName'])  # 下载文件
    # 将下载的文件发送给发送者
    itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', downloadWePicturePath + msg["FileName"]),
                msg["FromUserName"])


itchat.auto_login()
itchat.run()
