#-----------Main-----------#
import os,sys,time,random,string
import json.platform
#-----------import-----------#
try:
	import requests
except importError:
	os.system('pip install requests')
	import mechanize
except importError:
	os.system('pip install mechanize')
	import bs4
except importError:
	os.system('pip install bs4')
#-----------xnx-----------#
from concurrent.futures import ThreadPoolExecutor as xnx
from bs4 import beautifulsoup as sop

#-----------colour-----------#
green='\033[1:32m'
red='\003[1:31m'
yellow='\033[1:33m'
blue='\033[1:34'

#-----------logo-----------#
def logo( ):
	os.system('clear')
	print(f"""{white}
     _____  _  __      _   
    |  __ \(_)/ _|    | |  
    | |__) |_| |_ __ _| |_ 
    |  _  /| |  _/ _` | __|
    | | \ \| | || (_| | |_ 
    |_|  \_\_|_| \__,_|\__|
    
    --------------------------------------------------------------------------------
    {white}[{green}+{white}]  FACEBOOK  :Ahmed Shaon
   {white}[{green}+{white}]  GITHUB        :ahmed shaon 123
   {white}[{green}+{white}]  QUALITY      :TESTING
   ---------------------------------------------------------------------------------""")
   
#-----------ahmed_main-----------#
def main_Rifat( ) :
       logo( ) 
       
       
try:
      main_Ahmed( ) 
except:
    main_Ahmed( )
