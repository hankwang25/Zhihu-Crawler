#!/usr/bin/python2
# -*- coding: UTF-8 -*-

import re
import copy
import requests

from settings import HEADER

class Crawler:
    """docstring for Crawler
    """
    start_urls = []
    rules = []
        
    def start_crawl(self):
        self._compile_rules()

        start_urls = self._get_crawl_history() or self.start_urls
        for url in start_urls:
            self.process_url(url)

    def stop_crawl(self):
        pass

    def process_url(self, url):
        for rule in self._rules:
            for pattern in rule.url_pattern:
                if re.search(pattern,url):
                    if callable(rule.pre_process):
                        resp = rule.pre_process(url)
                    else:
                        resp = self.request(url)
                    if callable(rule.call_back):
                        rule.call_back(resp)
                    else:
                        self.response(resp)
        self.stop_crawl()

    def request(self, url):
        return requests.get(url,headers=HEADER)

    def response(self, response):
        pass

    def process_request(self):
        pass

    def process_response(self):
        pass

    def add_to_crawl(self):
        pass

    def _get_crawl_history(self):
        pass

    def _compile_rules(self):
        def get_method(method):
            if callable(method):
                return method
            elif isinstance(method, basestring):
                return getattr(self, method, None)

        self._rules = [copy.copy(r) for r in self.rules]
        for rule in self._rules:
            rule.call_back = get_method(rule.call_back)
            rule.pre_process = get_method(rule.pre_process)

class Rule:
    """docstring for Rule
    """
    def __init__(self, url_pattern=None, pre_process=None, call_back=None):
        self.url_pattern = url_pattern
        self.pre_process = pre_process
        self.call_back = call_back
        