#!/usr/bin/python2
# -*- coding: UTF-8 -*-

import time
import requests
from bs4 import BeautifulSoup
from PIL import Image
from lxml import etree

def login(username, password, oncaptcha):
    session = requests.session()

    _xsrf = BeautifulSoup(session.get('https://www.zhihu.com/#signin').content).find('input', attrs={'name': '_xsrf'})['value']
    captcha_content = session.get('http://www.zhihu.com/captcha.gif?r=%d' % (time.time() * 1000)).content
    data = {
        '_xsrf': _xsrf,
        'email': username,
        'password': password,
        'remember_me': 'true',
        'captcha': oncaptcha(captcha_content)
    }
    resp = session.post('http://www.zhihu.com/login/email', data).content
    print resp
    assert '\u767b\u9646\u6210\u529f' in resp
    return session

def kill_captcha(data):
    with open('captcha.png', 'wb') as fp:
        fp.write(data)
    image = Image.open('captcha.png')
    image.show()
    return raw_input('captcha : ')

if __name__ == '__main__':
    session = login('287429173@qq.com', '253174926', kill_captcha)
    print BeautifulSoup(session.get("https://www.zhihu.com/people/excited-vczh/followers").content).find('a', class_='name').getText()
    # print BeautifulSoup(session.get("https://www.zhihu.com/people/excited-vczh/followers").content,'lxml').select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.top > div.title-section.ellipsis > a")[0].getText()
