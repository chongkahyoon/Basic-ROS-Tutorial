#!/usr/bin/env python
import rospy, os, sys
from sound_play.msg import SoundRequest

from sound_play.libsoundplay import SoundClient

def sleep(t):
    try:
        rospy.sleep(t)
    except:
        pass

if __name__ == '__main__':
    rospy.init_node('soundplay_test_node', anonymous= True)
    soundhandle = SoundClient()

    rospy.sleep(1)

    soundhandle.stopAll()
    
    print 'say'
    soundhandle.say('Hello world!')
    sleep(3)

