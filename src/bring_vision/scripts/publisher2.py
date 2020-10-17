#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import sys
import rospy
import os
import threading
import time
from   std_msgs.msg    import Int32
from   cv_bridge       import CvBridge, CvBridgeError
from   sensor_msgs.msg import CompressedImage


list = [0,0,0,0,0,0,0,0]

class main_node:
    def __init__(self):
        self.image_sub     = rospy.Subscriber("/usb_cam/image_raw/compressed", CompressedImage, self.callback, queue_size=20)
        self.image_sub_2   = rospy.Subscriber("/usb_cam/image_raw/compressed", CompressedImage, self.callback_2, queue_size=20)
        self.contronl_pub  = rospy.Publisher("cmd_topic", Int32, queue_size=1)
        
        self.bridge = CvBridge()
        self.check  = 1

        tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
        self.tracker_type = tracker_types[4]

        if self.tracker_type == 'BOOSTING':
            self.tracker = cv2.TrackerBoosting_create()
        if self.tracker_type == 'MIL':
            self.tracker = cv2.TrackerMIL_create()
        if self.tracker_type == 'KCF':
            self.tracker = cv2.TrackerKCF_create()
        if self.tracker_type == 'TLD':
            self.tracker = cv2.TrackerTLD_create()
        if self.tracker_type == 'MEDIANFLOW':
            self.tracker = cv2.TrackerMedianFlow_create()
        if self.tracker_type == "CSRT":
            self.tracker = cv2.TrackerCSRT_create()
        if self.tracker_type == "MOSSE":
            self.tracker = cv2.TrackerMOSSE_create()

    def main_pub(self):
        # 设置循环频率
        rate = rospy.Rate(2/3)

        # dock = -1
        # 键盘控制 输入第一个x 走前半步, 输入第二个x 走后半步

        while not rospy.is_shutdown():
            # rospy.loginfo("Please inter a cmd : ")
            # vel_msg = input()
            # print(type(vel_msg))
            # dock = -dock
            rospy.loginfo(list[6])

            if list[4]-list[0] >= 30:   # 右
                self.contronl_pub.publish(1)
                rospy.loginfo("右")
            if list[0]-list[4] >= 30:   # 左
                self.contronl_pub.publish(-1)
                rospy.loginfo("左")
            if list[2]-list[6] >= 30:   # 前
                self.contronl_pub.publish(2)
                rospy.loginfo("前")
            if list[6]-list[2] >= 30:   # 后
                self.contronl_pub.publish(-2)
                rospy.loginfo("后")

            # 暂停1秒
            rate.sleep()

    def callback(self, data):
        while True:
            if self.check > 1:
                break
            else:
                # 使用cv_bridge将ROS的图像数据转换成Opencv的图像格式
                try:
                    # cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
                    cv_image = self.bridge.compressed_imgmsg_to_cv2(data, desired_encoding="passthrough")
                    # frame = np.array(cv_image, dtype=np.uint8)
                except CvBridgeError as e:
                    print(e)

                self.check += 1
                
                # Define an initial bounding box
                bbox = (287, 23, 86, 320)

                # Uncomment the line below to select a different bounding box
                bbox = cv2.selectROI(cv_image, False)


                list[0] = bbox[0]
                list[1] = bbox[1]
                list[2] = bbox[2]
                list[3] = bbox[3]

                # Initialize tracker with first frame and bounding box
                ok = self.tracker.init(cv_image, bbox)
                break



    def callback_2(self, data):
        try:
            # cv_image2 = self.bridge.imgmsg_to_cv2(data, "bgr8")
            cv_image2 = self.bridge.compressed_imgmsg_to_cv2(data, desired_encoding="passthrough")
            # frame = np.array(cv_image2, dtype=np.uint8)
        except CvBridgeError as e:
            print(e)

        # Start timer
        timer = cv2.getTickCount()
        # Update tracker
        ok, bbox = self.tracker.update(cv_image2)
        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

        list[4] = bbox[0]
        list[5] = bbox[1]
        list[6] = bbox[2]
        list[7] = bbox[3]

        # # Draw bounding box
        # if ok:
        #     # Tracking success
        #     p1 = (int(bbox[0]), int(bbox[1]))
        #     p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        #     cv2.rectangle(cv_image2, p1, p2, (255,0,0), 2, 1)

        # else :
        #     # Tracking failure
        #     cv2.putText(cv_image2, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

        # # Display tracker type on frame
        # cv2.putText(cv_image2, self.tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)

        # # Display FPS on frame
        # cv2.putText(cv_image2, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
        # # Display result
        # cv2.imshow("Tracking", cv_image2)

        # # Exit if ESC pressed
        # # k = cv2.waitKey(1) & 0xff
        # # if k == 27 : break
        # rospy.loginfo("callback_2")



if __name__ == '__main__':
    try:
        rospy.init_node('cmd_contronl', anonymous=True)
        # tracker_thread = trackerThread()
        # tracker_thread.start()
        # tracker_thread.join()

        a = main_node()
        a.main_pub()
        #rospy.spin()

        print("OVER!!!!!!")

        # system.os("python /home/wukong/Hexapod-robot-with-Ros/src/bring_up/scripts/tracker.py")
    except rospy.ROSInterruptException:
        pass
