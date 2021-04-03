#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Globle_Pos as GP
import stepdrive as IK
import math

PI = 3.14
H = 80
He = [0,0.3,0.6,0.8,1,1,1,1,1,1,1,1,1,1,1,1,0.3]
Index1 = 1
date = []

#Leg4
Xa,Ya,Za = -165,  215, -95

#Leg5
Xb,Yb,Zb = -245,  0,   -95

#Leg6
Xc,Yc,Zc = -165, -215, -95

#Leg3
Xd,Yd,Zd =  165, -215, -95

#Leg2
Xe,Ye,Ze =  245,  0,   -95

#Leg1
Xf,Yf,Zf =  165,  215, -95

def Test_Gait(L,A): 
    angle = A/180*PI

    for i in range(17):
        x4 = Xa + i*(L*math.cos(angle))/16
        y4 = Ya + i*(L*math.sin(angle))/16
        z4 = Za + H*He[i]

        GP.Leg4_Pos[0] = x4
        GP.Leg4_Pos[1] = y4
        GP.Leg4_Pos[2] = z4

        IK.InverseKinematics_Leg4(x4,y4,z4,date)
        #MOVE1

        if (Index1 == 0):
            break
    
    for i in range(17):
        x1 = Xf + i*(L*math.cos(angle))/16
        y1 = Yf + i*(L*math.sin(angle))/16
        z1 = Zf + H*He[i]

        GP.Leg1_Pos[0] = x1
        GP.Leg1_Pos[1] = y1
        GP.Leg1_Pos[2] = z1

        IK.InverseKinematics_Leg1(x1,y1,z1,date)
        #MOVE1

        if (Index1 == 0):
            break

    if (GP.Leg4_Pos[2] > Za):
        q = Za - GP.Leg4_Pos[2]
        GP.Leg4_Pos[2] = Za
        GP.Leg1_Pos[2] = GP.Leg1_Pos[2]-q*((GP.Leg1_Pos[1]+155)/(GP.Leg4_Pos[1]+155))
        GP.Leg2_Pos[2] = GP.Leg2_Pos[2]-q*((155)/(GP.Leg4_Pos[1]+155))
        GP.Leg5_Pos[2] = GP.Leg5_Pos[2]-q*((155)/(GP.Leg4_Pos[1]+155))
        IK.InverseKinematics_Leg1(GP.Leg1_Pos[0],GP.Leg1_Pos[1],GP.Leg1_Pos[2],date)
        IK.InverseKinematics_Leg2(GP.Leg2_Pos[0],GP.Leg2_Pos[1],GP.Leg2_Pos[2],date)
        IK.InverseKinematics_Leg4(GP.Leg4_Pos[0],GP.Leg4_Pos[1],GP.Leg4_Pos[2],date)
        IK.InverseKinematics_Leg5(GP.Leg5_Pos[0],GP.Leg5_Pos[1],GP.Leg5_Pos[2],date)
        #MOVE

    x1 = GP.Leg1_Pos[0] - L/3*math.cos(angle)
    y1 = GP.Leg1_Pos[1] - L/3*math.sin(angle)
    z1 = GP.Leg1_Pos[2]

    x2 = GP.Leg2_Pos[0] - L/3*math.cos(angle)
    y2 = GP.Leg2_Pos[1] - L/3*math.sin(angle)
    z2 = GP.Leg2_Pos[2] 

    x3 = GP.Leg3_Pos[0] - L/3*math.cos(angle)
    y3 = GP.Leg3_Pos[1] - L/3*math.sin(angle)
    z3 = GP.Leg3_Pos[2]

    x4 = GP.Leg4_Pos[0] - L/3*math.cos(angle)
    y4 = GP.Leg4_Pos[1] - L/3*math.sin(angle)
    z4 = GP.Leg4_Pos[2]

    x5 = GP.Leg5_Pos[0] - L/3*math.cos(angle)
    y5 = GP.Leg5_Pos[1] - L/3*math.sin(angle)
    z5 = GP.Leg5_Pos[2]

    x6 = GP.Leg6_Pos[0] - L/3*math.cos(angle)
    y6 = GP.Leg6_Pos[1] - L/3*math.sin(angle)
    z6 = GP.Leg6_Pos[2]

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

    for i in range(17):
        x5 = Xb + i*(L*math.cos(angle))/16
        y5 = Yb + i*(L*math.sin(angle))/16
        z5 = Zb + H*He[i]

        GP.Leg5_Pos[0] = x5
        GP.Leg5_Pos[1] = y5
        GP.Leg5_Pos[2] = z5

        #MOVE1

        if (Index1 == 0):
            break
    
    for i in range(17):
        x2 = Xe + i*(L*math.cos(angle))/16
        y2 = Ye + i*(L*math.sin(angle))/16
        z2 = Ze + H*He[i]

        GP.Leg2_Pos[0] = x2
        GP.Leg2_Pos[1] = y2
        GP.Leg2_Pos[2] = z2
        #MOVE1

    x1 = GP.Leg1_Pos[0] - L/3*math.cos(angle)
    y1 = GP.Leg1_Pos[1] - L/3*math.sin(angle)
    z1 = GP.Leg1_Pos[2]

    x2 = GP.Leg2_Pos[0] - L/3*math.cos(angle)
    y2 = GP.Leg2_Pos[1] - L/3*math.sin(angle)
    z2 = GP.Leg2_Pos[2] 

    x3 = GP.Leg3_Pos[0] - L/3*math.cos(angle)
    y3 = GP.Leg3_Pos[1] - L/3*math.sin(angle)
    z3 = GP.Leg3_Pos[2]

    x4 = GP.Leg4_Pos[0] - L/3*math.cos(angle)
    y4 = GP.Leg4_Pos[1] - L/3*math.sin(angle)
    z4 = GP.Leg4_Pos[2]

    x5 = GP.Leg5_Pos[0] - L/3*math.cos(angle)
    y5 = GP.Leg5_Pos[1] - L/3*math.sin(angle)
    z5 = GP.Leg5_Pos[2]

    x6 = GP.Leg6_Pos[0] - L/3*math.cos(angle)
    y6 = GP.Leg6_Pos[1] - L/3*math.sin(angle)
    z6 = GP.Leg6_Pos[2]

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

    for i in range(17):
        x6 = Xc + i*(L*math.cos(angle))/16
        y6 = Yc + i*(L*math.sin(angle))/16
        z6 = Zc + H*He[i]

        GP.Leg6_Pos[0] = x6
        GP.Leg6_Pos[1] = y6
        GP.Leg6_Pos[2] = z6

        #MOVE1

        if (Index1 == 0):
            break
    
    for i in range(17):
        x3 = Xd + i*(L*math.cos(angle))/16
        y3 = Yd + i*(L*math.sin(angle))/16
        z3 = Zd + H*He[i]

        GP.Leg3_Pos[0] = x3
        GP.Leg3_Pos[1] = y3
        GP.Leg3_Pos[2] = z3
        #MOVE1

Test_Gait(60,90)