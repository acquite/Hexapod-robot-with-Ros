#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import sys
import rospy
import os
import threading
import time
from   std_msgs.msg    import Int32
from   cv_bridge       import CvBridge, CvBridgeError
from   sensor_msgs.msg import Image


list = [0,0,0,0,0,0,0,0]

class main_node:
    def __init__(self):
        self.image_sub     = rospy.Subscriber("/usb_cam/image_raw", Image, self.callback)
        self.contronl_pub  = rospy.Publisher("cmd_topic", Int32, queue_size=10)
        
        self.bridge = CvBridge()

    def main_pub(self):
        # 设置循环频率
        rate = rospy.Rate(1)

        # dock = -1
        # 键盘控制 输入第一个x 走前半步, 输入第二个x 走后半步

        while not rospy.is_shutdown():
            # rospy.loginfo("Please inter a cmd : ")
            # vel_msg = input()
            # print(type(vel_msg))
            # dock = -dock
            rospy.loginfo(list[4])

            if list[4]-list[0] >= 10:   # 右
                test_pub.publish(1)
            if list[0]-list[4] >= 10:   # 左
                test_pub.publish(-1)
            if list[2]-list[6] >= 10:   # 前
                test_pub.publish(2)
            if list[6]-list[2] >= 10:   # 后
                test_pub.publish(-2)

            # 暂停1秒
            rate.sleep()

    def callback(self, data):
        # 使用cv_bridge将ROS的图像数据转换成Opencv的图像格式
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
        tracker_type = tracker_types[4]

        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == "CSRT":
            tracker = cv2.TrackerCSRT_create()
        if tracker_type == "MOSSE":
            tracker = cv2.TrackerMOSSE_create()
        # # Read video
        # video = cv2.VideoCapture(0)


        # Exit if video not opened.
        # if not cv_image.isOpened():
        #     print("Could not open video")
        #     sys.exit()

        # Read first frame.
        ok, frame = cv_image.read()
        if not ok:
            print('Cannot read video file')
            sys.exit()

        # Define an initial bounding box
        bbox = (287, 23, 86, 320)

        # Uncomment the line below to select a different bounding box
        bbox = cv2.selectROI(frame, False)


        list[0] = bbox[0]
        list[1] = bbox[1]
        list[2] = bbox[2]
        list[3] = bbox[3]

        # Initialize tracker with first frame and bounding box
        ok = tracker.init(frame, bbox)

        while True:
            # Read a new frame
            ok, frame = cv_image.read()
            if not ok:
                break
            # Start timer
            timer = cv2.getTickCount()
            # Update tracker
            ok, bbox = tracker.update(frame)
            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

            list[4] = bbox[0]
            list[5] = bbox[1]
            list[6] = bbox[2]
            list[7] = bbox[3]

            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)

            else :
                # Tracking failure
                cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

            # Display tracker type on frame
            cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

            # Display FPS on frame
            cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
            # Display result
            cv2.imshow("Tracking", frame)

            # Exit if ESC pressed
            k = cv2.waitKey(1) & 0xff
            if k == 27 : break



if __name__ == '__main__':
    try:
        rospy.init_node('cmd_contronl', anonymous=True)
        # tracker_thread = trackerThread()

        # tracker_thread.start()
        
        a = main_node()
        
        a.main_pub()
        rospy.spinOnce()

        # tracker_thread.join()

        print("OVER!!!!!!")

        # system.os("python /home/wukong/Hexapod-robot-with-Ros/src/bring_up/scripts/tracker.py")
    except rospy.ROSInterruptException:
        pass




 
    