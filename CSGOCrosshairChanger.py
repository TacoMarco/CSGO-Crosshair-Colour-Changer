from os.path import isfile
from random import choice

colours = [0, 1, 2, 4, 5]
path = 'C:/Program Files/Steam/steamapps/common/Counter-Strike Global Offensive/csgo/cfg/'

if isfile('C:/Users/Public/csgopath'):
    path = open('C:/Users/Public/csgopath').read()

if isfile(path + "autoexec.cfg"):
        open(path + "autoexec.cfg", "a").write(f"\ncl_crosshaircolor {choice(colours)}")
        print('wrote')
else:
    CreateCfgFile = open(path + "autoexec.cfg", "w+").write(f"cl_crosshaircolor {choice(colours)}")
