from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import os
import sys
from selenium import webdriver
import random
import time
os.system("apt install toilet")
color1=["\033[1;31;40m","\033[1;32;40m","\033[1;33;40m","\033[1;34;40m","\033[1;35;40m","\033[1;36;40m"]
def color():
 return str(random.choice(color1))
def banner():
 os.system("clear")
 os.system("toilet -fmono12 -F gay Bot")
 print("    \033[1;36;40m Code made by: \033[1;32;40m tuhin1729")
 print("    \033[1;36;40m Instagram id: \033[1;32;40m www.instagram.com/tuhin1729")
 print("    \033[1;36;40m Github      : \033[1;32;40m www.github.com/tuhin1729")
 print("    \033[1;36;40m YouTube     : \033[1;32;40m https://bit.ly/TuhinTheHacker")
 print("    \033[1;36;40m Dedicated to: \033[1;34;40m Diya Saha")
 print("        \033[1;31;40mSome Proxies May Be Dead. :(")
 print("        \033[1;31;40mRemember:The Website In Which You Are Testing May Identify This Bot.")
 print("\n\n") 
def req(target_url,time_out,stay_time):
 req_proxy=RequestProxy()
 proxies=req_proxy.get_proxy_list()
 os.system("clear")
 for var in range (0,(len(proxies)-1)):
  PROXY=proxies[var].get_address()
  print("\033[1;32;40mTrying From"+str(PROXY))
  try:   
   os.system("clear")
   webdriver.DesiredCapabilities.FIREFOX['proxy']={"httpProxy":PROXY,"ftpProxy":PROXY,"sslProxy":PROXY,"proxyType":"MANUAL"}
   driver=webdriver.Firefox()
   driver.set_page_load_timeout(time_out)
   driver.get(target_url)
   time.sleep(stay_time)
   driver.close()
  except Exception as e: 
   driver.close()
banner()
target=raw_input("\033[1;33;40mEnter The Target URL(Ex: https://www.google.com) :")
if("tuhin1729" in target):
 print("You can't use it my website.")
 sys.exit()
timeout=int(raw_input("\033[1;33;40mEnter The Time Out(In Seconds) :"))
stay=int(raw_input("\033[1;33;40mEnter The Stay Time(In Seconds) :"))
banner()
req(target,timeout,stay)
 
