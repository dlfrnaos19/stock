from pywinauto import application
import os, time, json
with open('info.json') as f:
    info = json.load(f)
os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
os.system('wmic process where "name like \"%coStarter%\'" call terminate')
os.system('wmic process where "name like \"%CpStart%\'" call terminate')
os.system('wmic process where "name like \"%DibServer%\'" call terminate')

time.sleep(5)
app = application.Application()
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp '
          '/id:{} /pwd:{} /pwdcert:{} /autostart'.format(info['id'], info['pwd'], info['pwdcert']))
time.sleep(30)