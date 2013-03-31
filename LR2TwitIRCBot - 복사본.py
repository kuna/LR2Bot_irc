from socket import *
import string
import sys
import threading



class connThread (threading.Thread):
    
    def __init__ (self, host, port):
        threading.Thread.__init__ (self)
        self.__running = False 

        self.__sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        self.__host = host
        self.__port = port
        self.__msg = ''

        self.start ()

    def run (self):
        self.__running = True
        self.__sock.connect ((self.__host, self.__port))

        while self.__running and self.recvMsg ():
            print self.__msg

    def close (self):
        self.__running = False
        self.__sock.close ()

    def reconnect (self):
        self.__sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.connect ((self.__host, self.__port))
        self.__running = True

    def sendMsg (self, msg, sec = 1):
        print msg
        self.__sock.send (msg + '\r\n')
        time.sleep (sec)

    def recvMsg (self):
        self.__msg = self.__sock.recv (BUFSIZE)
        return True

    def getMsg (self):
        return self.__msg

def main():
    #init socket
    myHost = 'altirc.ozinger.org'
    myPort = 80

    global sockObj, HttpObj
    global joined, registered
    joined = False
    registered = False

    sockObj = socket( )
    print myHost, myPort
    sockObj.connect( (myHost, myPort) )
    sockObj.send('USER lr2twitbot 0 0 0\r\n')
    sockObj.send('NICK rhygay\r\n')

    threading._start_new_thread(SocketThread, ())
    threading._start_new_thread(InputThread, ())

    try:
        while 1:
            pass
    except KeyboardInterrupt:
        print 'bye'

def InputThread():
    while True:
        str = raw_input(">> ")
        if (str == 'q'):
            sockObj.send('QUIT shutdown_bot')
        else:
            sockObj.send(str)
        
    sockObj.send('QUIT shutdown_bot')
    

def SocketThread():
    while True:
            data = sockObj.recv(1024)
            if not data:
                break
            
            if (joined == False and data.find('Welcome')>0):
                sockObj.send('JOIN :#zvuc')
                sockObj.send('PRIVMSG #zvuc :' + 'test')
                joined = True
                print 'Joined'
                
            temp = string.split(data, "\n")
            for line in temp:
                line = string.rstrip(line)
                line = string.split(line)
                if len(line) < 2:
                    break

                if (line[0]=='PING'):
                    sockObj.send('PONG %s\r\n' % line[1])
                if (line[0]=='MODE'):
                    joined = True
                    
            print '[IRC] ' + data


if __name__ == '__main__':
    main()
