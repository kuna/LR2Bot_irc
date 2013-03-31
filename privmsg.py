# -*- coding: cp949 -*-

import utils
import string
import lr2ir

class PrivMSG:
    def __init__(self, data):
        self.full, self.info, self.text, self.user, self.channel, self.char, self.cmd = utils.parse(data)
        self.res = ''
        #self.full: 본문 전체
        #self.info: unknown
        #self.text: 메시지만 해당
        #self.user: 메시지를 보낸 유저명
        #self.channel: 현재 접속한 채널
        #self.char: 맨 앞 글자, 특정 글자이면 명령어 실행으로 앎
        #self.cmd: char 뒤에 주어지는 명령어

    def procMsg(self):
        if self.text.find('exit') != -1:
            self.res = 'QUIT : bye\r\n'
        if self.text.find('lr2bot') == 0:
            self.res = 'PRIVMSG ' + self.channel + ' : ' + self.user + ', Hello :)\r\n'
