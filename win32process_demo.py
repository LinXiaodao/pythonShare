import win32api

# 获取显示器
devices = win32api.EnumDisplayDevices(None, 0, 0)

# 获取显示器的设备信息
dev_mode = win32api.EnumDisplaySettings(devices.DeviceName, 0)

print("显示器 %s 的宽度是 %s ,高度是 %s" %(devices.DeviceName, dev_mode.PelsWidth, dev_mode.PelsHeight))

hwnd = None

# 使用默认浏览器打开www.sina.com.cn
flag = win32api.ShellExecute(hwnd, 'open', 'www.sina.com.cn', None,
'‪C:\\Users\\linji\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Internet Explorer.exe', 0)

print("打开返回标识 %s " % (flag))