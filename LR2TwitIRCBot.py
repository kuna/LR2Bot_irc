#!/usr/bin/python2.7
# -*- coding: cp949 -*-

import sys
import socket
import string

import utils
import settings
import privmsg
import time

#from handlers import *


def connect(HOST, PORT, NICK, IDENT, REALNAME, PASS, CHANNEL):
    print "┌------------------------LR2IR irc bot----------------------------┐"
    print "  started connection to - ", HOST, ",", PORT
    print "└-----------------------------------------------------------------┘"
    conn.connect((HOST, PORT))
    conn.send('NICK '+NICK+'\r\n')
    conn.send('USER '+IDENT+' '+HOST+' * :'+REALNAME+'\r\n')

    initialPing() # Wait for initial ping
    time.sleep(1) # Wait for registration

    conn.send('JOIN '+CHANNEL+'\r\n')
    conn.send('PRIVMSG '+CHANNEL+' : LR2Bot started!\r\n')

def sendPing(ping):
    conn.send('PONG '+ping+'\r\n')
    print 'PONG'

def initialPing():
    while True:
        data = conn.recv(4096)
        data = data.strip()
        print data
        if data.split()[0] == 'PING':
            sendPing(data.split()[1])
            print 'Initial PONG sent'
            break

modes = { 'owner': '+q', 'o': '+q',
          'deowner': '-q', 'do': '-q',
          'protected': '+p', 'protect': '+p', 'p': '+p',
          'deprotected': '-p', 'deprotect': '-p', 'dp': '-p',
          'operator': '+o', 'op': '+o',
          'deoperator': '-o', 'deop': '-o', 'dop': '-o',
          'halfop': '+ho', 'hop': '+ho', 'ho': '+ho',
          'dehalfop': '-ho', 'dho': '-ho',
          'voice': '+v', 'v': '+v',
          'devoice': '-v', 'dv': '-v',
          'ban': '+b', 'b': '+b',
          'unban': '-b', 'b': '-b',
        }

def changeMode(conn, msg):
    if utils.isadmin(conn, msg):
        cmd = msg.text.split()[0][1:]
        if len(msg.text.split()) > 1:
            wie = msg.text.split()[1]
        else:
            wie = msg.user
        conn.send('MODE %s %s %s\r\n' % (msg.channel, modes[cmd], wie))
    else:
        conn.send('PRIVMSG %s :Je moet een operator zijn om dit commando te kunnen uitvoeren.\r\n' % msg.user)


def parseMessage(data):
    msg = privmsg.PrivMSG(data)
    msg.procMsg()
    if len(msg.res) > 0:
        conn.send(msg.res)

def listen(channel, conn):
    while True:
        data = conn.recv(4096)
        print data
        if len(data) > 0:
            if data.split()[0] == 'PING':
                sendPing(data.split()[1])
            if data.find('PRIVMSG '+channel) != -1:
                parseMessage(data)
        else:
            conn.close()
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect(settings.irc_HOST, settings.irc_PORT, settings.irc_NICK, settings.irc_IDENT, settings.irc_REALNAME, settings.irc_PASS, settings.irc_CHANNEL)
            listen(settings.irc_CHANNEL)

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect(settings.irc_HOST, settings.irc_PORT, settings.irc_NICK, settings.irc_IDENT, settings.irc_REALNAME, settings.irc_PASS, settings.irc_CHANNEL)
listen(settings.irc_CHANNEL, conn)
