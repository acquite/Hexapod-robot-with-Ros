# 人体追踪六足机器人

### 基于ROS组网

* 在/etc/hosts中设置IP别名

* 在bashrc中设置

  > export ROS_MASTER_URI=http://liu:11311
  >
  > export ROS_HOSTNAME = liu

### 启动步骤

* PC端

  > roscore
  >
  > sudo ssh username@liu
  >
  > vncserver

* VNC端

  > roslaunch usb_cam usb_cat-test.launch
  >
  > rosrun bring_up subscriber.py
---
* PC端

  > conda activate deeplearning
  >
  > source catkin_workspace/install/setup.bash --extend
  >
  > rosrun bring_vision publisher2.py
