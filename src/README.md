# 基于ROS组网
* 在/etc/hosts中设置IP别名,在bashrc中设置export ROS_MASTER_URI=http://***:11311

# 启动步骤
* roscore
* ssh ubuntu@***
* vncserver
* vnc端 - roslaunch usb_cam usb_cat-test.launch
* rosrun bring_up subscriber.py
---
* conda activate deeplearning
* source catkin_workspace/install/setup.bash --extend
* rosrun bring_vision publisher2.py
