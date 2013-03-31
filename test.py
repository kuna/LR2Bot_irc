#this file is for module testing

import lr2ir

def loadLR2IR():
    l = lr2ir.LR2IR('31478')
    print 'INITED'
    l.doParsing()
    print '------------PARSED-------------'

    print 'lets see rank of: ', l.recentsong[0][4], ", ", l.recentsong[0][3]
    l.getPlayInfo(l.recentsong[0][4], l.recentsong[0][3])

    print l.rank
    print l.combo


print '---EXECUTED---'
loadLR2IR()
