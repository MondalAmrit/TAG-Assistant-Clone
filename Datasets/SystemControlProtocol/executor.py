from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control, os, psutil

# Volume Controls
def setVolume(vol):
    # Increase volume --> + 10%
    # Decrease volume --> - 10%
    # Mute volume --> 0%
    # Full sound --> 100%
    # None = get volume
    device = AudioUtilities.GetSpeakers()
    
    interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    prevVol = volume.GetMasterVolumeLevelScalar()
    if not vol:
        print(f'Current Volume {prevVol*100:.0f}')
        return
    volume.SetMasterVolumeLevelScalar(max(0,min(1,vol/100)), None)
    currVol = volume.GetMasterVolumeLevelScalar()
    print(f'Increased Volume from {prevVol*100:.0f} to {currVol*100:.0f}')
    return None

# Brightness Controls
def setBrightness(qty):
    # Increase, Decrease, Min, Max, None = get the brightness
    prevVal = screen_brightness_control.get_brightness()[0]
    if not qty:
        print(f'Current Brightness {prevVal}')
        return
    screen_brightness_control.set_brightness(max(0,min(qty,100)))
    currVal = screen_brightness_control.get_brightness()[0]
    print(f'Changed brightness from {prevVal} to {currVal} ')
    return None

# Shutdown
def SystemDown(method):
    # Shut Down, Sleep, Restart, logout
    if method == 'shutdown':
        print('system is shutting down')
        os.system("shutdown /s /t 1") # 1 means 1 second delay
    elif method == 'restart':
        print('system is restarting')
        os.system("shutdown /r /t 1")
    elif method == 'logout':
        print('system is logging out')
        os.system("shutdown /l /t 1")
    else:   # sleep method
        print('system is going to sleep')
        os.system("shutdown /h")

# Battery status
def batteryStats(spec=None):
    # Charging % and mode (Balenced, Power Saving,...)
    battery = psutil.sensors_battery()
    if not spec:
        print('Battery Stats:')
        print(f'Charging left: {battery.percent}%')
        print(f'Battery Time Left(in secs):{battery.secsleft}')
        print(f'Charger plugged:{battery.power_plugged}')
    elif spec == 'battery':
        print(f'{battery.percent}%')
    elif spec == 'time':
        print(f'{battery.secsleft} (in secs)')
    elif spec == 'charger':
        print(battery.power_plugged)
    return None

# Wifi Controls
def toggleWifi(enable):
    # Enable, Disable
    return None

def getConnections(SSID):
    # Previous IP connections related to SSID or all by default
    return None

def forgetNetwork(SSID):
    return None

def connectNetwork(SSID, password=None):
    # If no password I.e. disconnect to that network
    return None

# Bluetooth Controls
def toggleBluetooth(enable):
    return None

def getDevices(state):
    # Paired devices or Connected devices
    return None

def connectDevice(name, connect_type = True):
    # connect_type = False --> Disconnect from bluetooth device specified
    return None

# Transfer files via bluetooth
def transferFiles(location, device):
    # The specified location can either be file or a folder
    return None

# Calendar Controls
def getCurrDateTime(inp_type = None):
    import datetime
    if not inp_type:    return datetime.datetime.now()
    elif inp_type == 'date':    return datetime.date.today()
    elif inp_type == 'time':    return datetime.time.isoformat()
    elif inp_type == 'zone':    return datetime.time.tzinfo
    elif inp_type == 'stamp':   return datetime.datetime.timestamp(datetime.time.isoformat())
    elif inp_type == 'day':     return datetime.datetime.isoweekday()
    elif inp_type == 'year':    return datetime.datetime.year

###########################
# Future Work
# CPU stats
# Virtual Memory
# Users ( in system )

# setBrightness(42)
# setVolume(72)
# SystemDown('sleep')
batteryStats()