from pywinauto import application
import time
import os
import json
with open(os.path.join(os.getcwd(), 'info.json'),'r',encoding='utf8') as f:
    info = json.load(f)
    
os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
os.system('wmic process where "name like \'%DibServer%\'" call terminate')
time.sleep(5)        

app = application.Application()
app.start(f'''C:\CREON\STARTER\coStarter.exe /prj:cp /id:{info['id']} /pwd:{info['password']} /pwdcert:{info['certpassword']} /autostart')''')
time.sleep(60)