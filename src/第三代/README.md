# Realsense D435i rtabmap建图

### 启动相机节点

> * roslaunch realsense2_camera rs_rgbd.launch

### 启动建图节点

> * roslaunch rtabmap_ros rtabmap.launch rtabmap_args:="--delete_db_on_start"