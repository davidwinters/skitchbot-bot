#shamelessly stolen from https://pythonspot.com/en/building-an-irc-bot/

# these import statements include stuff from the "standard library" for python, just in particular socket lets us open connections
import socket
import sys
 
# this is defining a class which is a thing, this is going to be used in a different file called simple-bot.py . all of the junk below is creating functions which our other file will use
class IRC:

#this junk creates a sockect object from the socket class 
    irc = socket.socket()
 
#all python classes have this __init__ function/method thing which automatically happens when you create an instance of the class which is called an object, in this case it does some socket junk with that socket object created above, fuck if i know what it does 
    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
#this is a function that properly formats any messages our bot will send into proper IRC speak
    def send(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " " + msg + "\n")

#this prob makes sense, but it connects our bot to the server and channel specified, more on this later 
    def connect(self, server, channel, botnick):
        #defines the socket
        print "connecting to:"+server
        self.irc.connect((server, 6667))                                                         #connects to the server
        self.irc.send("USER " + botnick + " " + botnick +" " + botnick + " :This is a fun bot!\n") #user authentication
        self.irc.send("NICK " + botnick + "\n")               
        self.irc.send("JOIN " + channel + "\n")        #join the chan

#this listens to the irc chatter and spits it out to the command line, while the bot is running, everything that is said by the server or chats in the channel are spit out to the command line. There is a special case here for PING in which case the bot will respond with PONG. Must be some IRC mumbo jumbo to test if we're alive. I saw the server ping the bot shortly after it connected.  
    def get_text(self):
        text=self.irc.recv(2040)  #receive the text
 
        if text.find('PING') != -1:                      
            self.irc.send('PONG ' + text.split() [1] + 'rn') 
 
        return text
