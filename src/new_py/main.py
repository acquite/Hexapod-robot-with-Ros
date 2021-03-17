#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import serial

import Curve 
import straight 
import Curve_h
import straight_h
import shrinkage
import stepdrive as IK

 
import Uart


def test():
    Xa = 130
    Ya = 130
    Za = -90
    Xb = 250
    Yb = 0
    date = bytearray(b'\x55\x55\x3B\x03\x12')
    date.extend(Uart.AddTime(65))
    IK.InverseKinematics_Leg1(Xa,Ya,Za,date)
    IK.InverseKinematics_Leg2(Xb,Yb,Za,date)
    IK.InverseKinematics_Leg3(Xa,-Ya,Za,date)
    IK.InverseKinematics_Leg4(-Xa,Ya,Za,date)
    IK.InverseKinematics_Leg5(-Xb,Yb,Za,date)
    IK.InverseKinematics_Leg6(-Xa,-Ya,Za,date)
    Uart.SendDate(date)


#test()


TempS = input()
while TempS[-1] not in ['N','n']:
    if TempS[-1] in ['8']:
        straight.straightLeg(100,90,1000)
        TempS = input()
    if TempS[-1] in ['2']:
        straight.straightLeg(-100,90,1000)
        TempS = input()
    if TempS[-1] in ['4']:
        straight.straightLeg(60,180,1000)
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

