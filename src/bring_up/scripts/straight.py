import stepcut
import math
import Uart
import serial

Xa,Ya,Za = -175,  230, -77
Xb,Yb,Zb = -270,  0,   -77
Xc,Yc,Zc = -175, -230, -77
Xd,Yd,Zd =  175, -230, -77
Xe,Ye,Ze =  270,  0,   -77
Xf,Yf,Zf =  175,  230, -77

ser=serial.Serial('/dev/ttyUSB0',9600)
#ser=serial.Serial('/dev/ttyACM0',9600)


def straight_Leg1(L,A1,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xa
    y0 = L/2*math.sin(Angle)+Ya
    z0 = Za
    x1 = -L/2*math.cos(Angle)+Xa
    y1 = -L/2*math.sin(Angle)+Ya
    z1 = Za
    stepcut.StepCut_Leg1(x0,y0,z0,x1,y1,z1,i,step,date)


def straight_Leg2(L,A1,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xb
    y0 = L/2*math.sin(Angle)+Yb
    z0 = Zb
    x1 = -L/2*math.cos(Angle)+Xb
    y1 = -L/2*math.sin(Angle)+Yb
    z1 = Zb
    stepcut.StepCut_Leg2(x0,y0,z0,x1,y1,z1,i,step,date)


def straight_Leg3(L,A1,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xc
    y0 = L/2*math.sin(Angle)+Yc
    z0 = Zc
    x1 = -L/2*math.cos(Angle)+Xc
    y1 = -L/2*math.sin(Angle)+Yc
    z1 = Zc
    stepcut.StepCut_Leg3(x0,y0,z0,x1,y1,z1,i,step,date)


def straight_Leg4(L,A1,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xd
    y0 = L/2*math.sin(Angle)+Yd
    z0 = Zd
    x1 = -L/2*math.cos(Angle)+Xd
    y1 = -L/2*math.sin(Angle)+Yd
    z1 = Zd
    stepcut.StepCut_Leg4(x0,y0,z0,x1,y1,z1,i,step,date)


def straight_Leg5(L,A1,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xe
    y0 = L/2*math.sin(Angle)+Ye
    z0 = Ze
    x1 = -L/2*math.cos(Angle)+Xe
    y1 = -L/2*math.sin(Angle)+Ye
    z1 = Ze
    stepcut.StepCut_Leg5(x0,y0,z0,x1,y1,z1,i,step,date)


def straight_Leg6(L,A1,i,step,date):
    Angle = A1/180*math.pi
    x0 = L/2*math.cos(Angle)+Xf
    y0 = L/2*math.sin(Angle)+Yf
    z0 = Zf
    x1 = -L/2*math.cos(Angle)+Xf
    y1 = -L/2*math.sin(Angle)+Yf
    z1 = Zf
    stepcut.StepCut_Leg6(x0,y0,z0,x1,y1,z1,i,step,date)


def straightLeg_1(Length,dir,time):
    step = 15
    for i in range(1,16):
        date = bytearray(b'\x55\x55\x3B\x03\x12')
        date.extend(Uart.AddTime(65))
        straight_Leg1(Length,dir,i,step,date)
        straight_Leg2(Length,dir,i,step,date)
        straight_Leg3(Length,dir,i,step,date)
        straight_Leg4(Length,dir,i,step,date)
        straight_Leg5(Length,dir,i,step,date)
        straight_Leg6(Length,dir,i,step,date)
        ser.write(date)
        #time.sleep(0.065)
        #print(date)
        #print('\n')

def straightLeg_2(Length,dir,time):
    step = 15
    for i in range(16,31):
        date = bytearray(b'\x55\x55\x3B\x03\x12')
        date.extend(Uart.AddTime(65))
        straight_Leg1(Length,dir,i,step,date)
        straight_Leg2(Length,dir,i,step,date)
        straight_Leg3(Length,dir,i,step,date)
        straight_Leg4(Length,dir,i,step,date)
        straight_Leg5(Length,dir,i,step,date)
        straight_Leg6(Length,dir,i,step,date)
        ser.write(date)
