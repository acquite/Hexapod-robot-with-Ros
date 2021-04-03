#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Globle_Pos as GP
import stepdrive as IK
import math
import serial
import Uart
import ccc
import time

import RPi.GPIO as GPIO

PI = 3.14
H = 60

#X_Index = [0, 0.025, 0.025, 0.025, 0.05, 0.075, 0.3, 0.3, 0.075, 0.05, 0.025, 0.025, 0.025]
#Y_Index = [0, 0.025, 0.025, 0.025, 0.05, 0.075, 0.3, 0.3, 0.075, 0.05, 0.025, 0.025, 0.025]
#Z_Index = [0, 0.25,  0.25,  0.25,  0.15, 0.05,  0,   0,   -0.05, -0.15,-0.25, -0.25, -0.25]
X_Index = [0,0.05,0.05,0.05,0.05,  0.2,0.2,  0.040,  0.038,  0.036,  0.034,  0.032,  0.030,  0.028,  0.026,  0.024,  0.022,  0.020,  0.018,  0.016,  0.014,  0.012,  0.010]
Y_Index = [0,0.05,0.05,0.05,0.05,  0.2,0.2,  0.040,  0.038,  0.036,  0.034,  0.032,  0.030,  0.028,  0.026,  0.024,  0.022,  0.020,  0.018,  0.016,  0.014,  0.012,  0.010]
Z_Index = [0,0.4, 0.32,0.24,0.04,  0,  0,   -0.060 ,-0.061, -0.062 ,-0.0625,-0.0625,-0.0625,-0.0625,-0.0625,-0.0625,-0.0625,-0.0625,-0.0625,-0.0625,-0.063, -0.064, -0.065]
'''
X_Index = [0, 0.025, 0.025,0.025,0.05,0.075,0.15,0.1,0.05 ,   0.075,0.035,0.04,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.05]
Y_Index = [0, 0.025, 0.025,0.025,0.05,0.075,0.15,0.1,0.05  ,  0.075,0.035,0.04,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.06,0.05]
Z_Index = [0,0.05  , 0.1, 0.15,  0.15 ,0.6,0.3,0.25,0.15,   -0.25,-0.15,-0.15, -0.05,-0.03,-0.03,-0.03,-0.03,-0.03,-0.03,-0.03,-0.03,-0.03,-0.03]
'''
#channel = [11,12,13,15,16,18]
channels = [11,12,13,15,16,18]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channels, GPIO.IN)

#GPIO.setup(channel, GPIO.IN)

def Read_GPIO(channel):
    if GPIO.input(channel):
        s = 0
    else:
        s = 1
    return s



def Robot_Init():

    date = bytearray(b'\x55\x55\x3B\x03\x12')
    date.extend(Uart.AddTime(65))
    IK.InverseKinematics_Leg1(GP.Leg1_Pos[0],GP.Leg1_Pos[1],GP.Leg1_Pos[2],date)
    IK.InverseKinematics_Leg2(GP.Leg2_Pos[0],GP.Leg2_Pos[1],GP.Leg2_Pos[2],date)
    IK.InverseKinematics_Leg3(GP.Leg3_Pos[0],GP.Leg3_Pos[1],GP.Leg3_Pos[2],date)
    IK.InverseKinematics_Leg4(GP.Leg4_Pos[0],GP.Leg4_Pos[1],GP.Leg4_Pos[2],date)
    IK.InverseKinematics_Leg5(GP.Leg5_Pos[0],GP.Leg5_Pos[1],GP.Leg5_Pos[2],date)
    IK.InverseKinematics_Leg6(GP.Leg6_Pos[0],GP.Leg6_Pos[1],GP.Leg6_Pos[2],date)
    Uart.SendDate(date)
    time.sleep(0.5)


def Swing_Leg1(L,A):
    angle = A/180*PI

    for i in range(0,23):
        #date = bytearray(b'\x55\x55\x0E\x03\x03')
        #date.extend(Uart.AddTime(65))
        x = GP.Leg1_Pos[0] + L*math.cos(angle)*X_Index[i]
        y = GP.Leg1_Pos[1] + L*math.sin(angle)*Y_Index[i]
        z = GP.Leg1_Pos[2] + H*Z_Index[i]
        #print(GP.Leg4_Pos[0],GP.Leg4_Pos[1],GP.Leg4_Pos[2])
        gamma_add, beta_add, z_add = ccc.adjust(z,GP.Leg2_Pos[2],GP.Leg3_Pos[2],GP.Leg4_Pos[2],GP.Leg5_Pos[2],GP.Leg6_Pos[2])
        ccc.twist_all(x,y,z+z_add,GP.Leg2_Pos[0],GP.Leg2_Pos[1],GP.Leg2_Pos[2],GP.Leg3_Pos[0],GP.Leg3_Pos[1],GP.Leg3_Pos[2],GP.Leg4_Pos[0],GP.Leg4_Pos[1],GP.Leg4_Pos[2],GP.Leg5_Pos[0],GP.Leg5_Pos[1],GP.Leg5_Pos[2],GP.Leg6_Pos[0],GP.Leg6_Pos[1],GP.Leg6_Pos[2], gamma_add, beta_add, z_add,1)
        #IK.InverseKinematics_Leg1(x,y,z,date)
        #Uart.SendDate(date)
        #time.sleep(0.1)
        GP.Leg1_Pos = [x, y, z]
        if (Read_GPIO(18) and (i>7)):
            #print(GPIO.input(15))
            break
        '''
        time.sleep(0.1)
        GP.Leg1_Pos = [x, y, z]
        if (Read_GPIO(15)):
            #print(GPIO.input(15))
            break
        time.sleep(0.1)
        GP.Leg1_Pos = [x, y, z]
        if (Read_GPIO(15)):
            #print(GPIO.input(15))
            break
        time.sleep(0.1)
        GP.Leg1_Pos = [x, y, z]
        if (Read_GPIO(15)):
            #print(GPIO.input(15))
            break
        if (-(Read_GPIO(15))):
            break
        '''

def Swing_Leg2(L,A):
    angle = A/180*PI
    
    for i in range(0,23):
        #date = bytearray(b'\x55\x55\x0E\x03\x03')
        #date.extend(Uart.AddTime(65))
        x = GP.Leg2_Pos[0] + L*math.cos(angle)*X_Index[i]
        y = GP.Leg2_Pos[1] + L*math.sin(angle)*Y_Index[i]
        z = GP.Leg2_Pos[2] + H*Z_Index[i]
        gamma_add, beta_add, z_add = ccc.adjust(GP.Leg1_Pos[2],z,GP.Leg3_Pos[2],GP.Leg4_Pos[2],GP.Leg5_Pos[2],GP.Leg6_Pos[2])
        ccc.twist_all(GP.Leg1_Pos[0],GP.Leg1_Pos[1],GP.Leg1_Pos[2],x, y,z+z_add,GP.Leg3_Pos[0],GP.Leg3_Pos[1],GP.Leg3_Pos[2],GP.Leg4_Pos[0],GP.Leg4_Pos[1],GP.Leg4_Pos[2],GP.Leg5_Pos[0],GP.Leg5_Pos[1],GP.Leg5_Pos[2],GP.Leg6_Pos[0],GP.Leg6_Pos[1],GP.Leg6_Pos[2], gamma_add, beta_add, z_add,2)

        #IK.InverseKinematics_Leg2(x,y,z,date)
        #Uart.SendDate(date)
        #time.sleep(0.1)
        GP.Leg2_Pos = [x, y, z]

        if (Read_GPIO(16) and (i>7)):
            #print(GPIO.input(15))
            break

def Swing_Leg3(L,A):
    angle = A/180*PI
    
    for i in range(0,23):
        #date = bytearray(b'\x55\x55\x0E\x03\x03')
        #date.extend(Uart.AddTime(65))
        x = GP.Leg3_Pos[0] + L*math.cos(angle)*X_Index[i]
        y = GP.Leg3_Pos[1] + L*math.sin(angle)*Y_Index[i]
        z = GP.Leg3_Pos[2] + H*Z_Index[i]
        gamma_add, beta_add, z_add = ccc.adjust(GP.Leg1_Pos[2],GP.Leg2_Pos[2],z,GP.Leg4_Pos[2],GP.Leg5_Pos[2],GP.Leg6_Pos[2])
        ccc.twist_all(GP.Leg1_Pos[0],GP.Leg1_Pos[1],GP.Leg1_Pos[2],GP.Leg2_Pos[0],GP.Leg2_Pos[1],GP.Leg2_Pos[2],x,y,z+z_add,GP.Leg4_Pos[0],GP.Leg4_Pos[1],GP.Leg4_Pos[2],GP.Leg5_Pos[0],GP.Leg5_Pos[1],GP.Leg5_Pos[2],GP.Leg6_Pos[0],GP.Leg6_Pos[1],GP.Leg6_Pos[2],gamma_add, beta_add, z_add,3)
        #IK.InverseKinematics_Leg3(x,y,z,date)
        #Uart.SendDate(date)
        #time.sleep(0.1)
        GP.Leg3_Pos = [x, y, z]

        if (Read_GPIO(12) and (i>7)):
            #print(GPIO.input(15))
            break

def Swing_Leg4(L,A):
    angle = A/180*PI
    
    for i in range(0,23):
        #date = bytearray(b'\x55\x55\x0E\x03\x03')
        #date.extend(Uart.AddTime(65))
        x = GP.Leg4_Pos[0] + L*math.cos(angle)*X_Index[i]
        y = GP.Leg4_Pos[1] + L*math.sin(angle)*Y_Index[i]
        z = GP.Leg4_Pos[2] + H*Z_Index[i]
        gamma_add, beta_add, z_add = ccc.adjust(GP.Leg1_Pos[2],GP.Leg2_Pos[2],GP.Leg3_Pos[2],z,GP.Leg5_Pos[2],GP.Leg6_Pos[2])
        ccc.twist_all(GP.Leg1_Pos[0],GP.Leg1_Pos[1],GP.Leg1_Pos[2],GP.Leg2_Pos[0],GP.Leg2_Pos[1],GP.Leg2_Pos[2],GP.Leg3_Pos[0],GP.Leg3_Pos[1],GP.Leg3_Pos[2],x,y,z+z_add,GP.Leg5_Pos[0],GP.Leg5_Pos[1],GP.Leg5_Pos[2],GP.Leg6_Pos[0],GP.Leg6_Pos[1],GP.Leg6_Pos[2],gamma_add, beta_add, z_add,4)

        #IK.InverseKinematics_Leg4(x,y,z,date)
        #Uart.SendDate(date)
        time.sleep(0.1)
        GP.Leg4_Pos = [x, y, z]

        if (Read_GPIO(11) and (i>7)):
            #print(GPIO.input(15))
            break

def Swing_Leg5(L,A):
    angle = A/180*PI
    
    for i in range(0,23):
        #date = bytearray(b'\x55\x55\x0E\x03\x03')
        #date.extend(Uart.AddTime(65))
        x = GP.Leg5_Pos[0] + L*math.cos(angle)*X_Index[i]
        y = GP.Leg5_Pos[1] + L*math.sin(angle)*Y_Index[i]
        z = GP.Leg5_Pos[2] + H*Z_Index[i]

        gamma_add, beta_add, z_add = ccc.adjust(GP.Leg1_Pos[2],GP.Leg2_Pos[2],GP.Leg3_Pos[2],GP.Leg4_Pos[2],z,GP.Leg6_Pos[2])
        ccc.twist_all(GP.Leg1_Pos[0],GP.Leg1_Pos[1],GP.Leg1_Pos[2],GP.Leg2_Pos[0],GP.Leg2_Pos[1],GP.Leg2_Pos[2],GP.Leg3_Pos[0],GP.Leg3_Pos[1],GP.Leg3_Pos[2],GP.Leg4_Pos[0],GP.Leg4_Pos[1],GP.Leg4_Pos[2],x,y,z+z_add,GP.Leg6_Pos[0],GP.Leg6_Pos[1],GP.Leg6_Pos[2],gamma_add, beta_add, z_add,5)
        #IK.InverseKinematics_Leg5(x,y,z,date)
        #Uart.SendDate(date)
        #time.sleep(0.1)
        GP.Leg5_Pos = [x, y, z]

        if (Read_GPIO(13) and (i>7)):
            #print(GPIO.input(15))
            break

def Swing_Leg6(L,A):
    angle = A/180*PI

    for i in range(0,23):
        #print("Hello")
        #date = bytearray(b'\x55\x55\x0E\x03\x03')
        #date.extend(Uart.AddTime(65))
        x = GP.Leg6_Pos[0] + L*math.cos(angle)*X_Index[i]
        y = GP.Leg6_Pos[1] + L*math.sin(angle)*Y_Index[i]
        z = GP.Leg6_Pos[2] + H*Z_Index[i]
        gamma_add, beta_add, z_add = ccc.adjust(GP.Leg1_Pos[2],GP.Leg2_Pos[2],GP.Leg3_Pos[2],GP.Leg4_Pos[2],GP.Leg5_Pos[2],z)
        ccc.twist_all(GP.Leg1_Pos[0],GP.Leg1_Pos[1],GP.Leg1_Pos[2],GP.Leg2_Pos[0],GP.Leg2_Pos[1],GP.Leg2_Pos[2],GP.Leg3_Pos[0],GP.Leg3_Pos[1],GP.Leg3_Pos[2],GP.Leg4_Pos[0],GP.Leg4_Pos[1],GP.Leg4_Pos[2],GP.Leg5_Pos[0],GP.Leg5_Pos[1],GP.Leg5_Pos[2],x,y,z+z_add,gamma_add, beta_add, z_add,6)
        #IK.InverseKinematics_Leg6(x,y,z,date)
        #Uart.SendDate(date)
        #time.sleep(0.1)
        GP.Leg6_Pos = [x,y,z]

        if (Read_GPIO(15) and (i>7)):
            #print(GPIO.input(15))
            break


def translation(L,N,A):
    date = bytearray(b'\x55\x55\x3B\x03\x12')
    date.extend(Uart.AddTime(65))
    angle = A/180*PI

    x1 = GP.Leg1_Pos[0] - L/N*math.cos(angle)
    y1 = GP.Leg1_Pos[1] - L/N*math.sin(angle)
    z1 = GP.Leg1_Pos[2]
    #IK.InverseKinematics_Leg1(x1,y1,z1,date)

    x2 = GP.Leg2_Pos[0] - L/N*math.cos(angle)
    y2 = GP.Leg2_Pos[1] - L/N*math.sin(angle)
    z2 = GP.Leg2_Pos[2]
    #IK.InverseKinematics_Leg2(x2,y2,z2,date)

    x3 = GP.Leg3_Pos[0] - L/N*math.cos(angle)
    y3 = GP.Leg3_Pos[1] - L/N*math.sin(angle)
    z3 = GP.Leg3_Pos[2]
    #IK.InverseKinematics_Leg3(x3,y3,z3,date)

    x4 = GP.Leg4_Pos[0] - L/N*math.cos(angle)
    y4 = GP.Leg4_Pos[1] - L/N*math.sin(angle)
    z4 = GP.Leg4_Pos[2]
    #IK.InverseKinematics_Leg4(x4,y4,z4,date)

    x5 = GP.Leg5_Pos[0] - L/N*math.cos(angle)
    y5 = GP.Leg5_Pos[1] - L/N*math.sin(angle)
    z5 = GP.Leg5_Pos[2]
    #IK.InverseKinematics_Leg5(x5,y5,z5,date)

    x6 = GP.Leg6_Pos[0] - L/N*math.cos(angle)
    y6 = GP.Leg6_Pos[1] - L/N*math.sin(angle)
    z6 = GP.Leg6_Pos[2]
    gamma_add, beta_add, z_add = ccc.adjust(z1,z2,z3,z4,z5,z6)
    ccc.twist_all(x1,y1,z1+z_add,x2,y2,z2+z_add,x3,y3,z3+z_add,x4,y4,z4+z_add,x5,y5,z5+z_add,x6,y6,z6+z_add, gamma_add, beta_add, z_add,'all')
    #IK.InverseKinematics_Leg6(x6,y6,z6,date)

    #Uart.SendDate(date)

    GP.Leg1_Pos[0] = x1
    GP.Leg1_Pos[1] = y1
    GP.Leg1_Pos[2] = z1
    GP.Leg2_Pos[0] = x2
    GP.Leg2_Pos[1] = y2
    GP.Leg2_Pos[2] = z2
    GP.Leg3_Pos[0] = x3
    GP.Leg3_Pos[1] = y3
    GP.Leg3_Pos[2] = z3
    GP.Leg4_Pos[0] = x4
    GP.Leg4_Pos[1] = y4
    GP.Leg4_Pos[2] = z4
    GP.Leg5_Pos[0] = x5
    GP.Leg5_Pos[1] = y5
    GP.Leg5_Pos[2] = z5
    GP.Leg6_Pos[0] = x6
    GP.Leg6_Pos[1] = y6
    GP.Leg6_Pos[2] = z6


def test():
    Robot_Init()
    time.sleep(5)
    L = 60
    A = 90
    while(1):
        Swing_Leg1(L,A)
        translation(L,6,A)
        Swing_Leg3(L,A)
        translation(L,6,A)
        Swing_Leg5(L,A)
        translation(L,6,A)
        Swing_Leg4(L,A)
        translation(L,6,A)
        Swing_Leg2(L,A)
        translation(L,6,A)
        Swing_Leg6(L,A)
        translation(L,6,A)

if __name__ == '__main__':
    test()