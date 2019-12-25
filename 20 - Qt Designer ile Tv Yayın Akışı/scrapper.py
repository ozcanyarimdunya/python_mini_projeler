# coding=utf-8

import requests

from bs4 import BeautifulSoup


def get_channels():
    url = "https://www.tvyayinakisi.com/"
    html = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    channels = []
    soup_channels = soup.select('.channel-card-list.channel-card-list--page-home a')
    for i, channel in enumerate(soup_channels, start=1):
        url = channel.attrs['href']
        name = channel.select_one('.name').get_text()
        channels.append({
            'order': i,
            'name': name,
            'url': url
        })

    return channels


def get_streams(url):
    html = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    streams = []
    soup_streams = soup.select('.active ul li')
    for i, stream in enumerate(soup_streams, start=1):
        time = stream.select_one('p.time').get_text(strip=True)
        name = stream.select_one('p.name').get_text(strip=True)
        type = stream.select_one('p.type').get_text(strip=True)

        streams.append({
            "time": time,
            "name": name,
            "type": type
        })

    return streams
