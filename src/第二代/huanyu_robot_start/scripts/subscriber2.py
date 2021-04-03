#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from   std_msgs.msg import Int32

import straight 
# import platform

import Curve
import time
import Uart
import serial

def bring_robot():
    rospy.init_node("param_demo")
    rate = rospy.Rate(1)
    while(not rospy.is_shutdown()):
        #get param
        parameter1 = rospy.get_param("/int_param")  #在node下的私有变量
        # parameter2 = rospy.get_param("/param2", default=222)  #全局变量
        # print(type(parameter1))  #参数类型
        # print(type(parameter2))  #参数类型
        rospy.loginfo('Get param1 = %s', parameter1)
        # rospy.loginfo('Get param2 = %d', parameter2)

        if parameter1 == 1:
            print("前行")
            straight.straightLeg(100,90,1000)
        if parameter1 == 2:
            print("抬高")
            straight.straightLeg(60,180,1000)
        if parameter1 == 3:
            print("狭缝")
            straight.straightLeg(60,180,1000)
#     if TempS == 2:
#         print("前")
#         straight.straightLeg(100,90,1000)
#     if TempS == -2:
#         print("后")
#         straight.straightLeg(-100,90,1000)


 
        #delete param 删除
        # rospy.delete_param('/param2') 
        # #set param 设置
        # rospy.set_param('/param2',2)

        #批量获取参数
        # gain_param = rospy.get_param('gains')
        # p, i, d = gain_param['P'], gain_param['I'], gain_param['D']
        # rospy.loginfo("gains are %s, %s, %s", p, i, d)
 
        # #get all param names
        # params = rospy.get_param_names()
        # rospy.loginfo('param list: %s', params)
 
        #check param  判断是否存在
        # ifparam = rospy.has_param('/int_param')
        # if(ifparam):
        #     rospy.loginfo('/int_param exists')
        # else:
        #     rospy.loginfo('/int_param does not exist')
 

 
 
        rate.sleep()
 
if __name__=="__main__":
    bring_robot()
