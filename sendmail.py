import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
#while True:
msg = MIMEText('你好，蓝胖', 'plain', 'utf-8')
msg['From'] = formataddr(["侯召顺", '13835544305@163.com'])
msg['To'] = formataddr(["sail", '995701749@qq.com'])
msg['Subject'] = "你好，蓝胖"

server = smtplib.SMTP("smtp.163.com", 25)
server.login("13835544305@163.com", "hello1234")
server.sendmail('13835544305@163.com', ['995701749@qq.com', ], msg.as_string())
server.quit()
print('ok')



