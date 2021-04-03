#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import math as m
import Uart
import stepdrive
import serial


def twist_all(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,x5,y5,z5,x6,y6,z6,gamma, beta, zc,leg_id):
    Rz = np.array([[1, 0, 0],[0, 1, 0],[0 ,0 ,1  ]])
    Ry = np.array([[m.cos(beta) , 0 ,m.sin(beta)],[0       , 1 ,0          ],[-m.sin(beta), 0 ,m.cos(beta)]])
    Rx = np.array([[1  ,0  ,0],[0 ,m.cos(gamma),-m.sin(gamma)],[0 ,m.sin(gamma),m.cos(gamma) ]])
    R1 = np.dot(Rz,Ry,)
    R = np.dot(R1,Rx)
    Rp = np.array([[R[0][0],R[0][1],R[0][2],0],[R[1][0],R[1][1],R[1][2],0],[R[2][0],R[2][1],R[2][2],zc],[0     ,0     ,0     ,1]])
#    one = np.array([[-114.94], [261.0668], [-140], [1]])
#    two = np.array([[-276], [0], [-140], [1]])
#    three = np.array([[-114.94], [-261.0668], [-140], [1]])
#    four = np.array([[114.94], [-261.06680], [-140], [1]])
#    five = np.array([[276], [0], [-140], [1]])
#    six = np.array([[114.94], [261.0668], [-140], [1]])
    one = np.array([[x1], [y1], [z1], [1]])
    two = np.array([[x2], [y2], [z2], [1]])
    three = np.array([[x3], [y3], [z3], [1]])
    four = np.array([[x4], [y4], [z4], [1]])
    five = np.array([[x5], [y5], [z5], [1]])
    six = np.array([[x6], [y6], [z6], [1]])
    P_one = np.dot(Rp,one)
    P_two = np.dot(Rp,two)
    P_three = np.dot(Rp,three)
    P_four = np.dot(Rp,four)
    P_five = np.dot(Rp,five)
    P_six = np.dot(Rp,six)
    date = bytearray(b'\x55\x55\x3B\x03\x12')
    date.extend(Uart.AddTime(65))
    #print(P_one[0],P_one[1],z1)
    #stepdrive.InverseKinematics_Leg1(P_one[0],P_one[1],P_one[2],date)
    #stepdrive.InverseKinematics_Leg2(P_two[0],P_two[1],P_two[2],date)
    #stepdrive.InverseKinematics_Leg3(P_three[0],P_three[1],P_three[2],date)
    #stepdrive.InverseKinematics_Leg4(P_four[0],P_four[1],P_four[2],date)
    #stepdrive.InverseKinematics_Leg5(P_five[0],P_five[1],P_five[2],date)
    #stepdrive.InverseKinematics_Leg6(P_six[0],P_six[1],P_six[2],date)
    
    if leg_id == 1:
        stepdrive.InverseKinematics_Leg1(P_one[0],P_one[1],z1,date)
    else:
        stepdrive.InverseKinematics_Leg1(P_one[0],P_one[1],P_one[2],date)
    if leg_id == 2:
        stepdrive.InverseKinematics_Leg2(P_two[0],P_two[1],z2,date)
    else :
        stepdrive.InverseKinematics_Leg2(P_two[0],P_two[1],P_two[2],date)
    if leg_id == 3:
        stepdrive.InverseKinematics_Leg3(P_three[0],P_three[1],z3,date)
    else:
        stepdrive.InverseKinematics_Leg3(P_three[0],P_three[1],P_three[2],date)
    if leg_id == 4:
        stepdrive.InverseKinematics_Leg4(P_four[0],P_four[1],z4,date)
    else:
        stepdrive.InverseKinematics_Leg4(P_four[0],P_four[1],P_four[2],date)
    if leg_id == 5:
        stepdrive.InverseKinematics_Leg5(P_five[0],P_five[1],z5,date)
    else:
        stepdrive.InverseKinematics_Leg5(P_five[0],P_five[1],P_five[2],date)
    if leg_id == 6 :
        stepdrive.InverseKinematics_Leg6(P_six[0],P_six[1],z6,date)
    else:
        stepdrive.InverseKinematics_Leg6(P_six[0],P_six[1],P_six[2],date)
    #print(P_two)
    Uart.SendDate(date)
    #ser.write(date)
    #print(date)


def adjust(z1,z2,z3,z4,z5,z6):
    z0 = -95
    Ka1 = 0.001
    Ka2 = 0.0005
    Ka3 = 0.001
    Kz = 0.3
    add_z = -Kz*(z1+z2+z3+z4+z5+z6-6*z0)
    add_gamma = Ka1*( (z3+z6-2*z0)-(z1+z4-2*z0))
    #print('add_gamma=',add_gamma)
    add_beta = Ka2*((z1+z3-2*z0)-(z4+z5-2*z0))+Ka3*((z2-z0)-(z5-z0))
    return add_gamma,add_beta,add_z
