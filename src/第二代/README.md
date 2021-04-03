# 激光雷达hector建图 + Astra rtabmap三维建图 + 激光雷达避障



### 启动激光雷达建图

>*  roslaunch rplidar_ros view_slam.launch

### 启动激光数据采集

> * rosrun hibot_follower hibot_follower_node 

### 启动避障功能

> * rosrun huanyu_robot_start subscriber2.py 

---



### 启动TF等初始化节点

> * roslaunch huanyu_robot_start Huanyu_robot_start.launch

### 启动Astra深度摄像头

> * roslaunch huanyu_robot_start astra_rgb_ir_depth.launch

### 启动rtabmap建图节点

> * roslaunch rtabmap_ros rtabmap.launch

---



