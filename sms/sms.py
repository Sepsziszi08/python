import modul

f=open("sms.txt")
sorok=f.read().split("\n")[1:-1]
f.close()

print(sorok)
smsek=[]
for i in range(0,len(sorok)//2):
    smsek.append(modul.adatok(sorok[i*2],sorok[i*2+1]))

print("2. feladat")
print("{}".format(smsek[-1].uzenet))

print("3. feladat")
minindex=0
maxindex=0

for a in range(0, len(smsek)):
    if len(smsek[1].uzenet)>len(smsek[maxindex].uzenet):
        maxindex=a
    if len(smsek[1].uzenet)>len(smsek[minindex].uzenet):
        minindex=a

print("óra:{} perc:{} telefonszám:{} üzenet:{}".format(smsek[maxindex].ora,
                                                       smsek[maxindex].perc,
                                                       smsek[maxindex].telefonszam,
                                                       smsek[maxindex].uzenet))

print("óra:{} perc:{} telefonszám:{} üzenet:{}".format(smsek[minindex].ora,
                                                       smsek[minindex].perc,
                                                       smsek[minindex].telefonszam,
                                                       smsek[minindex].uzenet))
