with open ("dati.txt","r",encoding="utf-8") as file:
    saturs = file.read()
print(saturs)

with open ("dati.txt","r",encoding="utf-8") as file:
    rindas = file.readlines()
    print(rindas)
for rinda in rindas:
    print(rinda.strip())


#split
with open ("dati.txt","r",encoding="utf-8") as file:
    saturs = file.read()
    vardi = saturs.split()
print(vardi)
print(len(vardi))
print(len(set(vardi)))

#enumerate

for index,rinda in enumerate(rindas,start= 1):
    print(f"{index},{rinda}")

#noraditaiss_burts
noraditais_burts = "k"
with open ("dati.txt","r",encoding="utf-8") as file:
    saturs = file.read()

saturs = saturs.lower()

vardi= saturs.split()
sara=[]
for i in vardi:
    if i [0] == "k":
        sara.append(i)
        
    else:
        pass
print(sara)
print(len(sara))