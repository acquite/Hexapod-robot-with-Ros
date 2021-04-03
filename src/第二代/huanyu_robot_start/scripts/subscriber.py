#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from   std_msgs.msg import Int32

import straight 
import platform



def callback(msg):
    TempS = msg.data
    rospy.loginfo(TempS)

    rate = rospy.Rate(3)     # 休息1秒钟
    rate.sleep()


    
    #if TempS == 1:
        #print("右")
        #straight.straightLeg(60,0,1000)
    #if TempS == -1:
        #print("左")
        #straight.straightLeg(60,180,1000)
    if TempS == 2:
        print("前")
        straight.straightLeg(100,90,1000)
    if TempS == -2:
        print("后")
        straight.straightLeg(-100,90,1000)
    

def pose_subscriber():
    rospy.init_node('cmd_subscribe', anonymous=True)

    # 创建一个Subscriber，订阅话题/turtle1/pose, 注册回调函数posecallback
    rospy.Subscriber('cmd_topic', Int32, callback, queue_size=1)

    # 循环等待回调函数
    rospy.spin()

if __name__ == '__main__':
    pose_subscriber()
