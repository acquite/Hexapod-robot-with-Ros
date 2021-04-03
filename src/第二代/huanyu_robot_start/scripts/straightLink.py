#!/usr/bin/env python
# -*- coding: utf-8 -*-

import stepcutLink
import ForwardKinematics
import math
import Uart
import serial

Xa,Ya,Za = -175,  230, -77
Xb,Yb,Zb = -270,  0,   -77
Xc,Yc,Zc = -175, -230, -77
Xd,Yd,Zd =  175, -230, -77
Xe,Ye,Ze =  270,  0,   -77
Xf,Yf,Zf =  175,  230, -77

ser=serial.Serial('/dev/ttyUSB1',9600)
#ser=serial.Serial('/dev/ttyACM0',9600)


def straight_Leg1_Link(L,A1,tx,ty,tz,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xa
    y0 = L/2*math.sin(Angle)+Ya
    z0 = Za
    x1 = -L/2*math.cos(Angle)+Xa
    y1 = -L/2*math.sin(Angle)+Ya
    z1 = Za
    stepcutLink.StepCut_Leg1_Link(x0,y0,z0,x1,y1,z1,tx,ty,tz,i,step,date)


def straight_Leg2_Link(L,A1,tx,ty,tz,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xb
    y0 = L/2*math.sin(Angle)+Yb
    z0 = Zb
    x1 = -L/2*math.cos(Angle)+Xb
    y1 = -L/2*math.sin(Angle)+Yb
    z1 = Zb
    stepcutLink.StepCut_Leg2_Link(x0,y0,z0,x1,y1,z1,tx,ty,tz,i,step,date)


def straight_Leg3_Link(L,A1,tx,ty,tz,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xc
    y0 = L/2*math.sin(Angle)+Yc
    z0 = Zc
    x1 = -L/2*math.cos(Angle)+Xc
    y1 = -L/2*math.sin(Angle)+Yc
    z1 = Zc
    stepcutLink.StepCut_Leg3_Link(x0,y0,z0,x1,y1,z1,tx,ty,tz,i,step,date)


def straight_Leg4_Link(L,A1,tx,ty,tz,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xd
    y0 = L/2*math.sin(Angle)+Yd
    z0 = Zd
    x1 = -L/2*math.cos(Angle)+Xd
    y1 = -L/2*math.sin(Angle)+Yd
    z1 = Zd
    stepcutLink.StepCut_Leg4_Link(x0,y0,z0,x1,y1,z1,tx,ty,tz,i,step,date)


def straight_Leg5_Link(L,A1,tx,ty,tz,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xe
    y0 = L/2*math.sin(Angle)+Ye
    z0 = Ze
    x1 = -L/2*math.cos(Angle)+Xe
    y1 = -L/2*math.sin(Angle)+Ye
    z1 = Ze
    stepcutLink.StepCut_Leg5_Link(x0,y0,z0,x1,y1,z1,tx,ty,tz,i,step,date)


def straight_Leg6_Link(L,A1,tx,ty,tz,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xf
    y0 = L/2*math.sin(Angle)+Yf
    z0 = Zf
    x1 = -L/2*math.cos(Angle)+Xf
    y1 = -L/2*math.sin(Angle)+Yf
    z1 = Zf
    stepcutLink.StepCut_Leg6_Link(x0,y0,z0,x1,y1,z1,tx,ty,tz,i,step,date)


def straightLeg_Link(Length,dir,time):
    step = 15
    tx1 = ForwardKinematics.Tempxyz()[0]
    ty1 = ForwardKinematics.Tempxyz()[1]
    tz1 = ForwardKinematics.Tempxyz()[2]
    tx2 = ForwardKinematics.Tempxyz()[3]
    ty2 = ForwardKinematics.Tempxyz()[4]
    tz2 = ForwardKinematics.Tempxyz()[5]
    tx3 = ForwardKinematics.Tempxyz()[6]
    ty3 = ForwardKinematics.Tempxyz()[7]
    tz3 = ForwardKinematics.Tempxyz()[8]
    tx4 = ForwardKinematics.Tempxyz()[9]
    ty4 = ForwardKinematics.Tempxyz()[10]
    tz4 = ForwardKinematics.Tempxyz()[11]
    tx5 = ForwardKinematics.Tempxyz()[12]
    ty5 = ForwardKinematics.Tempxyz()[13]
    tz5 = ForwardKinematics.Tempxyz()[14]
    tx6 = ForwardKinematics.Tempxyz()[15]
    ty6 = ForwardKinematics.Tempxyz()[16]
    tz6 = ForwardKinematics.Tempxyz()[17]
    for i in range(0,31):
        date = bytearray(b'\x55\x55\x3B\x03\x12')
        date.extend(Uart.AddTime(65))
        straight_Leg1_Link(Length,dir,tx1,ty1,tz1,i,step,date)
        straight_Leg2_Link(Length,dir,tx2,ty2,tz2,i,step,date)
        straight_Leg3_Link(Length,dir,tx3,ty3,tz3,i,step,date)
        straight_Leg4_Link(Length,dir,tx4,ty4,tz4,i,step,date)
        straight_Leg5_Link(Length,dir,tx5,ty5,tz5,i,step,date)
        straight_Leg6_Link(Length,dir,tx6,ty6,tz6,i,step,date)
        ser.write(date)
        #time.sleep(0.065)
        #print(date)
        #print('\n')
