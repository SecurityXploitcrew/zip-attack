#-*- coding: utf-8 -*-
#securityxploitcrew

import zipfile
import os,time,sys


jum = 1

a = """
   ╔═╗┬┌─┐       ╔═╗┌┬┐┌┬┐┌─┐┌─┐═╗ ╦
   ╔═╝│├─┘  ───  ╠═╣ │  │ ├─┤│  ╔╩╦╝
   ╚═╝┴┴         ╩ ╩ ┴  ┴ ┴ ┴└─┘╩ ╚═
              [ BRUTE FORCE ZIP FILE ]
"""
print a
print ""
zip = raw_input("File Zip: ")
wor = raw_input("wordlist: ")

x = zipfile.ZipFile(zip)

p = open(wor, "r")

for o in p.readlines():
    pas = o.strip()

    try:
        x.extractall(pwd=pas)
        print ""
        print "=======[",jum,"]======="
        print "\033[32;1msuccses :\033[37;1m ", pas
        print ""
        print ""
        break
    except:
        print "\033[31;1mnone :\033[33;1m", pas
        jum += 1
