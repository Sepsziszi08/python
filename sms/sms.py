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


stat=[0,0,0,0,0]

for a in smsek:
    if len(a.uzenet)<=20:
        stat [0]+=1
    elif len(a.uzenet)<=40:
        stat[1]+=1
    elif len(a.uzenet)<=60:
        stat[2]+=1
    elif len(a.uzenet)<=80:
        stat[3]+=1
    else:
        stat[4]+=1

print("4. feladat")
print("1-20:{} db, 21-40:{} db, 41-60:{} db, 61-80:{} db, 81-100:{} db".format(stat[0],stat[1],stat[2],stat[3],stat[4]))

stat2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for a in smsek:
    stat[a.ora]+=1

ossz=0
for a in stat:
    if a>10:
        ossz+=a-10

print("5. feladat")
print("Ernőnek {} sms-t kell fizetnie".format(ossz))
