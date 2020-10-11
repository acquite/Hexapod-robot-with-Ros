import math
import stepdrive

def StepCut_Leg1_Link(x0,y0,z0,x1,y1,z1,tx,ty,tz,s,step,date):
    H = 50
    if (s<=step):
        x = (x1-tx)/step*s + tx
        y = (y1-ty)/step*s + ty
        z = (z1-tz)/step*s + tz
        stepdrive.InverseKinematics_Leg1(x,y,z,date)
    else:
        x = (x0-x1)/step*(s-step) + x1
        y = (y0-y1)/step*(s-step) + y1
        z = (z0-z1)/step*(s-step) + z1 + (-H)*4/(step*step)*(s-step)*(s-2*step)
        stepdrive.InverseKinematics_Leg1(x,y,z,date)


def StepCut_Leg2_Link(x0,y0,z0,x1,y1,z1,tx,ty,tz,s,step,date):
    H = 50
    if (s<=step):
        x = (x0-tx)/step*s + tx
        y = (y0-ty)/step*s + ty
        z = (z0-tz)/step*s + tz + (-H)*4/(step*step)*(s-step)*s
        stepdrive.InverseKinematics_Leg2(x,y,z,date)
    else:
        x = (x1-x0)/step*(s-step) + x0
        y = (y1-y0)/step*(s-step) + y0
        z = (z1-z0)/step*(s-step) + z0
        stepdrive.InverseKinematics_Leg2(x,y,z,date)


def StepCut_Leg3_Link(x0,y0,z0,x1,y1,z1,tx,ty,tz,s,step,date):
    H = 50
    if (s<=step):
        x = (x1-tx)/step*s + tx
        y = (y1-ty)/step*s + ty
        z = (z1-tz)/step*s + tz
        stepdrive.InverseKinematics_Leg3(x,y,z,date)
    else:
        x = (x0-x1)/step*(s-step) + x1
        y = (y0-y1)/step*(s-step) + y1
        z = (z0-z1)/step*(s-step) + z1 + (-H)*4/(step*step)*(s-step)*(s-2*step)
        stepdrive.InverseKinematics_Leg3(x,y,z,date)


def StepCut_Leg4_Link(x0,y0,z0,x1,y1,z1,tx,ty,tz,s,step,date):
    H = 50
    if (s<=step):
        x = (x0-tx)/step*s + tx
        y = (y0-ty)/step*s + ty
        z = (z0-tz)/step*s + tz + (-H)*4/(step*step)*(s-step)*s
        stepdrive.InverseKinematics_Leg4(x,y,z,date)
    else:
        x = (x1-x0)/step*(s-step) + x0
        y = (y1-y0)/step*(s-step) + y0
        z = (z1-z0)/step*(s-step) + z0
        stepdrive.InverseKinematics_Leg4(x,y,z,date)



def StepCut_Leg5_Link(x0,y0,z0,x1,y1,z1,tx,ty,tz,s,step,date):
    H = 50
    if (s<=step):
        x = (x1-tx)/step*s + tx
        y = (y1-ty)/step*s + ty
        z = (z1-tz)/step*s + tz
        stepdrive.InverseKinematics_Leg5(x,y,z,date)
    else:
        x = (x0-x1)/step*(s-step) + x1
        y = (y0-y1)/step*(s-step) + y1
        z = (z0-z1)/step*(s-step) + z1 + (-H)*4/(step*step)*(s-step)*(s-2*step)
        stepdrive.InverseKinematics_Leg5(x,y,z,date)


def StepCut_Leg6_Link(x0,y0,z0,x1,y1,z1,tx,ty,tz,s,step,date):
    H = 50
    if (s<=step):
        x = (x0-tx)/step*s + tx
        y = (y0-ty)/step*s + ty
        z = (z0-tz)/step*s + tz + (-H)*4/(step*step)*(s-step)*s
        stepdrive.InverseKinematics_Leg6(x,y,z,date)
    else:
        x = (x1-x0)/step*(s-step) + x0
        y = (y1-y0)/step*(s-step) + y0
        z = (z1-z0)/step*(s-step) + z0
        stepdrive.InverseKinematics_Leg6(x,y,z,date)