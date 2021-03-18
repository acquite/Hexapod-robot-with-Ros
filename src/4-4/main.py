import time
import serial

import Curve 
import straight 
import Curve_h
import straight_h
import shrinkage
import Swing
 
import Uart
import stepdrive as IK

def Robot_Init():
    x1 = 200
    y1 = 240
    z1 = -130
    x2 = 250
    y2 = 0
    date = bytearray(b'\x55\x55\x3B\x03\x12')
    date.extend(Uart.AddTime(65))
    IK.InverseKinematics_Leg1( x1, y1, z1,date)
    IK.InverseKinematics_Leg2( x2, y2, z1,date)
    IK.InverseKinematics_Leg3( x1,-y1, z1,date)
    IK.InverseKinematics_Leg4(-x1, y1, z1,date)
    IK.InverseKinematics_Leg5(-x2, y2, z1,date)
    IK.InverseKinematics_Leg6(-x1,-y1, z1,date)
    Uart.SendDate(date)
    time.sleep(0.5)

'''
def Move():
    Swing.Swing_Leg1(80,90)
    Swing.translation(80,6,90)
    Swing.Swing_Leg2(80,90)
    Swing.translation(80,6,90)
    Swing.Swing_Leg2(80,90)
    Swing.translation(80,6,90)
    Swing.Swing_Leg3(80,90)
    Swing.translation(80,6,90)
    Swing.Swing_Leg4(80,90)
    Swing.translation(80,6,90)
    Swing.Swing_Leg5(80,90)
    Swing.translation(80,6,90)
    Swing.Swing_Leg6(80,90)
    Swing.translation(80,6,90)
'''
Robot_Init()
time.sleep(1)
#straight_h.robot_stand()
TempS = input()
while TempS[-1] not in ['N','n']:
    if TempS[-1] in ['8']:
        straight.straightLeg(100,90,1000)
        TempS = input()
    if TempS[-1] in ['2']:
        straight.straightLeg(-100,90,1000)
        TempS = input()
    if TempS[-1] in ['4']:
        shrinkage.shrinkageLeg(60,1000)
        TempS = input()
    if TempS[-1] in ['6']:
        straight.straightLeg(60,0,1000)
        TempS = input()
    if TempS[-1] in ['7']:
        Curve.CurveLeg(-300,8,1000)
        TempS = input()
    if TempS[-1] in ['9']:
        Curve.CurveLeg(300,8,1000)
        TempS = input()
    if TempS[-1] in ['1']:
        Curve.CurveLeg(-300,-8,1000)
        TempS = input()
    if TempS[-1] in ['3']:
        Curve.CurveLeg(300,-8,1000)
        TempS = input()
    if TempS[-1] in ['5']:
        Curve.CurveLeg(0,20,1000)
        TempS = input()
    if TempS[-1] in ['0']:
        Curve.CurveLeg(0,-20,1000)
        TempS = input()
    if TempS[-1] in ['h']:
        straight_h.straightLeg_h(60,0,1000)
        TempS = input()

