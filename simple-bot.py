#more import junk. take note of the first line tho "from irc import *" irc = irc.py the file we made and included in the same directory, i could make a skitch.py and have an import from it as well. import * means import all the classes/functions in that file
from irc import *
import os
import random
 

#these are variables we define, they get passed to the function .connect() below which was defined in irc.py
channel = "#sketchdaily"
server = "irc.freenode.net"
nickname = "pyopitop"
 
irc = IRC()
irc.connect(server, channel, nickname)
 
#this is a while loop, it basically means it will repeat this loop forever, or at least until 1 is no longer 1 
while 1:
    text = irc.get_text()
    print text
 
    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send(channel, "Hello!")
