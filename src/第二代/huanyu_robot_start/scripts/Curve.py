#!/usr/bin/env python
# -*- coding: utf-8 -*-
import stepcut
import math
import serial
import Uart

Xa,Ya,Za = -175,  230, -77
Xb,Yb,Zb = -270,  0,   -77
Xc,Yc,Zc = -175, -230, -77
Xd,Yd,Zd =  175, -230, -77
Xe,Ye,Ze =  270,  0,   -77
Xf,Yf,Zf =  175,  230, -77

ser=serial.Serial('/dev/ttyUSB1',9600)
#ser=serial.Serial('/dev/ttyACM0',9600)


def Curve_Leg1(R,A2,i,step,date):
    Angle = A2/180*math.pi
    if (R<-abs(Xb)):
        R = -R
        q1 = math.atan(Ya/(R+Xa))
        r1 = math.sqrt((R+Xa)**2+(Ya)**2)
        x0 = r1*math.cos(q1+Angle/2)-R
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Za
        x1 = r1*math.cos(q1-Angle/2)-R
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Za
        stepcut.StepCut_Leg1(x0,y0,z0,x1,y1,z1,i,step,date)
    elif ((R>-abs(Xb)) and (R<0)):
        R = -R
        La = math.sqrt((Xa+R)**2+Ya**2)
        Lb = math.sqrt(Xa**2+Ya**2)
        q1 = math.acos((R**2+La**2-Lb**2)/(2*La*R))
        x0 = La*math.cos(q1+Angle/2)-R
        y0 = La*math.sin(q1+Angle/2)
        z0 = Za
        x1 = La*math.cos(q1-Angle/2)-R
        y1 = La*math.sin(q1-Angle/2)
        z1 = Za
        stepcut.StepCut_Leg1(x0,y0,z0,x1,y1,z1,i,step,date)
    elif (R==0):
        q1 = math.pi - math.atan(Ya/-Xa)
        r1 = math.sqrt(Ya**2 + Xa**2)
        x0 = r1*math.cos(q1+Angle/2)
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Za
        x1 = r1*math.cos(q1-Angle/2)
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Za
        stepcut.StepCut_Leg1(x0,y0,z0,x1,y1,z1,i,step,date)
    elif ((R>0) and (R<abs(Xb))):
        La = math.sqrt((Xa-R)**2+Ya**2)
        Lb = math.sqrt(Xa**2+Ya**2)
        q1 = math.acos((R**2+La**2-Lb**2)/(2*La*R))
        x0 = -La*math.cos(q1+Angle/2)+R
        y0 = La*math.sin(q1+Angle/2)
        z0 = Za
        x1 = -La*math.cos(q1-Angle/2)+R
        y1 = La*math.sin(q1-Angle/2)
        z1 = Za
        stepcut.StepCut_Leg1(x0,y0,z0,x1,y1,z1,i,step,date)
    else:
        q1 = math.atan(Ya/(-Xa+R))
        r1 = math.sqrt((R-Xa)**2+Ya**2)
        x0 = -r1*math.cos(q1+Angle/2)+R
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Za
        x1 = -r1*math.cos(q1-Angle/2)+R
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Za
        stepcut.StepCut_Leg1(x0,y0,z0,x1,y1,z1,i,step,date)



def Curve_Leg2(R,A2,i,step,date):
    Angle = A2/180*math.pi
    if (R<-abs(Xb)):
        R = -R
        q1 = 0
        r1 = R+Xb
        x0 = r1*math.cos(q1+Angle/2)-R
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Zb
        x1 = r1*math.cos(q1-Angle/2)-R
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Zb
        stepcut.StepCut_Leg2(x0,y0,z0,x1,y1,z1,i,step,date)
    elif ((R>-abs(Xb)) and (R<0)):
        R = -R
        La = -(R+Xb)
        #Lb = 263.41
        q1 = 0
        x0 = -La*math.cos(q1-Angle/2)-R
        y0 = La*math.sin(q1-Angle/2)
        z0 = Zb
        x1 = -La*math.cos(q1+Angle/2)-R
        y1 = La*math.sin(q1+Angle/2)
        z1 = Zb
        stepcut.StepCut_Leg2(x0,y0,z0,x1,y1,z1,i,step,date)
    elif (R==0):
        q1 = math.pi
        r1 = abs(Xb)
        x0 = r1*math.cos(q1+Angle/2)
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Zb
        x1 = r1*math.cos(q1-Angle/2)
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Zb
        stepcut.StepCut_Leg2(x0,y0,z0,x1,y1,z1,i,step,date)
    elif ((R>0) and (R<abs(Xb))):
        La = abs(Xb)+R
        #Lb = 263.41
        q1 = 0
        x0 = -La*math.cos(q1+Angle/2)+R
        y0 = La*math.sin(q1+Angle/2)
        z0 = Zb
        x1 = -La*math.cos(q1-Angle/2)+R
        y1 = La*math.sin(q1-Angle/2)
        z1 = Zb
        stepcut.StepCut_Leg2(x0,y0,z0,x1,y1,z1,i,step,date)
    else:
        q1 = 0
        r1 = R+abs(Xb)
        x0 = -r1*math.cos(q1+Angle/2)+R
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Zb
        x1 = -r1*math.cos(q1-Angle/2)+R
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Zb
        stepcut.StepCut_Leg2(x0,y0,z0,x1,y1,z1,i,step,date)


def Curve_Leg3(R,A2,i,step,date):
    Angle = A2/180*math.pi
    if (R<-abs(Xb)):
        R = -R
        q1 = math.atan(-Yc/(R+Xc))
        r1 = math.sqrt((R+Xc)**2+Yc**2)
        x0 = r1*math.cos(q1-Angle/2)-R
        y0 = -r1*math.sin(q1-Angle/2)
        z0 = Zc
        x1 = r1*math.cos(q1+Angle/2)-R
        y1 = -r1*math.sin(q1+Angle/2)
        z1 = Zc
        stepcut.StepCut_Leg3(x0,y0,z0,x1,y1,z1,i,step,date)
    elif ((R>-abs(Xb)) and (R<0)):
        R = -R
        La = math.sqrt((Xc+R)**2+Yc**2)
        Lb = math.sqrt(Xc**2+Yc**2)
        q1 = math.acos((R**2+La**2-Lb**2)/(2*La*R))
        x0 = La*math.cos(q1-Angle/2)-R
        y0 = -La*math.sin(q1-Angle/2)
        z0 = Zc
        x1 = La*math.cos(q1+Angle/2)-R
        y1 = -La*math.sin(q1+Angle/2)
        z1 = Zc
        stepcut.StepCut_Leg3(x0,y0,z0,x1,y1,z1,i,step,date)
    elif (R==0):
        q1 = math.pi + math.atan(Yc/Xc)
        r1 = math.sqrt(Yc**2 + Xc**2)
        x0 = r1*math.cos(q1+Angle/2)
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Zc
        x1 = r1*math.cos(q1-Angle/2)
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Zc
        stepcut.StepCut_Leg3(x0,y0,z0,x1,y1,z1,i,step,date)
    elif ((R>0) and (R<abs(Xb))):
        La = math.sqrt((-Xc+R)**2+Yc**2)
        Lb = math.sqrt(Xc**2+Yc**2)
        q1 = math.acos((R**2+La**2-Lb**2)/(2*La*R))
        x0 = -La*math.cos(q1-Angle/2)+R
        y0 = -La*math.sin(q1-Angle/2)
        z0 = Zc
        x1 = -La*math.cos(q1+Angle/2)+R
        y1 = -La*math.sin(q1+Angle/2)
        z1 = Zc
        stepcut.StepCut_Leg3(x0,y0,z0,x1,y1,z1,i,step,date)
    else:
        q1 = math.atan(-Yc/(R-Xc))
        r1 = math.sqrt((R-Xc)**2+(Yc)**2)
        x0 = -r1*math.cos(q1-Angle/2)+R
        y0 = -r1*math.sin(q1-Angle/2)
        z0 = Zc
        x1 = -r1*math.cos(q1+Angle/2)+R
        y1 = -r1*math.sin(q1+Angle/2)
        z1 = Zc
        stepcut.StepCut_Leg3(x0,y0,z0,x1,y1,z1,i,step,date)


def Curve_Leg4(R,A2,i,step,date):
    Angle = A2/180*math.pi
    if (R<-abs(Xb)):
        R = -R
        q1 = math.atan(-Yd/(R+Xd))
        r1 = math.sqrt((R+Xd)**2+(Yd)**2)
        x0 = r1*math.cos(q1-Angle/2)-R
        y0 = -r1*math.sin(q1-Angle/2)
        z0 = Zd
        x1 = r1*math.cos(q1+Angle/2)-R
        y1 = -r1*math.sin(q1+Angle/2)
        z1 = Zd
        stepcut.StepCut_Leg4(x0,y0,z0,x1,y1,z1,i,step,date)
    elif ((R>-abs(Xb)) and (R<0)):
        R = -R
        La = math.sqrt((Xd+R)**2+Yd**2)
        Lb = math.sqrt(Xd**2+Yd**2)
        q1 = math.acos((R**2+La**2-Lb**2)/(2*La*R))
        x0 = La*math.cos(q1-Angle/2)-R
        y0 = -La*math.sin(q1-Angle/2)
        z0 = Zd
        x1 = La*math.cos(q1+Angle/2)-R
        y1 = -La*math.sin(q1+Angle/2)
        z1 = Zd
        stepcut.StepCut_Leg4(x0,y0,z0,x1,y1,z1,i,step,date)
    elif (R==0):
        q1 = -math.atan(-Yd/Xd)
        r1 = math.sqrt(Yd**2 + Xd**2)
        x0 = r1*math.cos(q1+Angle/2)
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Zd
        x1 = r1*math.cos(q1-Angle/2)
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Zd
        stepcut.StepCut_Leg4(x0,y0,z0,x1,y1,z1,i,step,date)
    elif ((R>0) and (R<abs(Xb))):
        La = math.sqrt((Xd-R)**2+Yd**2)
        Lb = math.sqrt(Xd**2+Yd**2)
        q1 = math.acos((R**2+La**2-Lb**2)/(2*La*R))
        x0 = -La*math.cos(q1-Angle/2)+R
        y0 = -La*math.sin(q1-Angle/2)
        z0 = Zd
        x1 = -La*math.cos(q1+Angle/2)+R
        y1 = -La*math.sin(q1+Angle/2)
        z1 = Zd
        stepcut.StepCut_Leg4(x0,y0,z0,x1,y1,z1,i,step,date)
    else:
        q1 = math.atan(-Yd/(R-Xd))
        r1 = math.sqrt((R-Xd)**2+(Yd)**2)
        x0 = -r1*math.cos(q1-Angle/2)+R
        y0 = -r1*math.sin(q1-Angle/2)
        z0 = Zd
        x1 = -r1*math.cos(q1+Angle/2)+R
        y1 = -r1*math.sin(q1+Angle/2)
        z1 = Zd
        stepcut.StepCut_Leg4(x0,y0,z0,x1,y1,z1,i,step,date)


def Curve_Leg5(R,A2,i,step,date):
    Angle = A2/180*math.pi
    if (R<-abs(Xb)):
        R = -R
        q1 = 0
        r1 = R+Xe
        x0 = r1*math.cos(q1+Angle/2)-R
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Ze
        x1 = r1*math.cos(q1-Angle/2)-R
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Ze
        stepcut.StepCut_Leg5(x0,y0,z0,x1,y1,z1,i,step,date)
    elif ((R>-abs(Xb)) and (R<0)):
        R = -R
        La = Xe+R
        #Lb = 263.41
        q1 = 0
        x0 = La*math.cos(q1+Angle/2)-R
        y0 = La*math.sin(q1+Angle/2)
        z0 = Ze
        x1 = La*math.cos(q1-Angle/2)-R
        y1 = La*math.sin(q1-Angle/2)
        z1 = Ze
        stepcut.StepCut_Leg5(x0,y0,z0,x1,y1,z1,i,step,date)
    elif (R==0):
        q1 = 0
        r1 = Xe
        x0 = r1*math.cos(q1+Angle/2)
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Ze
        x1 = r1*math.cos(q1-Angle/2)
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Ze
        stepcut.StepCut_Leg5(x0,y0,z0,x1,y1,z1,i,step,date)
    elif ((R>0) and (R<abs(Xb))):
        La = Xe-R
        #Lb = 263.41
        q1 = 0
        x0 = La*math.cos(q1-Angle/2)+R
        y0 = La*math.sin(q1-Angle/2)
        z0 = Ze
        x1 = La*math.cos(q1+Angle/2)+R
        y1 = La*math.sin(q1+Angle/2)
        z1 = Ze
        stepcut.StepCut_Leg5(x0,y0,z0,x1,y1,z1,i,step,date)
    else:
        q1 = 0
        r1 = R-Xe
        x0 = -r1*math.cos(q1+Angle/2)+R
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Ze
        x1 = -r1*math.cos(q1-Angle/2)+R
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Ze
        stepcut.StepCut_Leg5(x0,y0,z0,x1,y1,z1,i,step,date)


def Curve_Leg6(R,A2,i,step,date):
    Angle = A2/180*math.pi
    if (R<-abs(Xb)):
        R = -R
        q1 = math.atan(Yf/(R+Xf))
        r1 = math.sqrt((R+Xf)**2+(Yf)**2)
        x0 = r1*math.cos(q1+Angle/2)-R
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Zf
        x1 = r1*math.cos(q1-Angle/2)-R
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Zf
        stepcut.StepCut_Leg6(x0,y0,z0,x1,y1,z1,i,step,date)
    elif ((R>-abs(Xb)) and (R<0)):
        R = -R
        La = math.sqrt((Xf+R)**2+Yf**2)
        Lb = math.sqrt(Xf**2+Yf**2)
        q1 = math.acos((R**2+La**2-Lb**2)/(2*La*R))
        x0 = La*math.cos(q1+Angle/2)-R
        y0 = La*math.sin(q1+Angle/2)
        z0 = Zf
        x1 = La*math.cos(q1-Angle/2)-R
        y1 = La*math.sin(q1-Angle/2)
        z1 = Zf
        stepcut.StepCut_Leg6(x0,y0,z0,x1,y1,z1,i,step,date)
    elif (R==0):
        q1 = math.atan(Yf/Xf)
        r1 = math.sqrt(Yf**2 + Xf**2)
        x0 = r1*math.cos(q1+Angle/2)
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Zf
        x1 = r1*math.cos(q1-Angle/2)
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Zf
        stepcut.StepCut_Leg6(x0,y0,z0,x1,y1,z1,i,step,date)
    elif ((R>0) and (R<abs(Xb))):
        La = math.sqrt((Xf-R)**2+Yf**2)
        Lb = math.sqrt(Xf**2+Yf**2)
        q1 = math.acos((R**2+La**2-Lb**2)/(2*La*R))
        x0 = -La*math.cos(q1+Angle/2)+R
        y0 = La*math.sin(q1+Angle/2)
        z0 = Zf
        x1 = -La*math.cos(q1-Angle/2)+R
        y1 = La*math.sin(q1-Angle/2)
        z1 = Zf
        stepcut.StepCut_Leg6(x0,y0,z0,x1,y1,z1,i,step,date)
    else:
        q1 = math.atan(Yf/(R-Xf))
        r1 = math.sqrt((R-Xf)**2+(Yf)**2)
        x0 = -r1*math.cos(q1+Angle/2)+R
        y0 = r1*math.sin(q1+Angle/2)
        z0 = Zf
        x1 = -r1*math.cos(q1-Angle/2)+R
        y1 = r1*math.sin(q1-Angle/2)
        z1 = Zf
        stepcut.StepCut_Leg6(x0,y0,z0,x1,y1,z1,i,step,date)


def CurveLeg(Radius,angle,time):
    step = 15
    for i in range(0,31):
        date = bytearray(b'\x55\x55\x3B\x03\x12')
        date.extend(Uart.AddTime(65))
        Curve_Leg1(Radius,angle,i,step,date)
        Curve_Leg2(Radius,angle,i,step,date)
        Curve_Leg3(Radius,angle,i,step,date)
        Curve_Leg4(Radius,angle,i,step,date)
        Curve_Leg5(Radius,angle,i,step,date)
        Curve_Leg6(Radius,angle,i,step,date)
        ser.write(date)
        #print(date)
