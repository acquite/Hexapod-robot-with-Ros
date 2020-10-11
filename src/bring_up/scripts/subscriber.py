#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from   std_msgs.msg import Int32

# import Curve 
# import straight 
# import time 
# import Uart
# import serial



def callback(msg):
    TempS = msg.data
    rospy.loginfo(TempS)

    # rate = rospy.Rate(1)     # 休息1秒钟


    
    if TempS == 1:
        print("右")
    if TempS == -1:
        print("左")
    if TempS == 2:
        print("前")
    if TempS == -2:
        print("后")

    #     straight.straightLeg(-100,225,1000)
    # if TempS == 2:
    #     straight.straightLeg(-100,90,1000)
    # if TempS == 3:
    #     straight.straightLeg(-100,315,1000)
    # if TempS == 4:
    #     straight.straightLeg(60,180,1000)
    # if TempS == 6:
    #     straight.straightLeg(60,0,1000)
    # if TempS == 7:
    #     straight.straightLeg(100,135,1000)
    # if TempS == 8:
    #     straight.straightLeg(100,90,1000)
    # if TempS == 9:
    #     straight.straightLeg(100,45,1000)
    
    # if TempS == 5:
    #     Curve.CurveLeg(0,20,1000)

    

def pose_subscriber():
    rospy.init_node('cmd_subscribe', anonymous=True)

    # 创建一个Subscriber，订阅话题/turtle1/pose, 注册回调函数posecallback
    rospy.Subscriber('cmd_topic', Int32, callback)

    # 循环等待回调函数
    rospy.spin()

if __name__ == '__main__':
    pose_subscriber()