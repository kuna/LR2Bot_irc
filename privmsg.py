# -*- coding: cp949 -*-

import utils
import string
import lr2ir

class PrivMSG:
    def __init__(self, data):
        self.full, self.info, self.text, self.user, self.channel, self.char, self.cmd = utils.parse(data)
        self.res = ''
        #self.full: ���� ��ü
        #self.info: unknown
        #self.text: �޽����� �ش�
        #self.user: �޽����� ���� ������
        #self.channel: ���� ������ ä��
        #self.char: �� �� ����, Ư�� �����̸� ��ɾ� �������� ��
        #self.cmd: char �ڿ� �־����� ��ɾ�

    def procMsg(self):
        if self.text.find('exit') != -1:
            self.res = 'QUIT : bye\r\n'
        if self.text.find('lr2bot') == 0:
            self.res = 'PRIVMSG ' + self.channel + ' : ' + self.user + ', Hello :)\r\n'
