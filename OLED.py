#!/usr/bin/env python
# coding=utf-8

import os
from lib_oled96 import ssd1306
from smbus import SMBus
from PIL import ImageFont
import time


def getCpuTemperature():
 tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
 cpu_temp = tempFile.read()
 tempFile.close()
 return float(cpu_temp)/1000

def get_RAM_usage():
  mem=str(os.popen('free -t -m').readlines())
  T_ind=mem.index('T')
  mem_G=mem[T_ind+14:-4]
  S1_ind=mem_G.index(' ')
  mem_T=mem_G[0:S1_ind]
  mem_G1=mem_G[S1_ind+8:]
  S2_ind=mem_G1.index(' ')
  mem_U=mem_G1[0:S2_ind]
  mem_F=mem_G1[S2_ind+8:]
  k=(int((100/int(mem_G[:5]))*(int(mem_F[8:]))))
  i=100-k
  return i

i2cbus = SMBus(1)            # 0 = Raspberry Pi 1, 1 = Raspberry Pi > 1
oled = ssd1306(i2cbus)
draw = oled.canvas
DejaVuSans30 = ImageFont.truetype('FreeSans.ttf', 15)

oled.cls()
oled.display()
y=0
j=0
CPU_temp_before=0
RAM_usage_before
time.sleep(60)

while True:
 RAM_usage=get_RAM_usage()
 CPU_temp=int(getCpuTemperature())
 bash_status=str(os.popen('systemctl status hornet').readlines())
 index=bash_status.index("Active")
 status=bash_status[index+8:index+14]
 if (status == "active"):
         node_status="Online"
 else:
         node_status="Offline"


 if CPU_temp!=CPU_temp_before or RAM_usage!=RAM_usage_before:
     oled.cls()
     draw.text((30, 10), "CPU: " + str(CPU_temp)+"°C", font=DejaVuSans30,fill=1)
     draw.text((30, 28), "RAM: " + str(RAM_usage) + "%", font=DejaVuSans30,fill=1)
     draw.text((30, 46), "Status: " + node_status, font=DejaVuSans30,fill=1)

     oled.display()
     time.sleep(1)
     CPU_temp_before=CPU_temp
     RAM_usage_before=RAM_usage
 else:
     time.sleep(1)
