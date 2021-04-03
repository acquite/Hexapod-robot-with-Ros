#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import serial
import time

def ForwardKinematics_Leg1(Q11,Q12,Q13):
    L1 = 60.01
    L2 = 75.81
    L3 = 143.69
    X0 = -65.505
    Y0 = 120.505
    Z0 = 0
    q0 = -3.9269908169872414
    
    q11 = q0 - (Q11-500)/750*math.pi
    q12 = -(Q12-500)/750*math.pi
    q13 = (Q13-500)/750*math.pi-40/180*math.pi
    
    X = X0 + (L1+L2*math.cos(q12)+L3*math.cos(q13+q12))*math.cos(q11)
    Y = Y0 + (L1+L2*math.cos(q12)+L3*math.cos(q13+q12))*math.sin(q11)
    Z = Z0 + L2*math.sin(q12) + L3*math.sin(q13+q12)
    return X,Y,Z

def ForwardKinematics_Leg2(Q21,Q22,Q23):
    L1 = 60.01
    L2 = 75.81
    L3 = 143.69
    X0 = -116
    Y0 = 0
    Z0 = 0
    q0 = -math.pi
    
    q21 = q0 - (Q21-500)/750*math.pi
    q22 = -(Q22-500)/750*math.pi
    q23 = (Q23-500)/750*math.pi-40/180*math.pi
    
    X = X0 + (L1+L2*math.cos(q22)+L3*math.cos(q23+q22))*math.cos(q21)
    Y = Y0 + (L1+L2*math.cos(q22)+L3*math.cos(q23+q22))*math.sin(q21)
    Z = Z0 + L2*math.sin(q22) + L3*math.sin(q23+q22)
    return X,Y,Z

def ForwardKinematics_Leg3(Q31,Q32,Q33):
    L1 = 60.01
    L2 = 75.81
    L3 = 143.69
    X0 = -65.505
    Y0 = -120.505
    Z0 = 0
    q0 = -2.356194490192345
    
    q31 = q0 - (Q31-500)/750*math.pi
    q32 = -(Q32-500)/750*math.pi
    q33 = (Q33-500)/750*math.pi-40/180*math.pi
    
    X = X0 + (L1+L2*math.cos(q32)+L3*math.cos(q33+q32))*math.cos(q31)
    Y = Y0 + (L1+L2*math.cos(q32)+L3*math.cos(q33+q32))*math.sin(q31)
    Z = Z0 + L2*math.sin(q32) + L3*math.sin(q33+q32)
    return X,Y,Z

def ForwardKinematics_Leg4(Q41,Q42,Q43):
    L1 = 60.01
    L2 = 75.81
    L3 = 143.69
    X0 = 65.505
    Y0 = -120.505
    Z0 = 0
    q0 = -0.7853981633974483
    
    q41 = q0 - (Q41-500)/750*math.pi
    q42 = -(Q42-500)/750*math.pi
    q43 = (Q43-500)/750*math.pi-40/180*math.pi
    
    X = X0 + (L1+L2*math.cos(q42)+L3*math.cos(q43+q42))*math.cos(q41)
    Y = Y0 + (L1+L2*math.cos(q42)+L3*math.cos(q43+q42))*math.sin(q41)
    Z = Z0 + L2*math.sin(q42) + L3*math.sin(q43+q42)
    return X,Y,Z

def ForwardKinematics_Leg5(Q51,Q52,Q53):
    L1 = 60.01
    L2 = 75.81
    L3 = 143.69
    X0 = 116
    Y0 = 0
    Z0 = 0
    q0 = 0
    
    q51 = q0 - (Q51-500)/750*math.pi
    q52 = -(Q52-500)/750*math.pi
    q53 = (Q53-500)/750*math.pi-40/180*math.pi
    
    X = X0 + (L1+L2*math.cos(q52)+L3*math.cos(q53+q52))*math.cos(q51)
    Y = Y0 + (L1+L2*math.cos(q52)+L3*math.cos(q53+q52))*math.sin(q51)
    Z = Z0 + L2*math.sin(q52) + L3*math.sin(q53+q52)
    return X,Y,Z

def ForwardKinematics_Leg6(Q61,Q62,Q63):
    L1 = 60.01
    L2 = 75.81
    L3 = 143.69
    X0 = 65.505
    Y0 = 120.505
    Z0 = 0
    q0 = 0.7853981633974483
    
    q61 = q0 - (Q61-500)/750*math.pi
    q62 = -(Q62-500)/750*math.pi
    q63 = (Q63-500)/750*math.pi-40/180*math.pi
    
    X = X0 + (L1+L2*math.cos(q62)+L3*math.cos(q63+q62))*math.cos(q61)
    Y = Y0 + (L1+L2*math.cos(q62)+L3*math.cos(q63+q62))*math.sin(q61)
    Z = Z0 + L2*math.sin(q62) + L3*math.sin(q63+q62)
    return X,Y,Z


def Tempxyz():
    ser=serial.Serial('/dev/ttyUSB1',9600)
    buf = bytearray(b'\x55\x55\x15\x15\x12\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10\x11\x12')
    ser.write(buf)

    time.sleep(0.5)
    count = ser.inWaiting()
    recv_data = ser.read(count)
    Q11 = 0xffff & (recv_data[6]  | (0xff00 & (recv_data[7]  << 8)))
    Q12 = 0xffff & (recv_data[9]  | (0xff00 & (recv_data[10] << 8)))
    Q13 = 0xffff & (recv_data[12] | (0xff00 & (recv_data[13] << 8)))
    Q21 = 0xffff & (recv_data[15] | (0xff00 & (recv_data[16] << 8)))
    Q22 = 0xffff & (recv_data[18] | (0xff00 & (recv_data[19] << 8)))
    Q23 = 0xffff & (recv_data[21] | (0xff00 & (recv_data[22] << 8)))
    Q31 = 0xffff & (recv_data[24] | (0xff00 & (recv_data[25] << 8)))
    Q32 = 0xffff & (recv_data[27] | (0xff00 & (recv_data[28] << 8)))
    Q33 = 0xffff & (recv_data[30] | (0xff00 & (recv_data[31] << 8)))
    Q41 = 0xffff & (recv_data[33] | (0xff00 & (recv_data[34] << 8)))
    Q42 = 0xffff & (recv_data[36] | (0xff00 & (recv_data[37] << 8)))
    Q43 = 0xffff & (recv_data[39] | (0xff00 & (recv_data[40] << 8)))
    Q51 = 0xffff & (recv_data[42] | (0xff00 & (recv_data[43] << 8)))
    Q52 = 0xffff & (recv_data[45] | (0xff00 & (recv_data[46] << 8)))
    Q53 = 0xffff & (recv_data[48] | (0xff00 & (recv_data[49] << 8)))
    Q61 = 0xffff & (recv_data[51] | (0xff00 & (recv_data[52] << 8)))
    Q62 = 0xffff & (recv_data[54] | (0xff00 & (recv_data[55] << 8)))
    Q63 = 0xffff & (recv_data[57] | (0xff00 & (recv_data[58] << 8)))
    
    tx1 = ForwardKinematics_Leg1(Q11,Q12,Q13)[0]
    ty1 = ForwardKinematics_Leg1(Q11,Q12,Q13)[1]
    tz1 = ForwardKinematics_Leg1(Q11,Q12,Q13)[2]
    tx2 = ForwardKinematics_Leg2(Q21,Q22,Q23)[0]
    ty2 = ForwardKinematics_Leg2(Q21,Q22,Q23)[1]
    tz2 = ForwardKinematics_Leg2(Q21,Q22,Q23)[2]
    tx3 = ForwardKinematics_Leg3(Q31,Q32,Q33)[0]
    ty3 = ForwardKinematics_Leg3(Q31,Q32,Q33)[1]
    tz3 = ForwardKinematics_Leg3(Q31,Q32,Q33)[2]
    tx4 = ForwardKinematics_Leg4(Q41,Q42,Q43)[0]
    ty4 = ForwardKinematics_Leg4(Q41,Q42,Q43)[1]
    tz4 = ForwardKinematics_Leg4(Q41,Q42,Q43)[2]
    tx5 = ForwardKinematics_Leg5(Q51,Q52,Q53)[0]
    ty5 = ForwardKinematics_Leg5(Q51,Q52,Q53)[1]
    tz5 = ForwardKinematics_Leg5(Q51,Q52,Q53)[2]
    tx6 = ForwardKinematics_Leg6(Q61,Q62,Q63)[0]
    ty6 = ForwardKinematics_Leg6(Q61,Q62,Q63)[1]
    tz6 = ForwardKinematics_Leg6(Q61,Q62,Q63)[2]
    
    return tx1,ty1,tz1,tx2,ty2,tz2,tx3,ty3,tz3,tx4,ty4,tz4,tx5,ty5,tz5,tx6,ty6,tz6

#print(Tempxyz())
#print('\n')
#print(Tempxyz()[0])
