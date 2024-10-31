import csv
with open('grāmata1.csv',mode='r',encoding='utf-8') as file:
    csvFile=csv.reader(file)

    for lines in csvFile:
        print(lines)

fields=['Nr','Name','Year']

rows=[['1','Nikhil','21'],
      ['2','Sany','20'],
      ['2','Adit','23']]

with open("student.csv",'w',newline='') as csvfile:
    csvwriter= csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
skaits= 0
with open("studenti.csv",'r',encoding='utf-8') as file:
    csvFile= csv.DictReader(file)
    for lines in csvFile:
        if int(lines['Vecums']) > 20:
            skaits +=1
        print(lines)
print(f'studentu skaits vecāki par 20 gadiem:{skaits}')




Kopa=['Produkta nosaukums','Cena','Daudzums']

Visi=[
['Ābols','0.5','10'],
['Banāns','0.3','15'],
['Piens','1.2','7']
] 
with open("produkti.csv",'w',encoding='utf-8',newline='') as csvfile:
    csvwriter= csv.writer(csvfile)
    csvwriter.writerow(Kopa)
    csvwriter.writerows(Visi)

print("Darbība notika!!!!!!!")
kop_alga=0
vid_alga=0
darbniekusk=0
with open('darbnieki.csv','r',encoding='utf-8',newline='') as file:
    csvFile=csv.DictReader(file)

    for i in csvFile:
        kop_alga+=int(i['Alga'])
        print(i)
        darbniekusk+=1
vid_alga=kop_alga/darbniekusk
print(kop_alga)
print(vid_alga)