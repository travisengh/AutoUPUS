import os
import datetime as dt

pwd = '@ShadoW1234037%'
update = 'apt update -y && sudo apt upgrade -y'
today = dt.datetime.today().day
os.system('echo %s|sudo -S %s' % (pwd, update))

if today == 1:
    os.system('sudo apt autoremove -y && sudo autoclean && sudo reboot')
