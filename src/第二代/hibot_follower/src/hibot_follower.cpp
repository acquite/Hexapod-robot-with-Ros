#include "ros/ros.h"
#include <sensor_msgs/LaserScan.h>
#include <geometry_msgs/Twist.h>
#include <string.h>
#include <string> 

using namespace std;

float x_pillar;
float y_pillar;
float alpha_pillar;	
float smallest_distance = 1000;	
// string smoother_cmd_vel;
float scale_linear_X, scale_angular_Z;
int  num, int_param;
bool case1;
// geometry_msgs::Twist vel_msg_;
// ros::Publisher cmd_vel_pub;

void laserScancallback(const sensor_msgs::LaserScan::ConstPtr& scan)
{
	//用arr_size接收激光雷达扫描一次的激光点数（(最大角度-最小角度)/单位角度 = 激光点的个数）
	int arr_size = floor((scan->angle_max-scan->angle_min)/scan->angle_increment);
	for(int i=0;i< arr_size;i++)
	{
		if (scan->ranges[i] < 0.15) 	//滤除雷达的最小值
		{
			continue;
		}
		if(scan->ranges[i]<smallest_distance)
		{
			smallest_distance = scan->ranges[i];	//for语句来找到扫描一次后离机器人最近的直线距离的点
			alpha_pillar = (scan->angle_min + i*scan->angle_increment);		//并计算出角弧度    
	
		}
	}
	//通过得到的直线距离点，再通过三角函数公式，算出物体在以机器人为原点的X轴和Y轴的偏移量
	x_pillar = -smallest_distance*cos(alpha_pillar);		
	y_pillar = smallest_distance*sin(alpha_pillar);
	
	ROS_INFO("[min, angle, x, y]=[%lf, %lf, %lf, %lf]",smallest_distance, alpha_pillar, x_pillar, y_pillar);
	
	// if((x_pillar > Min_follower_Distence) && (x_pillar < Max_follower_Distence))
	// {
	// 	vel_msg_.linear.x = x_pillar * scale_linear_X;
	// 	vel_msg_.angular.z = -(y_pillar * scale_angular_Z);
	// }
	// else if ((x_pillar < Min_follower_Distence) && (x_pillar > 0))
	// {
	// 	vel_msg_.linear.x = -x_pillar * scale_linear_X;
	// 	vel_msg_.angular.z = -(y_pillar * scale_angular_Z);
	// }
	// else
	// {
	// 	vel_msg_.linear.x  = 0;
	// 	vel_msg_.angular.z = 0;
	// }

	if (smallest_distance <= 0.4)
	{
		if(alpha_pillar <= 0.3 & alpha_pillar >= -0.3)
                {
                        ros::param::set("int_param",2);  //身体抬高
                }
                else
		{
		        ros::param::set("int_param",3);  //狭缝
                }
		// ROS_INFO("[min, angle, x, y]=[%lf, %lf, %lf, %lf]",smallest_distance, alpha_pillar, x_pillar, y_pillar);
		// printf("int_param:  %d\n\n", num);

		// bool case1 = ros::param::get("int_param", int_param);
		// ROS_INFO("int_param=%d",int_param);
	}

	if (smallest_distance >= 0.45)
        {
                ros::param::set("int_param",1);
                // ROS_INFO("[min, angle, x, y]=[%lf, %lf, %lf, %lf]",smallest_distance, alpha_pillar, x_pillar, y_pillar);
                // printf("int_param:  %d\n\n", num);

                //bool case1 = ros::param::get("int_param", int_param);
                //ROS_INFO("GGGG int_param=%d",int_param);
        }
	
	
	// cmd_vel_pub.publish(vel_msg_);
	smallest_distance = 1000;
}

int main(int argc, char** argv)
{
	ros::init(argc,argv,"hibot_follower");

	ros::NodeHandle n;
	ros::NodeHandle nh_private("~");
//	ros::Rate loop_rate(0.25);
    //string s;
    //int num;

    //n.param<string>("string_param", s, "default_string");
        n.param<int>("int_param", num, 1);
	n.setParam("int_param", 1);
	
	// nh_private.param<std::string>("smoother_cmd_vel", smoother_cmd_vel, "/smoother_cmd_vel"); 
	nh_private.param<float>("scale_linear_X", scale_linear_X, 0.2); 
	nh_private.param<float>("scale_angular_Z", scale_angular_Z, 2.7); 
	// nh_private.param<float>("Min_follower_Distence", Min_follower_Distence, 0.5); 
	// nh_private.param<float>("Max_follower_Distence", Max_follower_Distence, 2.0); 

	ros::Subscriber sub = n.subscribe("/scan",1000,laserScancallback);
        // cmd_vel_pub = n.advertise<geometry_msgs::Twist>(smoother_cmd_vel,1000);
        // ros::spin();
        while(1)
        {
                ros::spinOnce();
                bool case1 = ros::param::get("int_param", int_param);
                if (int_param == 2 || int_param == 3)
                {
                        ros::Duration(7).sleep();
                        //loop_rate.sleep();
                }

        }
}



