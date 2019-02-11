# coding=utf-8

"""
    __author__ : shachuan
    Issue Date : 2019.2.11
    Description :自动登录学习强国，可以自动浏览文章、观看视频、收藏分享等功能
    History :
    Version : 1.0
"""


import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

broswer = webdriver.Chrome()
login_url = "https://pc.xuexi.cn/points/login.html?ref=https://www.xuexi.cn/"

if __name__ == '__main__':
    broswer.get(login_url)
    broswer.maximize_window()
    broswer.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("请扫描二维码登录\n")
    if (WebDriverWait(broswer, 20, 0.5).until(lambda x: x.find_element_by_id("Cds1ok08g8ns00").is_displayed())) == True:
        print("登陆成功！\n")
    broswer.get("https://www.xuexi.cn/98d5ae483720f701144e4dabf99a4a34/5957f69bffab66811b99940516ec8784.html")
    label = broswer.find_elements_by_class_name("word-item")
    for news in label:
        news.click()
        print("打开文章")