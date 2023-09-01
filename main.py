import time

zaman = int(input("Geri sayımın başlamısını istediğiniz saniye bilgisini giriniz"))
sayac=0

while (sayac != zaman):
    time.sleep(1)
    sayac=sayac+1
    print(sayac)


