import sys
import time
import signal
import cursor


class Hud:

    title = ''
    info = ''
    cols = 60

    def __init__(self, title=''):
        self.title = title

        signal.signal(signal.SIGINT, self.die)
        cursor.hide()
        self.clearall()


    def print(self, info):
        self.info = info
        self.clear()

        out = ''

        if self.title:
            out += (' +' + ('-' * (self.cols - 2)) + '+\n')
            out += self.get_line(self.title)

        out += ' +' + ('-' * (self.cols - 2)) + '+\n'
        out += self.get_lines()
        out += ' +' + ('-' * (self.cols - 2)) + '+'

        print(out)


    def sleep(self, duration=1):
        time.sleep(duration)


    def clearall(self):
        print(chr(27) + '[2j')
        print('\033c')
        print('\x1bc')
        sys.stdout.flush()


    def clear(self):
        lines = len(self.info) + 3
        if self.title:
            lines += 1

        print('\r\033[F' * lines, end='')
        sys.stdout.flush()


    def get_lines(self):
        out = ''
        for line in self.info:
            if line:
                out += self.get_line(line[0], line[1])
            else:
                out += self.get_line(' ')
        return out


    def get_line(self, key, val=None):
        if val != None:
            out = (self.pad(' | {}:'.format(key), 30) + self.pad('{}'.format(val), end='|\n'))
        else:
            out = (self.pad(' | {}'.format(key), cols=self.cols, end='|\n'))

        return out


    def pad(self, msg, cols=30, char=' ', end=''):
        msg += (char * (cols - len(msg)))
        msg += end
        return msg


    def die(self, sig=None, frame=None):
        #cursor.show()
        self.clearall()
        sys.exit(0)

