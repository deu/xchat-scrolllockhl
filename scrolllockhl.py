#!/usr/bin/env python

import xchat, threading, os, time

__module_name__ = 'Scroll Lock HL'
__module_version__ = '1.1'
__module_description__ = 'Highlights make the scroll lock LED blink.'

duration = 10

class BlinkingThread(threading.Thread):
    def run(self):
        for i in range(0, duration):
            os.system('xset led named "Scroll Lock"')
            time.sleep(0.5)
            os.system('xset -led named "Scroll Lock"')
            time.sleep(0.5)

def blink(word, word_eol, userdata):
    BlinkingThread().start()

xchat.hook_print('Channel Action Hilight', blink)
xchat.hook_print('Channel Msg Hilight', blink)
xchat.hook_print('Private Action to Dialog', blink)
xchat.hook_print('Private Message to Dialog', blink)
