import json

try:
    with open("people_data.json","r",encoding='utf-8') as file:
        people=json.load(file)
except FileNotFoundError:
    people=[]
while True:
    name=input("Ievadiet vārdu: ")
    age=input("Ievadiet vecumu: ")
    city=input("Ievadiet pilsetu: ")

    people.append({
        "name":name,
        "age":age,
        "city":city
    })

    another=input("Vai vēlaties pievienot vēl vienu cilvēku? (jā/nē)")
    if another !="jā":
        break
with open("people_data.json","w",encoding='utf-8') as file:
    json.dump(people,file,indent=4)

    print("Dati ir veiksmīgi saglabāti JSON failā!")

for person in people:
    if int(person["age"]) >= 18:
        print(f"Vārds:{person['name']},Vecums:{person['age']},Pilseta{person['city']}")
for person in people:  
    if int(person["city"][0]) =="R":
        print(f"Pilsetas kura pirmais burts ir R:{people["city"]}")

    
