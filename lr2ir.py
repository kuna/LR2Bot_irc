# -*- coding: utf-8 -*-
# .encode('cp949')

import httplib2
import urllib
import Cookie
import time
import unicodedata
import BeautifulSoup

#self.player : player name
#self.level : 단위인정
#self.intro : 자기소개
#self.home : 홈페이지 주소
#self.playsongcnt : 플레이한 곡 수
#self.playcnt : 플레이한 곡 회
#self.rival[] : 라이벌들
#self.clear[] : 클리어 상황 (FULLCOMBO, HARD, NORMAL, EASY, FAILED)
#self.favoritesong[] : 자주 하는 곡
#self.recentsong[] : 최근 한 곡
#favoritesong[0] : song title
#favoritesong[1] : clear guage
#favoritesong[2] : play count
#favoritesong[3] : ranking
#favoritesong[4] : link

# using getPlayInfo -
#self.guage
#self.rank
#self.score
#self.combo
#self.bp
#self.pg
#self.gr
#self.gd
#...


class LR2IR:
    def __init__(self, userid):
        self.url = "http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=mypage&playerid=" + userid
        self.player = ''
        self.level = ''
        self.intro = ''
        self.home = ''
        self.playsongcnt = ''
        self.playcnt = ''
        self.rival = []
        self.clear = []
        self.favoritesong = []
        self.recentsong = []

    def checkUrl(self, url):
        if (url.find('http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=mypage&playerid=') != -1):
            self.url = url
            return True
        elif:
            return False

        
    def doParsing(self):
        r = self.getHttpContents(self.url)
        table = r.findAll('table')
        if table is None:
            return
        self.profile_parsing(table[0])
        self.clear_parsing(table[1])
        self.favorite_parsing(table[2])
        self.recent_parsing(table[3])
    def profile_parsing(self, t):
        rows = t.findAll('tr')
        for row in rows:
            name = row.findAll('th')[0].text
            data = row.findAll('td')[0].text
            if (name == u'プレイヤー名'):
                self.player = data
            if (name == u'段位認定'):
                self.level = data
            if (name == u'自己紹介'):
                self.intro = data
            if (name == u'ホームページ'):
                self.home = data
            if (name == u'プレイした曲数'):
                self.playsongcnt = data
            if (name == u'ライバル'):
                self.rival = []
                links = row.findAll('a')
                for link in links:
                    self.rival.append(link.text)

    def clear_parsing(self, t):
        rows = t.findAll('tr')
        cells = rows[1].findAll('td')
        self.clear = []
        for cell in cells:
            self.clear.append(cell.text)

    def favorite_parsing(self, t):
        rows = t.findAll('tr')
        self.favoritesong = []
        i=0
        print 'FAVORITE PARSING START'
        for row in rows:
            i = i+1
            if (i<=1):
                continue
            cells = row.findAll('td')
            celldata = []
            celldata.append(cells[1].text)      # song title
            celldata.append(cells[2].text)      # clear guage
            celldata.append(cells[3].text)      # play count
            celldata.append(cells[4].text)      # ranking
            celldata.append(cells[1].find('a')['href']) # page addr
            
            self.favoritesong.append(celldata)
            print celldata

    def recent_parsing(self, t):
        rows = t.findAll('tr')
        self.recentsong = []
        i=0
        print 'RECENT PARSING START'
        for row in rows:
            i = i+1
            if (i<=1):
                continue
            cells = row.findAll('td')
            celldata = []
            celldata.append(cells[1].text)      # song title
            celldata.append(cells[2].text)      # clear guage
            celldata.append(cells[3].text)      # play count
            celldata.append(cells[4].text)      # ranking
            celldata.append(cells[1].find('a')['href']) # page addr
            
            self.recentsong.append(celldata)
            print celldata

    def getPlayInfo(self, url, rank):
        self.guage = ''
        self.rank = ''
        self.score = ''
        self.combo = ''
        self.bp = ''
        self.pg = ''
        self.gr = ''
        self.gd = ''
        self.bd = ''
        self.pr = ''

        name = self.player
        nrank = rank.split('/')
        page = int(nrank[0])/100+1
        newurl = 'http://www.dream-pro.info/~lavalse/LR2IR/' + url + '&page=' + str(page)
        r = self.getHttpContents(newurl)
        tables = r.findAll('table')
        rows = tables[3].findAll('tr')
        i=0
        for row in rows:
            i = i+1
            if (i%2 == 1):
                continue
            cells = row.findAll('td')
            if (cells[1].text == name):
                self.guage = cells[3].text
                self.rank = cells[4].text
                self.score = cells[5].text
                self.combo = cells[6].text
                self.bp = cells[7].text
                self.pg = cells[8].text
                self.gr = cells[9].text
                self.gd = cells[10].text
                self.bd = cells[11].text
                self.pr = cells[12].text
                break
            
    def getHttpContents(self, targeturl):
        try:
            http = httplib2.Http()
            res, c = http.request(targeturl);
            if 'err' in res['content-location'] or 'REDIRECT' in res['content-location']:
                print 'LR2IR Error: Error url loading'
                return None
            return BeautifulSoup.BeautifulSoup(c)
        except Exception, e:
            print ('LR2IR unexpected error: %s'%(e))


# search or see info
# sear
class LR2IRInfo:
    def __init__(self):
        self.userid = []
        self.username = []
        self.userlevel = []
        self.userpage = []
        
        self.songname = []
        self.songclear = []
        self.songurl = []

    # only song page
    def checkUrl(self, url):
        if (url.find('http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=ranking&bmsid=') != -1):
            return True
        elif:
            return False
        
    def searchUser(self, username):
        url = 'http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=search&sort=bmsid_desc&exec=%8C%9F%8D%F5&type=player&keyword=' + username
        r = self.getHttpContents(url)
        table = r.find('table')
        rows = table.findAll('tr')
        self.userid = []
        self.username = []
        self.userlevel = []
        self.userpage = []
        
        i=0
        for row in rows:
            i = i+1
            if (i <= 1) continue
            cells = row.findAll('td')
            self.userid.append(cells[0].text)
            self.username.append(cells[1].text)
            self.userlevel.append( cells[2].text + ' / ' + cells[3].text)
            self.userpage.append(cells[1].find('a')['href'])

    def searchSong(self, songname):
        url = 'http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=search&mode=search&sort=playcount_desc&keyword=' + songname
        r = self.getHttpContents(url)
        table = r.find('table')
        rows = table.findAll('tr')
        self.songname = []
        self.songclear = []
        self.songurl = []
        
        i=0
        for row in rows:
            i = i+1
            if (i <= 1) continue
            cells = row.findAll('td')
            self.songname.append(cells[1].text)
            self.songclear.append(cells[3].text + ' / ' + cells[4].text)
            self.songurl.append(cells[1].find('a')['href'])

    def parseSong(self, url):
        r = self.getHttpContents(url)
        self.songgenre = r.find('h4').text
        self.songtitle = r.find('h1').text
        self.songartist = r.find('h2').text
        tables = r.findAll('table')
        rows = tables[0].findAll('tr')
        for row in rows:
            t = row.find('th').text
            if (t == u'BPM'):
                self.songbpm = row.findAll('td')[0].text
                self.songlevel = row.findAll('td')[1].text
                self.songkey = row.findAll('td')[2].text
                self.songjudge = row.findAll('td')[3].text
            if (t == u'本体URL'):
                self.songurl = row.find('td').text
            if (t == u'差分URL'):
                self.songsabunurl = row.find('td').text

        self.songplaystatus = []
        rows = tables[1].findAll('td')
        for row in rows:
            self.songplaystatus.append(row.text)

        
    def getHttpContents(self, targeturl):
        try:
            http = httplib2.Http()
            res, c = http.request(targeturl);
            if 'err' in res['content-location'] or 'REDIRECT' in res['content-location']:
                print 'LR2IR Error: Error url loading'
                return None
            return BeautifulSoup.BeautifulSoup(c)
        except Exception, e:
            print ('LR2IR unexpected error: %s'%(e))
    

