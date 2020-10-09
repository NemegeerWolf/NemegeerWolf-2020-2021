import time
n = int(input("geeft een tijd dat je wilt wachten(in seconden): "))
while n > 0:
    n = n - 1
    print(n)
    time.sleep(1)
else:
    print("alarm gaat af: beep, beep, beep...")