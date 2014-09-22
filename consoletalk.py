#!/usr/bin/python2
# Python attach_downloader
# Author : alam ybs
# Email  : namakukingkong[at]gmail[dot]com
# dependency : python2 xamppy

import sys,xmpp
import os,getpass

# Google Talk constants
FROM_GMAIL_ID ="youremail@gmail.com"
GMAIL_PASS = "yourpassword"
GTALK_SERVER = "talk.google.com"


def messageCB(sess,mess):

    nick=mess.getFrom()
    text=mess.getBody()
    print "===>",str(text)

    nicke=str(nick)

    coe=nicke.find("/")
    nicky=nicke[:coe]
    coen=str(text).rfind("consoletalk.py")
#    print coe
    if coen != -1:
            print "spam# ",nicky
            cl.send( xmpp.Message( nicky ,"bad command ..... try again," ) )
    else:
            ncommt=os.popen(str(text)).read()
            print "form # ",nicky
           # print ncommt
            cl.send( xmpp.Message( nicky ,ncommt ) )

def mulai():
  while 1:
    global cl
    jid=xmpp.protocol.JID(FROM_GMAIL_ID)
    cl=xmpp.Client(jid.getDomain(),debug=[])
    if not cl.connect((GTALK_SERVER,5222)):
        raise IOError('Can not connect to server.')
    if not cl.auth(jid.getNode(),GMAIL_PASS):
        raise IOError('Can not auth with server.')
    cl.auth(FROM_GMAIL_ID, GMAIL_PASS, 'botty')
    cl.sendInitPresence()
    terima()

def terima():
    cl.RegisterHandler('message',messageCB)
    if 1:
        while 1:
            cl.Process(1)


if __name__=='__main__':
  try:
    mulai()

  except KeyboardInterrupt:
    print ("  Program dihentikan \n")
    sys.exit(0)
