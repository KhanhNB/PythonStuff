###################################################################################################
# Author: CK01											                                                              
# email: clarkkent.k41@gmail.com								                                                  
# Github: github.com/KhanhNB									                                                    
# Download High Quality music from mp3.zing.vn as VIP account					                            
# How to use:											                                                                
# Run command: python ZingHQ.py [link of song]							                                      
# Ex: python ZingHQ.py http://mp3.zing.vn/bai-hat/Em-Cua-Ngay-Hom-Qua-Son-Tung-M-TP/ZW69BZOF.html 
###################################################################################################

import sys
import urllib

link = sys.argv[1]
list_strings = link.split('/')
song_name = list_strings[4]
song_name += '.MP3'
tmp = list_strings[5]
song_code = tmp.split('.')[0]
link_HQ = 'http://mp3.zing.vn/download/vip/song/'
link_HQ += song_code
print('Downloading '+song_name)
urllib.urlretrieve(link_HQ, song_name)
print('Done!')
