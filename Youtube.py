from __future__ import unicode_literals
import youtube_dl, sys, urllib.request, urllib.parse, re, os, os.path, urllib
from html.parser import HTMLParser
from urllib.request import urlopen


class Parser(HTMLParser):
    def __init__(self, url):
        self.title = None
        self.rec = False
        HTMLParser.__init__(self)
        try:
            self.feed(to_ascii(urlopen(url).read()))
        except urllib.error.HTTPError:
            return
        except urllib.error.URLError:
            return
        except ValueError:
            return

        self.rec = False
        self.error = error_callback

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.rec = True

    def handle_data(self, data):
        if self.rec:
            self.title = data

    def handle_endtag(self, tag):
        if tag == 'title':
            self.rec = False


def error_callback(*_, **__):
    pass


def is_string(data):
    return isinstance(data, str)


def is_bytes(data):
    return isinstance(data, bytes)


def to_ascii(data):
    if is_string(data):
        data = data.encode('ascii', errors='ignore')
    elif is_bytes(data):
        data = data.decode('ascii', errors='ignore')
    else:
        data = str(data).encode('ascii', errors='ignore')
    return data


def get_title(url):
    return Parser(url).title


def get_alt_loc():
    raw_loc = sys.path[0]
    global utiloc
    global alt_loc
    global loc
    utiloc = '"'
    loc = raw_loc + "/Songs" + '/' + utiloc + get_title(slink) + '.mp3' + utiloc
    alt_loc = raw_loc + "/Songs" + '/' + get_title(slink) + '.mp3'
    return alt_loc


def get_loc():
    raw_loc = sys.path[0]
    global utiloc
    global loc
    utiloc = '"'
    loc = raw_loc + "/Songs" + '/' + utiloc + get_title(slink) + '.mp3' + utiloc
    alt_loc = raw_loc + "/Songs" + '/' + get_title(slink) + '.mp3'
    return loc


def download_option():
    global utiloc
    utiloc = '"'
    download_options = {
        'format': 'bestaudio/best',
        'outtmpl': title + '.mp3',
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    return download_options


def make_directory():
    if not os.path.exists('Songs'):
            os.mkdir('Songs')
    else:
            os.chdir('Songs')


def download_song(download_options, slink):
    with youtube_dl.YoutubeDL(download_options) as dl:
                    dl.download([slink])
                    os.system("cls")


def get_titles():
    global title
    title = get_title(slink)
    return title


def get_song(song):
    global query_string
    query_string = urllib.parse.urlencode({"search_query": song})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print("http://www.youtube.com/watch?v=" + search_results[0])
    global slink
    slink = "http://www.youtube.com/watch?v=" + search_results[0]


def play_song(song):

    # Download data and config
    alt_loc = get_alt_loc()
    loc = get_loc()
    if os.path.exists(alt_loc):
        os.system("start " + loc)
        play_audio(loc)
        os.system("srp.py")
    else:
        print('')
    download_options = download_option()
    # Song Directory
    make_directory()
    # Download Songs
    download_song(download_options, slink)
    loc = get_loc()
    play_audio(loc)


def play_audio(loc):
    os.system("start " + loc)
    print("")
    print("===============================================")
    title = get_title(slink)
    print(title)
    print("===============================================")
    print("")
    input("Press enter when you have finished listening")
    os.system("cls")
    print("")
    print("")
