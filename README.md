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

Navigate to [CircuitPython](https://circuitpython.org), select **Downloads**, and search for **XIAO RP2040**. and select the first one "RP2040"

<img width="1920" height="875" alt="Screenshot (59)" src="https://github.com/user-attachments/assets/64d9e929-46f9-4584-884b-fec0aa600928" />

Download the `.UF2` file
<img width="1920" height="955" alt="Screenshot (60)" src="https://github.com/user-attachments/assets/4914e0e9-6dfd-4baf-bf00-3dfe8a98a8a2" />

Now, it's time to plug in the board with a type c cable, but before that, hold the <b>B</b> button on the board for few seconds while at the same timme you plug in the device to the computer to factory reset it. The B button is located by the bottom right of the device in the image below
![XIAO RP2040](Images/xiao.jpeg)

After you have it plugged in, you should see it as a drive on your computer
<img width="1920" height="774" alt="Screenshot (61)" src="https://github.com/user-attachments/assets/12dc3070-2487-4145-858a-dbc1e7637e9d" />

Move the `adaruit.UF2` file we downloaded of recent to the drive. It is going to disconnect and restart itself after moving it.
<img width="1200" height="246" alt="Screenshot (62)" src="https://github.com/user-attachments/assets/7138cf57-3c98-4c13-a85d-85d4d16c33c2" />

After restarting, you would have something like this:
<img width="1747" height="796" alt="Screenshot (67)" src="https://github.com/user-attachments/assets/6b68389d-cc53-45a2-8cf8-c87e82cb9ec7" />

Next, go to the library file we downloaded `adafruit-circuitpython-bundle-10.x-mpy-20260124` and extract the content. Once you're done navigate to the `lib` directory in it and look for the folder `adafruit_hid` <img width="1725" height="854" alt="Screenshot (69)" src="https://github.com/user-attachments/assets/0f4516e5-572a-4148-96d8-aba22640a671" />

Then copy the folder to the lib directory in the XAIO RP2040 drive.
<img width="1912" height="819" alt="Screenshot (70)" src="https://github.com/user-attachments/assets/9edbda1f-ff17-47ff-a3ad-4b36fc21fd11" />

Going back to the root of the XAIO RP2040, you will see python script, this is where our code would be stored and that's where we do the programming. I have it programmed for you already, so you can just replace the python script with the one I've written and modify the ip address and anything that needs to modified to match your environment. Also make sure the script is renamed to `code.py`
<img width="1747" height="796" alt="Screenshot (67)" src="https://github.com/user-attachments/assets/6b68389d-cc53-45a2-8cf8-c87e82cb9ec7" />

Before we continue, let's see the config on the attacker server running in the cloud.

# Attacker Server #
We would like our attack to be successful irrespective of the network the target is on and wherever he is in the world. We don't want a situation whereby it only works when we are within the same network, therefore, I provisioned a server already in the cloud that listens for inbound and outbound connections with an available public IP Address.

You can come here [EC2 Server](https://us-east-1.console.aws.amazon.com/) to create a cloud Instance in AWS.

After creating an instance, navigate to security groups and configure an inbound allow rule for these ports and also an outbound for all ports

<img width="1618" height="298" alt="Screenshot (73)" src="https://github.com/user-attachments/assets/d06b2b8f-9f90-4a3b-b76b-8c5762766ef5" />

<img width="1628" height="278" alt="Screenshot (74)" src="https://github.com/user-attachments/assets/7fba9caa-05ca-4b9b-988e-ae7478acff4b" />

<img width="1649" height="235" alt="Screenshot (75)" src="https://github.com/user-attachments/assets/1b3d0854-d030-41be-bec2-5b0c9179c640" />



