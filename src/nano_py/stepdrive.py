#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import Uart

def InverseKinematics_Leg1(x,y,z,date):
    PI = 3.14
    L1 = 55
    L2 = 108
    L3 = 183

    X0 = 50
    Y0 = 105
    Z0 = 0

    Bias_A1 = 45
    Bias_A2 = 132.63
    Bias_A3 = 72.93

    Q11 = 500 + (int)((math.atan((y-Y0)/(x-X0)) - Bias_A1/180*PI)*750/PI)

    X1 = X0 + L1*math.cos(math.atan((y-Y0)/(x-X0)))
    Y1 = Y0 + L1*math.sin(math.atan((y-Y0)/(x-X0)))
    Z1 = Z0

    La = math.sqrt((x-X1)*(x-X1)+(y-Y1)*(y-Y1)+(z-Z1)*(z-Z1))
    Lb = math.sqrt((x-X0)*(x-X0)+(y-Y0)*(y-Y0)+(z-Z0)*(z-Z0))

    Q13 = 500 - (int)((math.acos((L2*L2+L3*L3-La*La)/(2*L2*L3)) - Bias_A3/180*PI)*750/PI)

    if (z < Z0):
        Q12 = 500 + (int)((-Bias_A2/180*PI + 2*PI - math.acos((La*La+L2*L2-L3*L3)/(2*L2*La)) - math.acos((L1*L1+La*La-Lb*Lb)/(2*L1*La)))*750/PI)
    elif (z == 0):
        Q12 = 500 + (int)((-Bias_A2/180*PI + PI - (math.acos((La*La+L2*L2-L3*L3)/(2*L2*La))))*750/PI)
    else:
        Q12 = 500 + (int)((-Bias_A2/180*PI + math.acos((L1*L1+La*La-Lb*Lb)/(2*L1*La)) - math.acos((La*La+L2*L2-L3*L3)/(2*L2*La)))*750/PI)
    #print('Leg1:')
    #print(Q11,Q12,Q13,'\n')
    
    date.extend(Uart.Cmd_Servo_Move(1,Q11))
    date.extend(Uart.Cmd_Servo_Move(2,Q12))
    date.extend(Uart.Cmd_Servo_Move(3,Q13))
    

def InverseKinematics_Leg2(x,y,z,date):
    PI = 3.14
    L1 = 55
    L2 = 108
    L3 = 183

    X0 = 95
    Y0 = 0
    Z0 = 0

    Bias_A1 = 0
    Bias_A2 = 132.63
    Bias_A3 = 72.93

    Q21 = 500 + (int)((math.atan((y-Y0)/(x-X0)) - Bias_A1/180 * PI)*750/PI)
    X1 = X0 + L1*math.cos(math.atan((y-Y0)/(x-X0)))
    Y1 = Y0 + L1*math.sin(math.atan((y-Y0)/(x-X0)))
    Z1 = Z0

    La = math.sqrt((x-X1)*(x-X1)+(y-Y1)*(y-Y1)+(z-Z1)*(z-Z1))
    Lb = math.sqrt((x-X0)*(x-X0)+(y-Y0)*(y-Y0)+(z-Z0)*(z-Z0))

    Q23 = 500 - (int)((math.acos((L2*L2+L3*L3-La*La)/(2*L2*L3)) - Bias_A3/180*PI)*750/PI)

    if (z < Z0):
        Q22 = 500 + (int)((-Bias_A2/180*PI + 2*PI - math.acos((La*La+L2*L2-L3*L3)/(2*L2*La)) - math.acos((L1*L1+La*La-Lb*Lb)/(2*L1*La)))*750/PI)
    elif (z == Z0):
        Q22 = 500 + (int)((-Bias_A2/180*PI + PI - (math.acos((La*La+L2*L2-L3*L3)/(2*L2*La))))*750/PI)
    else:
        Q22 = 500 + (int)((-Bias_A2/180*PI + math.acos((L1*L1+La*La-Lb*Lb)/(2*L1*La)) - math.acos((La*La+L2*L2-L3*L3)/(2*L2*La)))*750/PI)
    #print('Leg2:')
    #print(Q21,Q22,Q23,'\n')
    
    date.extend(Uart.Cmd_Servo_Move(4,Q21))
    date.extend(Uart.Cmd_Servo_Move(5,Q22))
    date.extend(Uart.Cmd_Servo_Move(6,Q23))
    

def InverseKinematics_Leg3(x,y,z,date):
    PI = 3.14
    L1 = 55
    L2 = 108
    L3 = 183

    X0 = 50
    Y0 = -105
    Z0 = 0

    Bias_A1 = 45
    Bias_A2 = 132.63
    Bias_A3 = 72.93

    Q31 = 500 + (int)((math.atan((y-Y0)/(x-X0)) + Bias_A1/180 * PI)*750/PI)
    X1 = X0 + L1*math.cos(math.atan((y-Y0)/(x-X0)))
    Y1 = Y0 + L1*math.sin(math.atan((y-Y0)/(x-X0)))
    Z1 = Z0

    La = math.sqrt((x-X1)*(x-X1)+(y-Y1)*(y-Y1)+(z-Z1)*(z-Z1))
    Lb = math.sqrt((x-X0)*(x-X0)+(y-Y0)*(y-Y0)+(z-Z0)*(z-Z0))

    Q33 = 500 - (int)((math.acos((L2*L2+L3*L3-La*La)/(2*L2*L3)) - Bias_A3/180*PI)*750/PI)

    if (z < Z0):
        Q32 = 500 + (int)((-Bias_A2/180*PI + 2*PI - math.acos((La*La+L2*L2-L3*L3)/(2*L2*La)) - math.acos((L1*L1+La*La-Lb*Lb)/(2*L1*La)))*750/PI)
    elif (z == Z0):
        Q32 = 500 + (int)((-Bias_A2/180*PI + PI - (math.acos((La*La+L2*L2-L3*L3)/(2*L2*La))))*750/PI)
    else:
        Q32 = 500 + (int)((-Bias_A2/180*PI + math.acos((L1*L1+La*La-Lb*Lb)/(2*L1*La)) - math.acos((La*La+L2*L2-L3*L3)/(2*L2*La)))*750/PI)
    #print('Leg3:')
    #print(Q31,Q32,Q33,'\n')
    
    date.extend(Uart.Cmd_Servo_Move(7,Q31))
    date.extend(Uart.Cmd_Servo_Move(8,Q32))
    date.extend(Uart.Cmd_Servo_Move(9,Q33))
    

def InverseKinematics_Leg4(x,y,z,date):
    PI = 3.14
    L1 = 55
    L2 = 108
    L3 = 183

    X0 = -50
    Y0 = 105
    Z0 = 0

    Bias_A1 = 45
    Bias_A2 = 132.63
    Bias_A3 = 72.93

    Q41 = 500 + (int)((math.atan((y-Y0)/(x-X0)) + Bias_A1/180 * PI)*750/PI)
    X1 = X0 - L1*math.cos(math.atan((y-Y0)/(x-X0)))
    Y1 = Y0 - L1*math.sin(math.atan((y-Y0)/(x-X0)))
    Z1 = Z0

    La = math.sqrt((x-X1)*(x-X1)+(y-Y1)*(y-Y1)+(z-Z1)*(z-Z1))
    Lb = math.sqrt((x-X0)*(x-X0)+(y-Y0)*(y-Y0)+(z-Z0)*(z-Z0))

    Q43 = 500 - (int)((math.acos((L2*L2+L3*L3-La*La)/(2*L2*L3)) - Bias_A3/180*PI)*750/PI)

    if (z < Z0):
        Q42 = 500 + (int)((-Bias_A2/180*PI + 2*PI - math.acos((La*La+L2*L2-L3*L3)/(2*L2*La)) - math.acos((L1*L1+La*La-Lb*Lb)/(2*L1*La)))*750/PI)
    elif (z == Z0):
        Q42 = 500 + (int)((-Bias_A2/180*PI + PI - (math.acos((La*La+L2*L2-L3*L3)/(2*L2*La))))*750/PI)
    else:
        Q42 = 500 + (int)((-Bias_A2/180*PI + math.acos((L1*L1+La*La-Lb*Lb)/(2*L1*La)) - math.acos((La*La+L2*L2-L3*L3)/(2*L2*La)))*750/PI)
    #print('Leg4:')
    #print(Q41,Q42,Q43,'\n')
    
    date.extend(Uart.Cmd_Servo_Move(10,Q41))
    date.extend(Uart.Cmd_Servo_Move(11,Q42))
    date.extend(Uart.Cmd_Servo_Move(12,Q43))
    

def InverseKinematics_Leg5(x,y,z,date):
    PI = 3.14
    L1 = 55
    L2 = 108
    L3 = 183

    X0 = -95
    Y0 = 0
    Z0 = 0

    Bias_A1 = 0
    Bias_A2 = 132.63
    Bias_A3 = 72.93

    Q51 = 500 + (int)((math.atan((y-Y0)/(x-X0)) + Bias_A1/180 * PI)*750/PI)

    X1 = X0 - L1*math.cos(math.atan((y-Y0)/(x-X0)))
    Y1 = Y0 - L1*math.sin(math.atan((y-Y0)/(x-X0)))
    Z1 = Z0

    La = math.sqrt((x-X1)*(x-X1)+(y-Y1)*(y-Y1)+(z-Z1)*(z-Z1))
    Lb = math.sqrt((x-X0)*(x-X0)+(y-Y0)*(y-Y0)+(z-Z0)*(z-Z0))

    Q53 = 500 - (int)((math.acos((L2*L2+L3*L3-La*La)/(2*L2*L3)) - Bias_A3/180*PI)*750/PI)

    if (z < Z0):
        Q52 = 500 + (int)((-Bias_A2/180*PI + 2*PI - math.acos((La*La+L2*L2-L3*L3)/(2*L2*La)) - math.acos((L1*L1+La*La-Lb*Lb)/(2*L1*La)))*750/PI)
    elif (z == Z0):
        Q52 = 500 + (int)((-Bias_A2/180*PI + PI - (math.acos((La*La+L2*L2-L3*L3)/(2*L2*La))))*750/PI)
    else:
        Q52 = 500 + (int)((-Bias_A2/180*PI + math.acos((L1*L1+La*La-Lb*Lb)/(2*L1*La)) - math.acos((La*La+L2*L2-L3*L3)/(2*L2*La)))*750/PI)
    #print('Leg5:')
    #print(Q51,Q52,Q53,'\n')
    
    date.extend(Uart.Cmd_Servo_Move(13,Q51))
    date.extend(Uart.Cmd_Servo_Move(14,Q52))
    date.extend(Uart.Cmd_Servo_Move(15,Q53))
    

def InverseKinematics_Leg6(x,y,z,date):
    PI = 3.14
    L1 = 55
    L2 = 108
    L3 = 183

    X0 = -50
    Y0 = -105
    Z0 = 0

    Bias_A1 = 45
    Bias_A2 = 132.63
    Bias_A3 = 72.93

    Q61 = 500 + (int)((math.atan((y-Y0)/(x-X0)) - Bias_A1/180 * PI)*750/PI)

    X1 = X0 - L1*math.cos(math.atan((y-Y0)/(x-X0)))
    Y1 = Y0 - L1*math.sin(math.atan((y-Y0)/(x-X0)))
    Z1 = Z0

    La = math.sqrt((x-X1)*(x-X1)+(y-Y1)*(y-Y1)+(z-Z1)*(z-Z1))
    Lb = math.sqrt((x-X0)*(x-X0)+(y-Y0)*(y-Y0)+(z-Z0)*(z-Z0))

    Q63 = 500 - (int)((math.acos((L2*L2+L3*L3-La*La)/(2*L2*L3)) - Bias_A3/180*PI)*750/PI)

    if (z < Z0):
        Q62 = 500 + (int)((-Bias_A2/180*PI + 2*PI - math.acos((La*La+L2*L2-L3*L3)/(2*L2*La)) - math.acos((L1*L1+La*La-Lb*Lb)/(2*L1*La)))*750/PI)
    elif (z == Z0):
        Q62 = 500 + (int)((-Bias_A2/180*PI + PI - (math.acos((La*La+L2*L2-L3*L3)/(2*L2*La))))*750/PI)
    else:
        Q62 = 500 + (int)((-Bias_A2/180*PI + math.acos((L1*L1+La*La-Lb*Lb)/(2*L1*La)) - math.acos((La*La+L2*L2-L3*L3)/(2*L2*La)))*750/PI)
    #print('Leg6:')
    #print(Q61,Q62,Q63,'\n')
    
    date.extend(Uart.Cmd_Servo_Move(16,Q61))
    date.extend(Uart.Cmd_Servo_Move(17,Q62))
    date.extend(Uart.Cmd_Servo_Move(18,Q63))
    

'''
date = bytearray(b'\x55\x55\x3B\x03\x12')
x = -200
y = -250
z = -105

InverseKinematics_Leg6(x,y,z,date)
'''
