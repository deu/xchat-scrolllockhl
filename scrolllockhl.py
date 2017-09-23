#!/usr/bin/env python

import xchat, threading, os, time

__module_name__ = 'Scroll Lock HL'
__module_version__ = '1.2'
__module_description__ = 'Highlights make the scroll lock LED blink.'

NUMBLINKS = 10
INTERVAL = 0.5

alreadyBlinking = False

class BlinkingThread(threading.Thread):
    def run(self):
        global alreadyBlinking
        if not alreadyBlinking:
            alreadyBlinking = True
            for i in range(0, NUMBLINKS):
                os.system('xset led named "Scroll Lock"')
                time.sleep(INTERVAL)
                os.system('xset -led named "Scroll Lock"')
                time.sleep(INTERVAL)
            alreadyBlinking = False

def blink(word, word_eol, userdata):
    BlinkingThread().start()

xchat.hook_print('Channel Action Hilight', blink)
xchat.hook_print('Channel Msg Hilight', blink)
xchat.hook_print('Private Action to Dialog', blink)
xchat.hook_print('Private Message to Dialog', blink)
