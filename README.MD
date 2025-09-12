# ⚠️ **DO NOT PLUG IN!** ⚠️

![DANGER](https://img.shields.io/badge/DO%20NOT%20PLUG%20IN!-DANGER-red?style=for-the-badge&logo=warning)
> **This device is dangerous. Do not connect to power or any data ports.**  
> Unauthorized use may cause data loss, system compromise, or physical harm.


![Alt text](Images/xiao.jpeg)
![Alt text](Images/xiao_rp2040_pins.png)

Welcome!

The scripts above were written to perform the same function, but in two different scenarios.

<a href="https://github.com/Fernandez99fc/BAD-USB-XIAO-RP2040-/blob/main/Admin_RevShell.py">Admin_RevShell</a> is capable of the following:

- running powershell as admin to execute the first instance of the payload.
- Capturing all wifi passwords and logs it to a remote server
- Scheduling a reverse shell as a task that runs every 5 minutes on the victim's system.
- Bypasses UAC and disables windows Defender

While <a href="https://github.com/Fernandez99fc/BAD-USB-XIAO-RP2040-/blob/main/RevShell_Without_Admin.py">RevShell</a> runs the same script but excludes:
- running powershell as admin to execute the first instance of the payload(Instead, It runs as a normal user)
- Bypasses UAC and disables windows Defender.

This is suitable to use incase there's a UAC in place that requires a username and password, so it evades it and your script will run successfully.
