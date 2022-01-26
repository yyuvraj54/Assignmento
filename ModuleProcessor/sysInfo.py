import sys
def getSystemOS():
    if sys.platform.startswith('linux'):
        return "Linux"
    elif sys.platform.startswith('darwin'):
        return "MacOs"
    elif sys.platform.startswith('win32'):
        return "Windows"
