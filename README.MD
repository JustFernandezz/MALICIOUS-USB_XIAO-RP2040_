# ⚠️ DO NOT PLUG IN! ⚠️

![DANGER](https://img.shields.io/badge/DO%20NOT%20PLUG%20IN!-DANGER-red?style=for-the-badge)

> **This device is dangerous. Do not connect to power or any data ports.**  
> Unauthorized use may cause data loss, system compromise, or physical harm.

---

![XIAO RP2040](Images/xiao.jpeg)
![XIAO RP2040 Pins](Images/xiao_rp2040_pins.png)

# XIAO RP2040 MALICIOUS DRIVE

Hello guys, I go by the name **Fernandez**, but you can call me **CyberInkuei** 🥷😎  
This project is a **Bad USB simulation** built to showcase how simple-looking devices can become powerful tools for security testing, awareness, and defense.

The **Bad USB** functions as a **Human Interface Device (HID)**, allowing it to emulate a keyboard and execute keystrokes on a computer within seconds. While this capability is often abused for malicious purposes, it also makes Bad USB devices valuable tools for **security research, awareness, and attack simulation**.

For this project, we’ll be using the **XIAO RP2040** microcontroller as the foundation of our Bad USB build, which will be programmed using **CircuitPython**.

You can purchase the board from:
- [Seeed Studio](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html)
- [Microscale (Nigeria)](https://www.microscale.net/)

---

## Requirements

- XIAO RP2040
- A dedicated server (local system or hosted in the cloud)

I already have a dedicated server hosted in the cloud, which provides a public IP address and allows targets to connect from anywhere in the world. Some configuration is required, which will be covered later.

---

## Goal

The goal of this project is to:
- Exfiltrate Wi-Fi SSIDs and passwords
- Inject a backdoor to obtain a remote shell
- Schedule the backdoor as a task for persistence
- Disable Windows Defender

---

## Scripts

I wrote two scripts for similar purposes.

### `Base_run.py`
[View script](https://github.com/JustFernandezz/MALICIOUS-USB_XIAO-RP2040_/blob/main/Base_run.py)

- Exfiltrates Wi-Fi SSIDs and passwords
- Injects a backdoor for a remote shell
- Schedules persistence via task scheduler
- Opens a YouTube video as a distraction

### `uac_defender.py`
[View script](https://github.com/JustFernandezz/MALICIOUS-USB_XIAO-RP2040_/blob/main/uac_defender.py)

- Opens PowerShell with admin privileges
- Exfiltrates Wi-Fi SSIDs and passwords
- Injects a backdoor for a remote shell
- Schedules persistence
- Accepts UAC prompts and disables Windows Defender

The scripts are similar, but `uac_defender.py` includes UAC handling and Defender disablement.

---

## Setup

Navigate to [CircuitPython](https://circuitpython.org), select **Downloads**, and search for **XIAO RP2040**.


