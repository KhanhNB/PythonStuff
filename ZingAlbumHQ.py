import sys
import unicodedata
import re
from Mp3ZingParser import Mp3ZingParser
from subprocess import call

__author__ = 'CK01'
__email__ = 'clarkkent.k41@gmail.com'


#title: ten bai hat
#performer: ten ca si the hien
#link: link thong tin ca si
#source: link download nhac voi acc free
#source_hq: link download nhac vip


def main():
    title = []
    performer = []
    link = []
    source = []
    source_hq = []
    title, performer, link, source, source_hq = Mp3ZingParser(sys.argv[1]).GetAlbumInfo()
    DownloadWithWget(title, performer, link, source, source_hq)


def DownloadWithWget(title, performer, link, source, source_hq):
    wget = ["wget", "-nd", "-np", "-c", "-r"]
    
    for i in range(len(title)):
	wget_args = []
        if(title[i] is not None):
            filename = ''
            filename = title[i]+' '+performer[i]+'.MP3'
            filename = unicodedata.normalize('NFKD', unicode(filename)).encode('ASCII', 'ignore')
            wget_args.append(source_hq[i])
            wget_args.append('-O')
            wget_args.append(filename.replace(' ', '-'))
            call(wget+wget_args)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nFile Download has been canceled")
