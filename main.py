#!/usr/bin/env python

import threading

import string

import base64

import urllib.request

import urllib.parse

import os

import time

import sys

import random

try:

    import requests

except ImportError:

    os.system('pip2 install requests')



try:

    request = requests.get("https://www.google.com/search?q=tahmid+rayat", timeout=3)

except (requests.ConnectionError, requests.Timeout) as exception:

    print("[!] No internet connection [!]")

    sys.exit()

import requests

from bs4 import BeautifulSoup









yellow='\033[93m'

gren='\033[92m'

cyan='\033[96m'

pink='\033[95m'

red='\033[91m'

b='\033[1m'

W = '\033[0m'

colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']





"""

Rq URl Library

"""



class RqUrl:                  # RqUrl library codes

    f_val = ""

    url = ""

    rq_url = ""

    soup = ""

    find_tag = ""

    find_intag = ""

    find_tagtxt = ""

    val_txt = ""

    sender = ""

    rq_url2 = ""

    url1 = ""

    sender_tag = ""

    sender_intag = ""

    sender_tagtxt = ""

    f_val1 = ""



    def Rq_html(self):

        rq_url = requests.get(self.url)

        soup = BeautifulSoup(rq_url.content, "lxml")

        f_tag = soup.find_all(self.find_tag)

        for link in f_tag:

            yazdırlist = link.get(self.find_intag)

            print(yazdırlist)

    def Sender(self):

        rq_url = requests.get(self.url)

        soup = BeautifulSoup(rq_url.content, "lxml")

        f_val1 = soup.findAll(self.sender_tag,{self.sender_intag:self.sender_tagtxt})

        for value2 in f_val1:

            sender_val = value2.text

        print("----------------------------------------------\n Sender:",sender_val)

    def Rq(self):

        rq_url = requests.get(self.url)

        soup = BeautifulSoup(rq_url.content, "lxml")

        f_val = soup.findAll(self.find_tag,{self.find_intag:self.find_tagtxt})

        for value in f_val:

            val_txt = value.text

            print("\n\nMessage:",val_txt,"\n ------------------------------------------------------------------------ \n\n",)













def clr():

    if os.name == 'nt':

        os.system('cls')

    else:

        os.system('clear')

def banner():

    clr()

    logo = """



\033[96m\ \   / /___  _ __ (_) / _|(_)  ___  __ _ | |_ (_)  ___   _ __  \033[92m| \ | | _

\033[96m \ \ / // _ \| '__|| || |_ | | / __|/ _` || __|| | / _ \ | '_ \ \033[92m|  \| || | | || '_ ` _ \



\033[96m  \ V /|  __/| |   | ||  _|| || (__| (_| || |_ | || (_) || | | |\033[92m| |\  || |_| || | | | | |

\033[96m   \_/  \___||_|   |_||_|  |_| \___|\__,_| \__||_| \___/ |_| |_|\033[92m|_| \_| \__,_||_| |_| |_|



Choose the service you want to use



\033[0m[1] \033[96mhttps://sms-online.co/receive-free-sms/



\033[92mType -help into the console to learn commands

                                         """

    print(logo)

    print("\n")



banner()







console1 = input("\033[91m \n\n[*]VerificationNum:\033[0m " )





""" Anw1 Function Start """



def anw1():



     print("\n Connecting this website...")

     time.sleep(1)

     clr()

     nums = """



\033[96m\ \   / /___  _ __ (_) / _|(_)  ___  __ _ | |_ (_)  ___   _ __  \033[92m| \ | | _

\033[96m \ \ / // _ \| '__|| || |_ | | / __|/ _` || __|| | / _ \ | '_ \ \033[92m|  \| || | | || '_ ` _ \



\033[96m  \ V /|  __/| |   | ||  _|| || (__| (_| || |_ | || (_) || | | |\033[92m| |\  || |_| || | | | | |

\033[96m   \_/  \___||_|   |_||_|  |_| \___|\__,_| \__||_| \___/ |_| |_|\033[92m|_| \_| \__,_||_| |_| |_|



Choose the phone number you want to use



\033[0m[1] \033[96m+1 201-857-7757

\033[0m[2] \033[96m+1 787-337-5275

\033[0m[3] \033[96m+60 11-1700 0917

\033[0m[4] \033[96m+44 7520 635797

\033[0m[5] \033[96m+46 76 943 62 66







                                         """

     print(nums)

     console2 = input("\033[91m \n\n[*]VerificationNum:\033[0m " )

     def c2Anw1():



        print("Connecting to sms number")

        time.sleep(1)

        while True:

          clr()

          site1 = RqUrl()

          site1.url = "https://sms-online.co/receive-free-sms/12018577757"

          site1.find_tag = "div"

          site1.find_intag = "class"

          site1.find_tagtxt = 'list-item-content'

          site1.url1 = "https://sms-online.co/receive-free-sms/12018577757"

          site1.sender_tag = "div"

          site1.sender_intag = "class"

          site1.sender_tagtxt = 'list-item-header'

          site1.Sender()

          site1.Rq()



          time.sleep(10)



     def c2Anw2():

        print("Connecting to sms number")

        time.sleep(1)

        while True:

          clr()

          site2 = RqUrl()

          site2.url = "https://sms-online.co/receive-free-sms/17873375275"

          site2.find_tag = "div"

          site2.find_intag = "class"

          site2.find_tagtxt = 'list-item-content'

          site2.Rq()

          time.sleep(10)

     def c2Anw3():

        print("Connecting to sms number")

        time.sleep(1)

        while True:

          clr()

          site2 = RqUrl()

          site2.url = "https://sms-online.co/receive-free-sms/601117000917"

          site2.find_tag = "div"

          site2.find_intag = "class"

          site2.find_tagtxt = 'list-item-content'

          site2.Rq()

          time.sleep(10)

     def c2Anw4():

        print("Connecting to sms number")

        time.sleep(1)

        while True:

          clr()

          site3 = RqUrl()

          site3.url = "https://sms-online.co/receive-free-sms/447520635797"

          site3.find_tag = "div"

          site3.find_intag = "class"

          site3.find_tagtxt = 'list-item-content'

          site3.Rq()

          time.sleep(10)

     def c2Anw5():

        print("Connecting to sms number")

        time.sleep(1)

        while True:

          clr()

          site4 = RqUrl()

          site4.url = "https://sms-online.co/receive-free-sms/46769436266"

          site4.find_tag = "div"

          site4.find_intag = "class"

          site4.find_tagtxt = 'list-item-content'

          site4.Rq()

          time.sleep(10)







     if ( console2 == "1"):

         c2Anw1()

     if ( console2 == "2"):

         c2Anw2()

     if ( console2 == "3"):

         c2Anw3()

     if ( console2 == "4"):

         c2Anw4()

     if ( console2 == "5"):

         c2Anw5()







     """   Anw1 Function End """



def helpage():

    helpage_ = """



    Commands



    """

    print(helpage_)





if ( console1 == "1" ):

     anw1()

if ( console1 == "-help"):

     helpage()

