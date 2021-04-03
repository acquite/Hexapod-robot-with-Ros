#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import Uart 


def InverseKinematics_Leg1(x,y,z,date):
    
    L1 = 60.01
    L2 = 75.81
    L3 = 143.69
    X0 = -65.505
    Y0 = 120.505
    Z0 = 0
    q0 = 0.7853981633974483

    q11 = 500+int((-q0 + math.atan((y-Y0)/(X0-x)))*750/math.pi)

    X1 = X0 - L1*math.cos(math.atan((y-Y0)/(X0-x)))
    Y1 = Y0 + L1*math.sin(math.atan((y-Y0)/(X0-x)))
    Z1 = 0

    La = math.sqrt((x-X1)**2+(y-Y1)**2+(z-Z1)**2)
    Lb = math.sqrt((x-X0)**2+(y-Y0)**2+(z-Z0)**2)

    q12 = 500+int((math.pi - math.acos((La**2+L2**2-L3**2)/(2*L2*La)) - math.acos((L1**2+La**2-Lb**2)/(2*L1*La)))*750/math.pi)
    q13 = 500-int((140/180*math.pi - math.acos((L2**2+L3**2-La**2)/(2*L2*L3)))*750/math.pi)

    date.extend(Uart.Cmd_Servo_Move(1,q11))
    date.extend(Uart.Cmd_Servo_Move(2,q12))
    date.extend(Uart.Cmd_Servo_Move(3,q13))
    #print(q11,q12,q13,'\n')
    


def InverseKinematics_Leg2(x,y,z,date):
    
    L1 = 60.01
    L2 = 75.81
    L3 = 143.69
    X0 = -116
    Y0 = 0
    Z0 = 0

    q21 = 500+int(math.atan((y-Y0)/(X0-x))*750/math.pi)

    X1 = X0 - L1*math.cos(math.atan((y-Y0)/(X0-x)))
    Y1 = Y0 + L1*math.sin(math.atan((y-Y0)/(X0-x)))
    Z1 = 0

    La = math.sqrt((x-X1)**2+(y-Y1)**2+(z-Z1)**2)
    Lb = math.sqrt((x-X0)**2+(y-Y0)**2+(z-Z0)**2)

    q22 = 500+int((math.pi - math.acos((La**2+L2**2-L3**2)/(2*L2*La)) - math.acos((L1**2+La**2-Lb**2)/(2*L1*La)))*750/math.pi)
    q23 = 500-int((140/180*math.pi - math.acos((L2**2+L3**2-La**2)/(2*L2*L3)))*750/math.pi)

    date.extend(Uart.Cmd_Servo_Move(4,q21))
    date.extend(Uart.Cmd_Servo_Move(5,q22))
    date.extend(Uart.Cmd_Servo_Move(6,q23))
    #print(q21,q22,q23,'\n')



def InverseKinematics_Leg3(x,y,z,date):
    
    L1 = 60.01
    L2 = 75.81
    L3 = 143.69
    X0 = -65.505
    Y0 = -120.505
    Z0 = 0
    q0 = 0.7853981633974483

    q31 = 500+int((q0 - math.atan((y-Y0)/(x-X0)))*750/math.pi)

    X1 = X0 - L1*math.cos(math.atan((y-Y0)/(x-X0)))
    Y1 = Y0 - L1*math.sin(math.atan((y-Y0)/(x-X0)))
    Z1 = 0

    La = math.sqrt((x-X1)**2+(y-Y1)**2+(z-Z1)**2)
    Lb = math.sqrt((x-X0)**2+(y-Y0)**2+(z-Z0)**2)

    q32 = 500+int((math.pi - math.acos((La**2+L2**2-L3**2)/(2*L2*La)) - math.acos((L1**2+La**2-Lb**2)/(2*L1*La)))*750/math.pi)
    q33 = 500-int((140/180*math.pi - math.acos((L2**2+L3**2-La**2)/(2*L2*L3)))*750/math.pi)

    date.extend(Uart.Cmd_Servo_Move(7,q31))
    date.extend(Uart.Cmd_Servo_Move(8,q32))
    date.extend(Uart.Cmd_Servo_Move(9,q33))
    #print(q31,q32,q33,'\n')
    


def InverseKinematics_Leg4(x,y,z,date):
    
    L1 = 60.01
    L2 = 75.81
    L3 = 143.69
    X0 = 65.505
    Y0 = -120.505
    Z0 = 0
    q0 = 0.7853981633974483

    q41 = 500+int((-q0 + math.atan(-(y-Y0)/(x-X0)))*750/math.pi)

    X1 = X0 + L1*math.cos(math.atan(-(y-Y0)/(x-X0)))
    Y1 = Y0 - L1*math.sin(math.atan(-(y-Y0)/(x-X0)))
    Z1 = 0

    La = math.sqrt((x-X1)**2+(y-Y1)**2+(z-Z1)**2)
    Lb = math.sqrt((x-X0)**2+(y-Y0)**2+(z-Z0)**2)

    q42 = 500+int(((math.pi - math.acos((La**2+L2**2-L3**2)/(2*L2*La)) - math.acos((L1**2+La**2-Lb**2)/(2*L1*La)))*750/math.pi))
    q43 = 500-int((140/180*math.pi - math.acos((L2**2+L3**2-La**2)/(2*L2*L3)))*750/math.pi)

    date.extend(Uart.Cmd_Servo_Move(10,q41))
    date.extend(Uart.Cmd_Servo_Move(11,q42))
    date.extend(Uart.Cmd_Servo_Move(12,q43))
    #print(q41,q42,q43,'\n')
    



def InverseKinematics_Leg5(x,y,z,date):
    
    L1 = 60.01
    L2 = 75.81
    L3 = 143.69
    X0 = 116
    Y0 = 0
    Z0 = 0

    q51 = 500+int((-math.atan((y-Y0)/(x-X0)))*750/math.pi)

    X1 = X0 + L1*math.cos(math.atan((y-Y0)/(x-X0)))
    Y1 = Y0 + L1*math.sin(math.atan((y-Y0)/(x-X0)))
    Z1 = 0

    La = math.sqrt((x-X1)**2+(y-Y1)**2+(z-Z1)**2)
    Lb = math.sqrt((x-X0)**2+(y-Y0)**2+(z-Z0)**2)

    q52 = 500+int((math.pi - math.acos((La**2+L2**2-L3**2)/(2*L2*La)) - math.acos((L1**2+La**2-Lb**2)/(2*L1*La)))*750/math.pi)
    q53 = 500-int((140/180*math.pi - math.acos((L2**2+L3**2-La**2)/(2*L2*L3)))*750/math.pi)

    date.extend(Uart.Cmd_Servo_Move(13,q51))
    date.extend(Uart.Cmd_Servo_Move(14,q52))
    date.extend(Uart.Cmd_Servo_Move(15,q53))
    #print(q51,q52,q53,'\n')
    


def InverseKinematics_Leg6(x,y,z,date):
    
    L1 = 60.01
    L2 = 75.81
    L3 = 143.69
    X0 = 65.505
    Y0 = 120.505
    Z0 = 0
    q0 = 0.7853981633974483

    q61 = 500+int((q0 - math.atan((y-Y0)/(x-X0)))*750/math.pi)

    X1 = X0 + L1*math.cos(math.atan((y-Y0)/(x-X0)))
    Y1 = Y0 + L1*math.sin(math.atan((y-Y0)/(x-X0)))
    Z1 = 0

    La = math.sqrt((x-X1)**2+(y-Y1)**2+(z-Z1)**2)
    Lb = math.sqrt((x-X0)**2+(y-Y0)**2+(z-Z0)**2)

    q62 = 500+int((math.pi - math.acos((La**2+L2**2-L3**2)/(2*L2*La)) - math.acos((L1**2+La**2-Lb**2)/(2*L1*La)))*750/math.pi)
    q63 = 500-int((140/180*math.pi - math.acos((L2**2+L3**2-La**2)/(2*L2*L3)))*750/math.pi)

    date.extend(Uart.Cmd_Servo_Move(16,q61))
    date.extend(Uart.Cmd_Servo_Move(17,q62))
    date.extend(Uart.Cmd_Servo_Move(18,q63))
    #print(q61,q62,q63,'\n')
