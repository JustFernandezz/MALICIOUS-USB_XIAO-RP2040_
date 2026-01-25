# ⚠️ **DO NOT PLUG IN!** ⚠️

![DANGER](https://img.shields.io/badge/DO%20NOT%20PLUG%20IN!-DANGER-red?style=for-the-badge&logo=warning)
> **This device is dangerous. Do not connect to power or any data ports.**  
> Unauthorized use may cause data loss, system compromise, or physical harm.


![Alt text](Images/xiao.jpeg)
![Alt text](Images/xiao_rp2040_pins.png)

# XIAO RP2040 MALICIOUS DRIVE #

Hello guys, I go by the name Fernandez, but you can call me CyberInkuei 🥷😎.
This project is a BAD USB simulation built to showcase how simple-looking devices can become powerful tools for security testing, awareness, and defense.

The Bad USB functions as a Human Interface Device (HID), allowing it to emulate a keyboard and execute keystrokes on a computer within seconds. While this capability is often abused for malicious purposes, it also makes Bad USB devices valuable tools for security research, awareness, and attack simulation.

For this project, we’ll be using the XIAO RP2040 microcontroller as the foundation of our Bad USB build, which will be programmed using CircuitPython. You can purchase the board from
👉 <a href="https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html?srsltid=AfmBOop0VZ_jHX3hqeEwixS7_KCj41w8qmIfnBCEUeNWxq647FOvcWkS">Seeed Studio</a>
or
👉 <a href="https://www.microscale.net/?srsltid=AfmBOoooYjyeR2MXf-PNIm0P0SWP6HJNdi7z7AktNsc88h1k5MQf68Tw">Microscale</a> (for those based in Nigeria).

# Requirement #
<li>XIAO RP2040</li>
<li>A dedicated Server(Local system or hosted in the cloud) </li>


I already have a dedicated server hosted in the cloud which gives me a public IP address and allows the targets connect to me from anywhere in the world, but requires some configuration which I'm going to show you.

# Goal #

The goal of this project is to:
- Exfiltrate every wifi ssid and password from the victim's machine and forward it to our server
- Inject a backdoor that gives us a remote shell
- Schedule the backdoor to run as a task on the victim's machine to maintain persistence almost forever
- Lastly, disable windows defender.

# Scripts #
I wrote two different scripts for almost the samething. <a href="https://github.com/JustFernandezz/MALICIOUS-USB_XIAO-RP2040_/blob/main/Base_run.py">Base_run.py</a> does the following:
- Exfiltrates every wifi ssid and password from the victim's machine and forward it to our server
- Injects a backdoor that gives us a remote shell
- Schedules the backdoor to run as a task on the victim's machine to maintain persistence almost forever.
- Opens a youtube video on the browser for distraction

While <a href="https://github.com/JustFernandezz/MALICIOUS-USB_XIAO-RP2040_/blob/main/uac_defender.py">uac_defender.py</a> does the following:
- Opens powershell as admin and exfiltrates every wifi ssid and password from the victim's machine and forward it to our server
- Inject a backdoor that gives us a remote shell
- Schedule the backdoor to run as a task on the victim's machine to maintain persistence almost forever
- Accepts UAC and Disables windows defender.

They are similar, just that the <a href="https://github.com/JustFernandezz/MALICIOUS-USB_XIAO-RP2040_/blob/main/uac_defender.py">uac_defender.py</a> is capable of accepting uac and disabling windows defender.

Let's get started, shall we?

# Setup #
Navigate to <a href="https://circuitpython.org">Circuit_Python</a>, select Downloads and search for "xiao rp2040"
