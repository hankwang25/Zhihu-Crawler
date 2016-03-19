#!/usr/bin/python2
# -*- coding: UTF-8 -*-

import pickle
import re
from bs4 import BeautifulSoup

from BaseCrawler.crawl import Crawler, Rule
from login import login, kill_captcha
from zhihu_item import PeopleItem


class ZhihuCrawl(Crawler):
    """docstring for ZhihuCrawl
    """
    # start_urls = ["https://www.zhihu.com/people/excited-vczh/followees",]
    # rules = [Rule(url_pattern=['people/[^/]+/followees'],pre_process='use_session',call_back="parse_item")]
    # start_urls = ["https://book.douban.com/",]
    # rules = [Rule(url_pattern=['douban.com'],call_back="parse_item")]

    def __init__(self):
        # try:
        #     self.session = pickle.load(open("session", "rt"))
        # except:
        #     self.session = self.init_session()
        pass

    def init_session(self):
        self.session = login('287429173@qq.com', '253174926', kill_captcha)

    def use_session(self, url):
        return self.session.get(url)

    def parse_item(self, response):
        print dir(response)
        if response.status_code != 200: 
            self.init_session()
            return

        soup = BeautifulSoup(response.content,'lxml')
        uid = self.parse_uid(response.url)
        people = PeopleItem(uid=uid,soup=soup)

        followees = []
        for div in soup.select('#zh-profile-follows-list > div'):
            other_uid = self.parse_uid(div.a['href'])
            other_href = 'www.zhihu.com' + div.a['href'] + '/followees'
            followees.append(other_uid)
            self.add_to_crawl(other_href)

        people.set_followees(followees)
        people.save()

        self.get_more_followees()

    def get_more_followees(self):
        pass

    def parse_uid(self, url):
        return url.split('/people/')[-1].split('/followees')[0]

    def stop_crawl(self):
        # pickle.dump(self.session,open('session','wt'))
        pass


if __name__ == '__main__':
    zhihu = ZhihuCrawl()
    zhihu.start_crawl()
