#!/usr/bin/env python
# coding=utf-8
# Bibliotheken importieren
import os
from lib_oled96 import ssd1306
from smbus import SMBus
from PIL import ImageFont
import time

#Definitionen
def getCpuTemperature():
 tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
 cpu_temp = tempFile.read()
 tempFile.close()
 return float(cpu_temp)/1000
# Display einrichten
i2cbus = SMBus(1)            # 0 = Raspberry Pi 1, 1 = Raspberry Pi > 1
oled = ssd1306(i2cbus)
# Ein paar Abkürzungen, um den Code zu entschlacken
draw = oled.canvas
DejaVuSans30 = ImageFont.truetype('FreeSans.ttf', 15) #DejaVuSans #FreeSans
# Display zum Start löschen
oled.cls()
oled.display()
y=0

while True:
    
    #RAM-Auslastung
    mem=str(os.popen('free -t -m').readlines())
    T_ind=mem.index('T')
    mem_G=mem[T_ind+14:-4]
    S1_ind=mem_G.index(' ')
    mem_T=mem_G[0:S1_ind]
    mem_G1=mem_G[S1_ind+8:]
    S2_ind=mem_G1.index(' ')
    mem_U=mem_G1[0:S2_ind]

    mem_F=mem_G1[S2_ind+8:]
    
    x=int(getCpuTemperature())
    k=(int((100/int(mem_G[:5]))*(int(mem_F[8:]))))
    i=100-k
    if x!=y or i!=j:
        oled.cls()
        draw.text((30, 20), "CPU: " + str(x)+"°C", font=DejaVuSans30,fill=1)
        draw.text((30, 40), "RAM: " + str(i) + "%", font=DejaVuSans30,fill=1)
# Ausgaben auf Display schreiben
        oled.display()
        time.sleep(1)
        y=x
        j=i
    else:
        time.sleep(1)
