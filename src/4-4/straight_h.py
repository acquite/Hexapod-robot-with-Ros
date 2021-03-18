import stepcut
import math
import Uart
import serial

import time

import stepdrive as IK

#Leg4
Xa,Ya,Za = -145,  155, -255

#Leg5
Xb,Yb,Zb = -185,  0,   -255

#Leg6
Xc,Yc,Zc = -145, -155, -255

#Leg3
Xd,Yd,Zd =  145, -155, -255

#Leg2
Xe,Ye,Ze =  185,  0,   -255

#Leg1
Xf,Yf,Zf =  145,  155, -255

'''
Xa,Ya,Za = -175,  230, -77
Xb,Yb,Zb = -270,  0,   -77
Xc,Yc,Zc = -175, -230, -77
Xd,Yd,Zd =  175, -230, -77
Xe,Ye,Ze =  270,  0,   -77
Xf,Yf,Zf =  175,  230, -77
'''

#ser=serial.Serial('/dev/ttyUSB0',9600)
#ser=serial.Serial('COM3',9600)
def robot_stand():
    date = bytearray(b'\x55\x55\x20\x03\x09')
    date.extend(Uart.AddTime(65))
    IK.InverseKinematics_Leg1(145,  155, -90, date)
    IK.InverseKinematics_Leg3(145, -155, -90, date)
    IK.InverseKinematics_Leg5(-185, 0, -90, date)
    Uart.SendDate(date)
    time.sleep(0.1)
    date = bytearray(b'\x55\x55\x20\x03\x09')
    date.extend(Uart.AddTime(65))
    IK.InverseKinematics_Leg1(145,  155, -95, date)
    IK.InverseKinematics_Leg3(145, -155, -95, date)
    IK.InverseKinematics_Leg5(-185, 0, -95, date)
    Uart.SendDate(date)
    time.sleep(0.1)
    date = bytearray(b'\x55\x55\x20\x03\x09')
    date.extend(Uart.AddTime(65))
    IK.InverseKinematics_Leg2(185,  0, -90, date)
    IK.InverseKinematics_Leg4(-145, 155, -90, date)
    IK.InverseKinematics_Leg6(-145, -155, -90, date)
    Uart.SendDate(date)
    time.sleep(0.1)
    date = bytearray(b'\x55\x55\x20\x03\x09')
    date.extend(Uart.AddTime(65))
    IK.InverseKinematics_Leg2(185,  0, -95, date)
    IK.InverseKinematics_Leg4(-145, 155, -95, date)
    IK.InverseKinematics_Leg6(-145, -155, -95, date)
    Uart.SendDate(date)
    time.sleep(0.1)
    date = bytearray(b'\x55\x55\x3B\x03\x12')
    date.extend(Uart.AddTime(65))
    IK.InverseKinematics_Leg1( 145, 155,-255, date)
    IK.InverseKinematics_Leg2( 185, 0,  -255, date)
    IK.InverseKinematics_Leg3( 145,-155,-255, date)
    IK.InverseKinematics_Leg4(-145, 155,-255, date)
    IK.InverseKinematics_Leg5(-185, 0,  -255, date)
    IK.InverseKinematics_Leg6(-145,-155,-255, date)
    Uart.SendDate(date)
    time.sleep(0.5)

def straight_h_Leg4(L,A1,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xa
    y0 = L/2*math.sin(Angle)+Ya
    z0 = Za
    x1 = -L/2*math.cos(Angle)+Xa
    y1 = -L/2*math.sin(Angle)+Ya
    z1 = Za
    stepcut.StepCut_Leg4(x0,y0,z0,x1,y1,z1,i,step,date)


def straight_h_Leg5(L,A1,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xb
    y0 = L/2*math.sin(Angle)+Yb
    z0 = Zb
    x1 = -L/2*math.cos(Angle)+Xb
    y1 = -L/2*math.sin(Angle)+Yb
    z1 = Zb
    stepcut.StepCut_Leg5(x0,y0,z0,x1,y1,z1,i,step,date)


def straight_h_Leg6(L,A1,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xc
    y0 = L/2*math.sin(Angle)+Yc
    z0 = Zc
    x1 = -L/2*math.cos(Angle)+Xc
    y1 = -L/2*math.sin(Angle)+Yc
    z1 = Zc
    stepcut.StepCut_Leg6(x0,y0,z0,x1,y1,z1,i,step,date)


def straight_h_Leg3(L,A1,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xd
    y0 = L/2*math.sin(Angle)+Yd
    z0 = Zd
    x1 = -L/2*math.cos(Angle)+Xd
    y1 = -L/2*math.sin(Angle)+Yd
    z1 = Zd
    stepcut.StepCut_Leg3(x0,y0,z0,x1,y1,z1,i,step,date)


def straight_h_Leg2(L,A1,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xe
    y0 = L/2*math.sin(Angle)+Ye
    z0 = Ze
    x1 = -L/2*math.cos(Angle)+Xe
    y1 = -L/2*math.sin(Angle)+Ye
    z1 = Ze
    stepcut.StepCut_Leg2(x0,y0,z0,x1,y1,z1,i,step,date)


def straight_h_Leg1(L,A1,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xf
    y0 = L/2*math.sin(Angle)+Yf
    z0 = Zf
    x1 = -L/2*math.cos(Angle)+Xf
    y1 = -L/2*math.sin(Angle)+Yf
    z1 = Zf
    stepcut.StepCut_Leg1(x0,y0,z0,x1,y1,z1,i,step,date)


def straightLeg_h(Length,dir,time):
    step = 8
    for i in range(0,17):
        date = bytearray(b'\x55\x55\x3B\x03\x12')
        date.extend(Uart.AddTime(65))
        straight_h_Leg1(Length,dir,i,step,date)
        straight_h_Leg2(Length,dir,i,step,date)
        straight_h_Leg3(Length,dir,i,step,date)
        straight_h_Leg4(Length,dir,i,step,date)
        straight_h_Leg5(Length,dir,i,step,date)
        straight_h_Leg6(Length,dir,i,step,date)
        Uart.SendDate(date)
        #time.sleep(0.065)
        #print(date)
        #print('\n')
