import time
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


class Run():
    def __init__(self):
        self.statue = None

    def check(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--disable-gpu')
        option.add_argument(
            "user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")

        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        driver = webdriver.Chrome(executable_path=r'D:\Python\Pythoncode\爬虫软件\chromedriver_win32\chromedriver.exe',
                                  options=option)

        list_url = 'http://www.dahepiao.com/news1/2019010560825.html'
        driver.get(list_url)

        a = driver.find_elements_by_xpath('//div[@class="detail liebiao"]//div[@class="detail1"]//blockquote')[0]
        s = a.text
        b = s.split()
        print(s)

        for i in b[:1]:
            if i == '许巍广州演唱会时间：待公开':
                print('未放票')
                self.statue = b
            else:
                print('放票了')
                self.statue = b

        driver.close()

    def send_email(self):

        my_sender = '1411789366@qq.com'  # 发件人邮箱账号
        my_pass = 'yusqrqfuagidihid'  # 发件人邮箱密码
        my_user = '1411789366@qq.com'  # 收件人邮箱账号，我这边发送给自己

        msg = MIMEText('{}'.format(self.statue), 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "许巍演唱会门票详情！"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发

        server.quit()  # 关闭连接



    def run(self):
        # self.send_email(u"1411789366@qq.com", u"1411789366@qq.com", u"主题", u"yusqrqfuagidihid")
        for i in range(1):
            self.check()
            # self.send_email()
            time.sleep(10)
            print(i)

a = Run()
a.run()
