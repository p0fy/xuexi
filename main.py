# coding=utf-8

"""
    __author__ : shachuan
    Issue Date : 2019.2.11
    Description :自动登录学习强国，可以自动浏览文章、观看视频、收藏分享等功能
    History :
    Version : 1.0
"""


from xuexi import xxqg

#from selenium.webdriver.chrome.options import Options

'''
chrome_options=Options()
chrome_options.add_argument('--headless')
broswer = webdriver.Chrome(options=chrome_options)
'''


if __name__ == '__main__':
    study = xxqg()
    while(True):
        active_flag = study.active_detect()
        if active_flag:
            study.login()
            study.auto_browse()
        else:
            print('还不到活跃Buff加成时间，再等一会^.^')