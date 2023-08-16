import time
import math, random
from array import *

print("WELCOME")
print("PLEASE INSERT THE CARD")
time.sleep(2)
print("PLEASE WAIT CHECKING.....")
time.sleep(5)
print("PLEASE SELECT YOUR LANGUAGE")
print("PRESS OPTION :1 - ENGLISH")
print("PRESS OPTION :2 - HINDI")
print("PRESS OPTION :3 -TELUGU")
print("ENTER YOUR OPTION")
y = int(input())
person1 = [1000032, 100000]
p1 = [7890564321]
person2 = [1000045, 10000]
p2 = [1234567890]
lst = []
def eng():
    print("ENTER YOUR ACCOUNT NUMBER")
    A = int(input())
    print("ENTER YOUR PHONE NUMBER")
    for i in range(1):
        i = int(input())
        lst.append(i)
    if (p1 == lst and A == person1[0]):
        b(person1, 1)
    elif (p2 == lst and A == person2[0]):
        d(person2, 1)
    else:
        print("SOMETHING WENT WRONG")
def b(n, q):
    digits = "123456789"
    x = ""
    for i in range(4):
        x += digits[math.floor(random.random() * 9)]
    print("YOUR OTP HAS GENTRATED :", x)
    print("ENTER YOUR OTP")
    y = input()
    if (x == y):
        print("CHECK YOUR DETAILS")
        print("NAME : RAVI KUMAR ")
        print("AMOUNT IN YOUR BANK :", person1[1])
        c(n, q)
    else:
        print("SOMETHING WENT WRONG")
def d(n, q):
    digits = "123456789"
    x = ""
    for i in range(4):
        x += digits[math.floor(random.random() * 9)]
    print("YOUR OTP HAS GENTRATED :", x)
    print("ENTER YOUR OTP")
    y = input()
    if (x == y):
        print("CHECK YOUR DETAILS")
        print("NAME : KARTHIK REDDY ")
        print("AMOUNT IN YOUR BANK :", person2[1])
        c(n, q)
    else:
        print("SOMETHING WENT WRONG")
def c(n, q):
    print("PRESS OPTION :1 - WITHDRAWL")
    print("PRESS OPTION :2 - EXIT")
    print("ENTER YOUR OPTION")
    g = int(input())
    if (g == 1):
        w(n, q)
    elif (g == 2):
        e()

    else:
        print("SOMETHING WENT WRONG")
def w(n, q):
    person1 = [1000032, 100000]
    person2 = [1000045, 10000]
    print("MONEY FOR WITHDRAWL")
    k = int(input())
    if (k <= n[q]):
        if (k % 500 == 0):
            person1 = n[q] - k
            print("PLEASE COLLECT YOUR CASH ")
            print("REMANING BALANCE : ", person1)
            print("  **         THANKS FOR VISITING    ****      ")
        else:
            print("SOMETHING WENT WRONG")
    else:
        print("SOMETHING WENT WRONG")
def e():
    print("  **         THANKS FOR VISITING    ****      ")
# hin fun start
def hin():
    print("अपना खाता नंबर दर्ज करें")
    A = int(input())
    print("अपना दूरभाष क्रमांक दर्ज करें")
    for i in range(1):
        i = int(input())
        lst.append(i)
    if (p1 == lst and A == person1[0]):
        h(person1, 1)
    elif (p2 == lst and A == person2[0]):
        u(person2, 1)
    else:
        print("कुछ गलत हो गया")
def h(n,q):
    digits="123456789"
    x =""
    for i in range (4):
        x += digits[math.floor(random.random()*9)]
    print("आपका OTP जेंट्रेट हो गया है :", x)
    print("अपना भरें OTP")
    y = input()
    if (x == y):
        print("अपना विवरण जांचें")
        print("नाम : रवि कुमार ")
        print("आपके बैंक में राशि :",person1[1])
        d(n,q)
    else:
        print("कुछ गलत हो गया")
def u(n,q):
    digits = "123456789"
    x = ""
    for i in range(4):
        x += digits[math.floor(random.random() * 9)]
    print("आपका OTP जेंट्रेट हो गया है :", x)
    print("अपना भरें OTP")
    y = input()
    if (x == y):
        print("अपना विवरण जांचें")
        print("नाम : कार्तिक रेड्डी ")
        print("आपके बैंक में राशि :", person2[1])
        d(n,q)
    else:
        print("कुछ गलत हो गया")
def d(n,q):
    print("PRESS OPTION :1 - WITHDRAWL")
    print("PRESS OPTION :2 - EXIT")
    print("ENTER YOUR OPTION")
    g = int(input())
    if (g == 1):
        l(n,q)
    elif (g == 2):
        e()
    else:
        print("कुछ गलत हो गया")
def l(n,q):
   person1 = [1000032, 100000]
   person2 = [1000045, 10000]
   print("निकासी के लिए पैसा")
   k=int(input())
   if (k <= n[q]):
        if (k % 500 == 0):
            person1 = n[q]-k
            print("कृपया अपना कैश जमा करें ")
            print("शेष राशि : ", person1)
            print("  **         आने के लिए धन्यवाद    ****      ")
        else:
            print("कुछ गलत हो गया")
   else:
        print("कुछ गलत हो गया")
def e():
    print("  **         आने के लिए धन्यवाद    ****      ")

# tel fun start
def tel():
    print("మీ ఖాతా నంబర్‌ను నమోదు చేయండి")
    A = int(input())
    print("మీ ఫోన్ నెంబర్ ను ఎంటర్ చేయండి")
    for i in range(1):
        i = int(input())
        lst.append(i)
    if (p1 == lst and A == person1[0]):
        t(person1, 1)
    elif (p2 == lst and A == person2[0]):
        o(person2, 1)
    else:
        print("ఏదో తప్పు జరిగింది")
def t(n,q):
    digits="123456789"
    x =""
    for i in range (4):
        x += digits[math.floor(random.random()*9)]
    print("మీ OTP వచ్చింది :", x)
    print("మీ OTPని నమోదు చేయండి")
    y = input()
    if (x == y):
        print("మీ వివరాలను తనిఖీ చేయండి")
        print("పేరు : రవి కుమార్ ")
        print("మీ బ్యాంక్‌లోని మొత్తం :",person1[1])
        m(n,q)
    else:
        print("ఏదో తప్పు జరిగింది")
def o(n,q):
    digits = "123456789"
    x = ""
    for i in range(4):
        x += digits[math.floor(random.random() * 9)]
    print("మీ OTP వచ్చింది :", x)
    print("మీ OTPని నమోదు చేయండి")
    y = input()
    if (x == y):
        print("మీ వివరాలను తనిఖీ చేయండి")
        print("పేరు : కార్తీక్ రెడ్డి ")
        print("మీ బ్యాంక్‌లోని మొత్తం :", person2[1])
        m(n,q)
    else:
        print("ఏదో తప్పు జరిగింది")
def m(n,q):
    print("PRESS OPTION :1 - WITHDRAWL")
    print("PRESS OPTION :2 - EXIT")
    print("ENTER YOUR OPTION")
    g = int(input())
    if (g == 1):
        v(n,q)
    elif (g == 2):
        z()

    else:
        print("ఏదో తప్పు జరిగింది")
def v(n,q):
   person1 = [1000032, 100000]
   person2 = [1000045, 10000]
   print("ఉపసంహరణ కోసం డబ్బు")
   k=int(input())
   if (k <= n[q]):
        if (k % 500 == 0):
            person1 = n[q]-k
            print("దయచేసి మీ నగదును సేకరించండి ")
            print("మిగిలిన మొత్తం : ", person1)
            print("  **         సందర్శించినందుకు ధన్యవాదాలు    ****      ")
        else:
            print("ఏదో తప్పు జరిగింది")
   else:
        print("ఏదో తప్పు జరిగింది")
def z():
    print("  **         సందర్శించినందుకు ధన్యవాదాలు    ****      ")

if (y == 1):
    eng()
elif (y == 2):
    hin()
elif (y == 3):
    tel()
else:
    print("INVALID OPTION")
    print("PLEASE TRY AGAIN")
