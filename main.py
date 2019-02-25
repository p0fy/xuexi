# coding=utf-8

"""
    __author__ : shachuan
    Issue Date : 2019.2.11
    Description :自动登录学习强国，可以自动浏览文章、观看视频、收藏分享等功能
    History :
    Version : 1.0
"""


from xuexi import xxqg
from time import sleep




if __name__ == '__main__':
    study = xxqg()
    study.login()
    """
    while(True):
        try:
            active_flag = study.active_detect()
            if active_flag:
                study.login()
                #study.auto_browse()
            else:
                print('还不到活跃Buff加成时间，再等一会^.^')
                study.broswer.get("https://www.xuexi.cn/")
                sleep(300)
        except Exception:
            continue
        continue
    """