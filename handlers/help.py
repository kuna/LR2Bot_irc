import settings
import utils

def help(conn, msg):

        conn.send('PRIVMSG %s :Eendje IRC Help\r\n' % (msg.user))
        conn.send('PRIVMSG %s :\r\n' % (msg.user))
        conn.send('PRIVMSG %s :Admin commands:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     kick:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Kicks a player from the chatroom\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Usage: !kick [name] [reason]\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     topic:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Alters the topic of the channel\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Usage: !topic [new topic]\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     assign:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Assigns a definition to a word\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Usage: !assign [word] [definition]\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     reassign:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Alters a definition\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Usage: !reassign [word] [new definition]\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     unassign\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Removes a definition\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Usage: !unassign [word]\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     delquote:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Deletes a quote\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Usages: !delquote [numer of the quote]\r\n' % (msg.user))
        conn.send('PRIVMSG %s :\r\n' % (msg.user))
        conn.send('PRIVMSG %s :User commands:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     addquote:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :         Adds a quote\r\n' % (msg.user))
        conn.send('PRIVMSG %s :         Usage: !addquote [quote]\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     quote:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Displays a quote\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Usage: !quote [nothing|number|person|word]\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     tell:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Remembers a message and displays this when the user comes online\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Usage: !tell [receiver] [message]\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     help:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Displays this help message\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Usage: !help\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     dt:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Gives the user a dt-point\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Usage: !dt [user] [sentence]\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     dtlijst:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Displays a top 5 of dt-fouten\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Usage: !dtlijst\r\n' % (msg.user))
        conn.send('PRIVMSG %s :     oa:\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Displays an onzinalarm\r\n' % (msg.user))
        conn.send('PRIVMSG %s :          Usage: !oa\r\n' % (msg.user))