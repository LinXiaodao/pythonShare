import win32gui

def mian_window(width,height):
    exe_dow = win32gui.FindWindow('IEFrame',None)
    f = win32gui.MoveWindow(exe_dow, 0, 0, width, height,True)

mian_window(1920,846)