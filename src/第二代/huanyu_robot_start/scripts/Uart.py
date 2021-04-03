#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time 

ser=serial.Serial('/dev/ttyUSB1',9600)
#ser=serial.Serial('/dev/ttyACM0',9600)

def Cmd_Servo_Move(id,angle=None):
    buf = bytearray(b'')
    try:
        buf.extend([(0xff & id)])
        buf.extend([(0xff & angle), (0xff & (angle >> 8))])
    except Exception as e:
        print(e)
    return buf

def AddTime(time=None):
    buf = bytearray(b'')
    try:
        buf.extend([(0xff & time), (0xff & (time >> 8))])
    except Exception as e:
        print(e)
    return buf

def RandAngle(Q11,Q12,Q13,Q21,Q22,Q23,Q31,Q32,Q33,Q41,Q42,Q43,Q51,Q52,Q53,Q61,Q62,Q63):
    buf = bytearray(b'\x55\x55\x15\x15\x12\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10\x11\x12')
    ser.write(buf)
    time.sleep(0.25)
    count = ser.inWaiting()
    recv_data = ser.read(count)
    Q11 = 0xffff & (recv_data[6]  | (0xff00 & (recv_data[7]  << 8)))
    Q12 = 0xffff & (recv_data[9]  | (0xff00 & (recv_data[10] << 8)))
    Q13 = 0xffff & (recv_data[12] | (0xff00 & (recv_data[13] << 8)))
    Q21 = 0xffff & (recv_data[15] | (0xff00 & (recv_data[16] << 8)))
    Q22 = 0xffff & (recv_data[18] | (0xff00 & (recv_data[19] << 8)))
    Q23 = 0xffff & (recv_data[21] | (0xff00 & (recv_data[22] << 8)))
    Q31 = 0xffff & (recv_data[24] | (0xff00 & (recv_data[25] << 8)))
    Q32 = 0xffff & (recv_data[27] | (0xff00 & (recv_data[28] << 8)))
    Q33 = 0xffff & (recv_data[30] | (0xff00 & (recv_data[31] << 8)))
    Q41 = 0xffff & (recv_data[33] | (0xff00 & (recv_data[34] << 8)))
    Q42 = 0xffff & (recv_data[36] | (0xff00 & (recv_data[37] << 8)))
    Q43 = 0xffff & (recv_data[39] | (0xff00 & (recv_data[40] << 8)))
    Q51 = 0xffff & (recv_data[42] | (0xff00 & (recv_data[43] << 8)))
    Q52 = 0xffff & (recv_data[45] | (0xff00 & (recv_data[46] << 8)))
    Q53 = 0xffff & (recv_data[48] | (0xff00 & (recv_data[49] << 8)))
    Q61 = 0xffff & (recv_data[51] | (0xff00 & (recv_data[52] << 8)))
    Q62 = 0xffff & (recv_data[54] | (0xff00 & (recv_data[55] << 8)))
    Q63 = 0xffff & (recv_data[57] | (0xff00 & (recv_data[58] << 8)))
