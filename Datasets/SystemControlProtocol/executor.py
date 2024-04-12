# Volume Controls
def setVolume(vol):
    # Increase volume --> + 10%
    # Decrease volume --> - 10%
    # Mute volume --> 0%
    # Full sound --> 100%
    return None

# Brightness Controls
def setBrightness(qty):
    # Increase, Decrease, Min, Max
    return None

# Shutdown
def SystemDown(method):
    # Shut Down, Sleep, Restart
    return None

# Battery status
def batteryStats():
    # Charging % and mode (Balenced, Power Saving,...)
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