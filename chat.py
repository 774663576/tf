import itchat
import result
import db
downloadWePicturePath = 'weimage/'


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

@itchat.msg_register(itchat.content.PICTURE)
def download_files(msg):
    itchat.send("信息获取中",msg["FromUserName"])
    # msg.download(msg['FileName'])   #这个同样是下载文件的方式
    savePath = downloadWePicturePath + msg['FileName']
    msg['Text'](savePath)  # 下载文件
    # 将下载的文件发送给发送者
    # itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', downloadWePicturePath + msg["FileName"]),
    #             msg["FromUserName"])
    res = result.getResult(savePath)
    if  res == '未查询到员工信息':
        itchat.send('你要查询的员工信息：' + res, msg["FromUserName"])
    else:
       print("res--"+res)
       user_info=db.queryInfo(res)
       itchat.send('你要查询的员工信息：'+user_info,msg["FromUserName"])

itchat.auto_login()
itchat.run()
