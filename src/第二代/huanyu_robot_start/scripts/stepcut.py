#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import stepdrive

def StepCut_Leg1(x0,y0,z0,x1,y1,z1,s,step,date):
    H = 60
    if (s<=step):
        x = (x1-x0)/step*s + x0
        y = (y1-y0)/step*s + y0
        z = (z1-z0)/step*s + z0
        stepdrive.InverseKinematics_Leg1(x,y,z,date)
    else:
        x = (x0-x1)/step*(s-step) + x1
        y = (y0-y1)/step*(s-step) + y1
        z = (z0-z1)/step*(s-step) + z1 + (-H)*4/(step*step)*(s-step)*(s-2*step)
        stepdrive.InverseKinematics_Leg1(x,y,z,date)


def StepCut_Leg2(x0,y0,z0,x1,y1,z1,s,step,date):
    H = 60
    if (s<=step):
        x = (x0-x1)/step*s + x1
        y = (y0-y1)/step*s + y1
        z = (z0-z1)/step*s + z1 + (-H)*4/(step*step)*(s-step)*s
        stepdrive.InverseKinematics_Leg2(x,y,z,date)
    else:
        x = (x1-x0)/step*(s-step) + x0
        y = (y1-y0)/step*(s-step) + y0
        z = (z1-z0)/step*(s-step) + z0
        stepdrive.InverseKinematics_Leg2(x,y,z,date)


def StepCut_Leg3(x0,y0,z0,x1,y1,z1,s,step,date):
    H = 60
    if (s<=step):
        x = (x1-x0)/step*s + x0
        y = (y1-y0)/step*s + y0
        z = (z1-z0)/step*s + z0
        stepdrive.InverseKinematics_Leg3(x,y,z,date)
    else:
        x = (x0-x1)/step*(s-step) + x1
        y = (y0-y1)/step*(s-step) + y1
        z = (z0-z1)/step*(s-step) + z1 + (-H)*4/(step*step)*(s-step)*(s-2*step)
        stepdrive.InverseKinematics_Leg3(x,y,z,date)


def StepCut_Leg4(x0,y0,z0,x1,y1,z1,s,step,date):
    H = 60
    if (s<=step):
        x = (x0-x1)/step*s + x1
        y = (y0-y1)/step*s + y1
        z = (z0-z1)/step*s + z1 + (-H)*4/(step*step)*(s-step)*s
        stepdrive.InverseKinematics_Leg4(x,y,z,date)
    else:
        x = (x1-x0)/step*(s-step) + x0
        y = (y1-y0)/step*(s-step) + y0
        z = (z1-z0)/step*(s-step) + z0
        stepdrive.InverseKinematics_Leg4(x,y,z,date)



def StepCut_Leg5(x0,y0,z0,x1,y1,z1,s,step,date):
    H = 60
    if (s<=step):
        x = (x1-x0)/step*s + x0
        y = (y1-y0)/step*s + y0
        z = (z1-z0)/step*s + z0
        stepdrive.InverseKinematics_Leg5(x,y,z,date)
    else:
        x = (x0-x1)/step*(s-step) + x1
        y = (y0-y1)/step*(s-step) + y1
        z = (z0-z1)/step*(s-step) + z1 + (-H)*4/(step*step)*(s-step)*(s-2*step)
        stepdrive.InverseKinematics_Leg5(x,y,z,date)


def StepCut_Leg6(x0,y0,z0,x1,y1,z1,s,step,date):
    H = 60
    if (s<=step):
        x = (x0-x1)/step*s + x1
        y = (y0-y1)/step*s + y1
        z = (z0-z1)/step*s + z1 + (-H)*4/(step*step)*(s-step)*s
        stepdrive.InverseKinematics_Leg6(x,y,z,date)
    else:
        x = (x1-x0)/step*(s-step) + x0
        y = (y1-y0)/step*(s-step) + y0
        z = (z1-z0)/step*(s-step) + z0
        stepdrive.InverseKinematics_Leg6(x,y,z,date)
