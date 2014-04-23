import urllib2
from HTMLParser import HTMLParser
from StringIO import StringIO
import xml.etree.ElementTree as ET
import gzip


__author__ = "CK01"
__email__ = "clarkkent.k41@gmail.com"

class Mp3ZingParser(HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.title = []
        self.source_hq = []
        self.performer = []
        self.source = []
        self.link = []
        req = urllib2.urlopen(url)
        if req.info()["Content-Encoding"] == "gzip":
            buf = StringIO(req.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read().split("\n")
        else:
            data = req.read().split("\n")
        feed_code = ''
        feed_name = ''
        for param in data:
            if (param.find('<div id="_divPlsLite') > -1):
                feed_code = feed_code + param
            if (param.find('<param name="flashvars" value=') > -1):
                feed_name = feed_name + param
        self.feed(feed_code)
        self.feed(feed_name)
    def handle_starttag(self, tag, attrs):
        xml_url = ''
        if(tag == 'div'):
            self.source_hq.append(dict(attrs)['id'].replace('_divPlsLite','http://mp3.zing.vn/download/vip/song/'))
        if(tag == 'param'):
            flashvars = dict(attrs)['value'].split('&')
            for flashvar in flashvars:
                if(flashvar.find('xmlURL') > -1):
                    xml_url = flashvar.replace('xmlURL=','')
                    break
            xml_data = urllib2.urlopen(xml_url)
            if(xml_data.info().get('Content-Encoding') == "gzip"):
                buf = StringIO( xml_data.read())
                xml_data = gzip.GzipFile(fileobj=buf)
            tree = ET.parse(xml_data)
            for name in tree.findall('./item/title'):
                tmp = name.text
                self.title.append(tmp[1:len(tmp)-1])     # xml cua zing lom
            for singer in tree.findall('./item/performer'):
                tmp = singer.text
                self.performer.append(tmp[:len(tmp)-1])  # xml cua zing lom
            for source in tree.findall('./item/source'):
                self.source.append(source.text)
            for link in tree.findall('./item/link'):
                self.link.append(link.text)
    def GetAlbumInfo(self):
        return self.title, self.performer, self.link, self.source, self.source_hq
