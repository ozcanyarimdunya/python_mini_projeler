# coding=utf-8

"""
Tv kanalları yayın akışı
"""
import requests

from bs4 import BeautifulSoup


def get_channels():
    """
    Get list of the page

    Args:
    """
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
    """
    Parse a list of urls.

    Args:
        url: (str): write your description
    """
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


def print_channels(channels):
    """
    Print out the channel.

    Args:
        channels: (int): write your description
    """
    for channel in channels:
        print(channel['order'], '-', channel['name'])


def print_streams(streams):
    """
    Print streams

    Args:
        streams: (todo): write your description
    """
    for stream in streams:
        print("[{}] {} {}".format(
            stream['time'], stream['type'].ljust(15), stream['name']
        ))


def main():
    """
    Main function.

    Args:
    """
    print("Select a channel\n")
    channels = get_channels()
    print_channels(channels)
    choice = int(input('>> '))
    selected = channels[choice - 1]  # index starts from 0
    streams = get_streams(selected['url'])
    print_streams(streams)


if __name__ == '__main__':
    main()
