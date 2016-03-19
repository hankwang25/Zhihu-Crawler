#!/usr/bin/python2
# -*- coding: UTF-8 -*-

from BaseCrawler.item import CrawlItem

class PeopleItem(CrawlItem):
    """docstring for PeopleItem
    """
    def __init__(self, uid=None, soup=None):
        self.uid = uid
        if soup:
            self.name = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.top > div.title-section.ellipsis > a")[0].getText()
            self.location = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.body.clearfix > div > div > div.items > div:nth-child(1) > span.info-wrap > span.location.item > a")[0].getText()
            self.business = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.body.clearfix > div > div > div.items > div:nth-child(1) > span.info-wrap > span.business.item > a")[0].getText()
            self.employment = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.body.clearfix > div > div > div.items > div:nth-child(2) > span.info-wrap > span.employment.item > a")[0].getText()
            self.position = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.body.clearfix > div > div > div.items > div:nth-child(2) > span.info-wrap > span.position.item > a")[0].getText()
            self.education = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.body.clearfix > div > div > div.items > div:nth-child(3) > span.info-wrap > span.education.item > a")[0].getText()
            self.education_extra = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div.body.clearfix > div > div > div.items > div:nth-child(3) > span.info-wrap > span.education-extra.item > a")[0].getText()
            self.user_agree = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-operation.zg-clear > div.zm-profile-header-info-list > span.zm-profile-header-user-agree > strong")[0].getText()
            self.user_thanks = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-operation.zg-clear > div.zm-profile-header-info-list > span.zm-profile-header-user-thanks > strong")[0].getText()
            self.asks = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(2) > span")[0].getText()
            self.answers = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(3) > span")[0].getText()
            self.posts = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(4) > span")[0].getText()
            self.los = soup.select("body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.profile-navbar.clearfix > a:nth-child(6) > span")[0].getText()

    def set_followees(self, followees=[]):
        self.followees = followees
        
    def save(self):
        pass

class FolloweeItem(CrawlItem):
    """docstring for FolloweeItem
    """
    def __init__(self, soup):
        pass


class FollowerItem(CrawlItem):
    """docstring for FollowerItem
    """
    def __init__(self, author, followers):
        self.author = author
        self.followers = followers
