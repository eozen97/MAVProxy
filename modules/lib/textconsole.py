#!/usr/bin/env python

"""
  MAVProxy default console
"""
import sys

class SimpleConsole():
    '''
    a message console for MAVProxy
    '''
    def __init__(self):
        pass

    def write(self, text, fg='black', bg='white'):
        '''write to the console'''
        sys.stdout.write(text)
        sys.stdout.flush()

    def writeln(self, text, fg='black', bg='white'):
        '''write to the console with linefeed'''
        self.write(text + '\n', fg=fg, bg=bg)

    def error(self, text, fg='red', bg='white'):
        self.writeln(text, fg=fg, bg=bg)

    def close(self):
        pass

    def is_alive(self):
        '''check if we are alive'''
        return True
    
if __name__ == "__main__":
    # test the console
    import time
    console = SimpleConsole()
    while console.is_alive():
        console.write('Tick', fg='red')
        console.write(" %s " % time.asctime())
        console.writeln('tock', bg='yellow')
        time.sleep(0.5)
