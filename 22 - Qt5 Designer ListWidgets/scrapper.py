import os

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
        logo = channel.select_one('.logo img').attrs['src']
        channels.append({
            'order': i,
            'name': name,
            'url': url,
            'logo': saved_logo_path(name, logo),
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


def saved_logo_path(name, url):
    icon_dir = 'icons'
    icon_path = os.path.join(icon_dir, name + '.png')

    if os.path.exists(icon_path):
        return icon_path

    if not os.path.isdir(icon_dir):
        os.mkdir(icon_dir)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(icon_path, 'wb') as fp:
            for chunk in response:
                fp.write(chunk)
        return icon_path
