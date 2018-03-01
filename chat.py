import itchat
import result

downloadWePicturePath = 'weimage/'


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

@itchat.msg_register(itchat.content.PICTURE)
def download_files(msg):
    # msg.download(msg['FileName'])   #这个同样是下载文件的方式
    savePath = downloadWePicturePath + msg['FileName']
    msg['Text'](savePath)  # 下载文件
    # 将下载的文件发送给发送者
    # itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', downloadWePicturePath + msg["FileName"]),
    #             msg["FromUserName"])
    itchat.send("信息获取中",msg["FromUserName"])
    res = result.getResult(savePath)
    itchat.send('你要查询的人员信息：'+res,msg["FromUserName"])


itchat.auto_login()
itchat.run()
