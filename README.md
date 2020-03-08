# Hornet_OLED

This is a Tutorial to upgrade your IOTA Hornet or GoShimmer Node with a little status monitor based on a 0,96" 128x64 OLED display showing temperature of the CPU, RAM usage and if your node is running or not.

You´ll need any Raspberry Pi running a hornet or GoShimmer node software, a 0,96" 128x64 OLED display (~7€) and four female-female jumper wires. If you own a 3D printer, STL files for a little display stand i designed can be found here ( Platzhalter).

Wiring diagram can be found here(https://indibit.de/wp-content/uploads/2018/04/rpi_oled_i2c_schaltung.png). 
!!!On some displays VCC and GND are reversed!!!

Navigate to your home directory by:

>cd /

>cd home

Then clone the github repository by:

>sudo git clone https://github.com/mrctln/Hornet_OLED

To choose your node type, go to

>cd Hornet_OLED

and then 

>sudo nano OLED.py

Change the **node_type** variable to *hornet* or *shimmer*.

By changing the **sleep_time** variable you can change the updating interval of the monitor in seconds.

To automatically start the script after rebooting:

>crontab -e

and copy

>@reboot cd/home/Hornet_OLED && sudo python OLED.py

at the end of the file. Save with CTRL+O and Enter and close it by Ctrl+X.
