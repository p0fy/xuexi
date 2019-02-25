import datetime
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.chrome.options import Options


class xxqg():

    def __init__(self):
        #self.broswer = webdriver.Chrome()
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.broswer = webdriver.Chrome(options=chrome_options)

    def active_detect(self):
        flag = True
        #首先判断是不是活跃时间
        now_time = datetime.datetime.now().time()
        active_time_start = ["06:00:00","12:00:00","20:00:00"]
        active_time_end = ["08:30:00","14:00:00","22:30:00"]
        for i in range(0,len(active_time_start)):
            start = datetime.datetime.strptime(active_time_start[i],'%H:%M:%S').time()
            end = datetime.datetime.strptime(active_time_end[i], '%H:%M:%S').time()
            if start<now_time<end:
                flag = True
            else:
                flag = flag
        return flag


    # 获取二维码
    def getQRCode(self):
        self.broswer.get("https://pc.xuexi.cn/points/login.html?ref=https://www.xuexi.cn/index.html")
        QRCodeTemp = self.broswer.find_elements_by_tag_name('iframe')[2]
        self.broswer.switch_to.frame(QRCodeTemp)
        return self.broswer.find_element_by_css_selector(".login_content>.login_body>.login_qrcode>.login_qrcode_content>img").get_attribute("src")

    # 二进制转换
    def imgio(self,img_data):
        with open("QRCode.png","wb+")as imgfile:
            imgfile.write(img_data)
            print("二维码已获取")



    # 生成二维码
    def QRShow(self):
        import base64
        Base64Data = self.getQRCode()
        data = Base64Data.split(",")[-1]
        img_binary = base64.b64decode(data)
        self.imgio(img_binary)
        QRPic = Image.open('QRCode.png')
        QRPic.show()

    # 登录
    def login(self):
        self.QRShow()
        print("请打开学习强国APP扫描二维码登录\n")
        if (WebDriverWait(self.broswer,60, 0.5).until(lambda x: x.find_element_by_id("Cds1ok08g8ns00").is_displayed())) == True:
            print("登陆成功！\n")
        else:
            print("登录出现问题，请查看网络连接，或者二维码已失效\n")


    # 自动浏览学习强国
    def auto_browse(self):
        # 阅读文章
        num = 0
        self.broswer.get("https://www.xuexi.cn/98d5ae483720f701144e4dabf99a4a34/5957f69bffab66811b99940516ec8784.html")
        # 重要新闻栏目
        news_label = self.broswer.find_elements_by_id("Ca4gvo4bwg7400")
        for news in news_label:
            news.click()
            print(news.text)
            sleep(randint(240,300))
            num += 1
            if num == 5:
                break
        # 看当日的新闻联播
        self.broswer.get("https://www.xuexi.cn/8e35a343fca20ee32c79d67e35dfca90/7f9f27c65e84e71e1b7189b7132b4710.html?p1="+\
              datetime.datetime.now().date().strftime('%Y-%m-%d'))
        sleep(1800)
        for i in range(5, 0, -1):
            windows = self.broswer.window_handles
            self.broswer.switch_to.window(windows[i])
            self.broswer.close()
        print(datetime.datetime.now().date().strftime('%Y-%m-%d')+"的浏览任务已经完成")
        self.broswer.quit()
