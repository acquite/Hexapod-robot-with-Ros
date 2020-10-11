#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from   std_msgs.msg import Int32

def talker():
    # ROS节点初始化
    rospy.init_node('cmd_contronl', anonymous=True)

    test_pub = rospy.Publisher('cmd_topic', Int32, queue_size=10)

    # 设置循环频率
    rate = rospy.Rate(1)

    dock = -1

    # 键盘控制 输入第一个x 走前半步, 输入第二个x 走后半步
    while not rospy.is_shutdown():
        rospy.loginfo("Please inter a cmd : ")
        vel_msg = int(input())
        # print(type(vel_msg))
        dock = -dock

        if dock == 1:
            test_pub.publish(vel_msg)
        else:
            test_pub.publish(-vel_msg)
        
        # rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass