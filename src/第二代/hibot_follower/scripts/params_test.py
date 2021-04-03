#!/usr/bin/env python
# coding:utf-8
import rospy
 
def param_demo():
    rospy.init_node("params_test")
    rate = rospy.Rate(1)
    while(not rospy.is_shutdown()):
        #get param
        '''parameter1 = rospy.get_param("~param1")  #在node下的私有变量
        parameter2 = rospy.get_param("/param2", default=222)  #全局变量
        print(type(parameter1))  #参数类型
        print(type(parameter2))  #参数类型
        rospy.loginfo('Get param1 = %s', parameter1)
        rospy.loginfo('Get param2 = %d', parameter2)
 
        #delete param 删除
        rospy.delete_param('/param2')''' 
        #set param 设置
        rospy.set_param('~param4',4)
 
        #check param  判断是否存在
        '''ifparam3 = rospy.has_param('/param3')
        if(ifparam3):
            rospy.loginfo('/param3 exists')
        else:
            rospy.loginfo('/param3 does not exist')
 '''
        #批量获取参数
        '''gain_param = rospy.get_param('gains')
        p, i, d = gain_param['P'], gain_param['I'], gain_param['D']
        rospy.loginfo("gains are %s, %s, %s", p, i, d)
 '''
        #get all param names
        params = rospy.get_param_names()
        rospy.loginfo('param list: %s', params)
 
 
        rate.sleep()
 
if __name__=="__main__":
    param_demo()

