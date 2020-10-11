import Curve 
import straight 
import time 
import Uart
import serial

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
        straight.straightLeg(100,135,1000)
        TempS = input()
    if TempS[-1] in ['9']:
        straight.straightLeg(100,45,1000)
        TempS = input()
    if TempS[-1] in ['1']:
        straight.straightLeg(-100,225,1000)
        TempS = input()
    if TempS[-1] in ['3']:
        straight.straightLeg(-100,315,1000)
        TempS = input()
    if TempS[-1] in ['5']:
        Curve.CurveLeg(0,20,1000)
        TempS = input()
