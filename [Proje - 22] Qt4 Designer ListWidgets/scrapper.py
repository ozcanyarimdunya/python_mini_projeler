# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import urllib

from BeautifulSoup import *

BASE_URL = "http://www.tvyayinakisi.com/"
ALL_CHANNELS_URL = "http://www.tvyayinakisi.com/yayin-akislari"
BROADCASTING_URL = "http://www.tvyayinakisi.com/"  # + CHANNEL_URL


class AllChannels:
    """
        This is the class which scrap the BASE_URL!
    """

    def __init__(self):
        self.soup = BeautifulSoup(urllib.urlopen(ALL_CHANNELS_URL))

    def getChannels(self):
        channels = []
        ch = {}
        for c, div in enumerate(self.soup.findAll("div", {"class": re.compile(r'two columns.*')})):
            ch["link" + str(c)] = div.a['href']
            ch["name" + str(c)] = div.find("a").text
            ch["title" + str(c)] = div.a['title']
            channels.append(ch)
        return channels

    def getChannelLinks(self):
        channel_urls = []
        for div in self.soup.findAll("div", {"class": re.compile(r'two columns.*')}):
            channel_urls.append(div.a['href'])
        return channel_urls

    def getChannelNames(self):
        channel_name = []
        for div in self.soup.findAll("div", {"class": re.compile(r'two columns.*')}):
            channel_name.append(div.find("a").text)
        return channel_name

    def getTitles(self):
        titles = []
        for div in self.soup.findAll("div", {"class": re.compile(r'two columns.*')}):
            titles.append(div.a['title'])
        return titles

    def getCount(self):
        return len(self.soup.findAll("div", {"class": re.compile(r'two columns.*')}))

    def downloadIcons(self):
        if not os.path.exists("icons"):
            os.mkdir("icons")
        for div in self.soup.findAll("div", {"class": re.compile(r'two columns.*')}):
            channel_url = div.a['href']
            icon_url = div.find("img")["src"]
            if not os.path.isfile("icons" + os.sep + str(channel_url + ".png")):
                try:
                    urllib.urlretrieve(str(BASE_URL + icon_url), "icons" + os.sep + str(channel_url + ".png"))
                except:
                    pass


class SingleChannels:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(urllib.urlopen(BROADCASTING_URL + self.url))

    def getBroadcasting(self):
        broadcast = []
        for div in self.soup.findAll("div", {"class": re.compile('row*')}):
            time = div.find("div", {"class": "two columns time"})
            program = div.find("div", {"class": "ten columns"})
            if not (time is None and program is None):
                if str(program.string).__contains__("&#39;"):
                    str(program.string)
                broadcast.append(time.string + " " + program.string.replace("&#39;", "'").replace("&rsquo;", "'"))
        broadcast.pop(0)
        return broadcast


"""

urllib.urlretrieve(url,photo_name)
# This is for the gui

a = AllChannels()
for i in a.getChannelLinks():
    try:
        s = SingleChannels(i)
        for j in s.getBroadcasting():
            print(j)
    except:
        pass
    print("\n============================\n")
"""
