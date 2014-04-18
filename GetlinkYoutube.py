###########################################################################
# Author: CK01								                              
# Email: clarkkent.k41@gmail.com 					                      
# Github: github.com/KhanhNB						                      
# Python 2.7.x							                                  
# How to use: python GetlinkYoutube.py [link]                             
# Ex: python GetlinkYoutube.py http://www.youtube.com/watch?v=8mP5xOg7ijs 
###########################################################################

import urllib2
import json
import sys

f = urllib2.urlopen(sys.argv[1])
html1 = f.read()
output = open('links.txt', 'wb')
start = html1.find('ytplayer || {};ytplayer.config', 0, len(html1))
end = html1.find(';ytplayer.config.loaded', 0, len(html1))
start = start + 33
#print(html1[start+33])
html2 = html1[start:end]
end = html2.find('function')
end = end - 2
var_json = html2[0:end]

json_object = json.loads(var_json)
url_encoded_fmt_stream_map = json_object['args']['url_encoded_fmt_stream_map']
urls = json.dumps(url_encoded_fmt_stream_map)
qualities = urls.split(',')

for quality in qualities:
    mems = quality.split('&')
    for mem in mems:
        tmp = urllib2.unquote(mem)
        if tmp[0:3] == 'qua':
            print(tmp)
            output.write(tmp)
        elif tmp[0:3] == 'url':
            print(tmp)
            output.write(tmp)
        else:
            output.write(tmp)
        output.write('\n')
    output.write('\n\n\n')
    print('')    
output.close()
