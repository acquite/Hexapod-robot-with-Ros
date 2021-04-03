#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Curve 
import straight
import straightLink
import time 
import Uart
import serial

while True:
    #time.sleep(0.5)
    straightLink.straightLeg_Link(-60,90,1000)
    #time.sleep(0.5)
    straight.straightLeg(-60,90,1000)
