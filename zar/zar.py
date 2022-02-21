f=open("ajto.txt")
kodok=[]
for egysor in f:
    kodok.append(egysor[:-1])
f.close()
print(kodok)
