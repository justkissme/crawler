from twilio.rest import Client#用于给手机发送消息,自己注册才行,不能使用我的

account_sid = 'AC0c532124f2f92d98e2285da84e0f9f0d'
auth_token = 'd3ac34bde7ef6b91aefbc05959135f5e'
client = Client(account_sid,auth_token)

#列表发送形式
# text = ['1','2','3']
# a=("".join(text))
#列表发送不了，转换成字符串

#字数限制在68个汉字内
text = '今天是天气晴朗的日子今天是天气晴朗的日子今天是天气晴朗的日子今天是天气晴朗的日子今天是天气晴朗的日子今天是天气晴朗的日子今天是天气晴朗的'



message = client.messages.create(
    to = '+8618827511517',
    from_ = '+14434322044',
    body = text)
